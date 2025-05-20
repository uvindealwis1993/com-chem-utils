#!/usr/bin/python
'''
interlayer.py version 3.0
Michael Cordes (Python 3.0)
Thomas L. Ellington (Python 2.7.5)
March 2, 2021
'''

import sys
import re
import numpy as np
from numpy import linalg
from itertools import combinations
from mpl_toolkits.mplot3d import Axes3D

if len(sys.argv) != 2:
    print "\nERROR: EXPECTING ARGUMENT. PLEASE SPECIFY GAUSSIAN OUTPUT FILE!\n"
    exit()
else:
    outputfile = sys.argv[1]

def open_file(outputfile):
    with open(outputfile) as f:
        data = f.read()
        data = re.sub('\n ', '', data)
        data = re.findall(r'[A-Z],-??\d\.\d+,-??\d\.\d+,-??\d\.\d+', data)
        atom_list = []
        atom_coords = []
        for i in range(len(data)):
            data[i] = re.split(',', data[i])
            atom_list.append(data[i][0])
            for j in range(len(data[i])-1):
                data[i][j+1] = float(data[i][j+1])
            atom_coords.append(data[i][1:4])
    return atom_list, atom_coords

def distance_formula(point_1, point_2):
    distance = ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2 + (point_1[2]-point_2[2])**2)**0.5
    return distance

def bonded_atoms(atom_list, atom_coords):
    vdw_radii = {'H':0., 'C':1.90, 'N':1.79, 'O':1.71, 'F':1.63, 'P':2.23, 'S':2.14, 'Cl':2.06}
    bonded_atoms = []
    for i in range(len(atom_coords)):
        bonds = []
        for j in range(len(atom_coords)):
            distance = distance_formula(atom_coords[i], atom_coords[j])
            vdw = (vdw_radii[atom_list[i]]+vdw_radii[atom_list[j]])/2
            if i != j and distance < vdw:
                bonds.append(j)
        bonded_atoms.append(bonds)
    return bonded_atoms

def rec(atom, atom_list, layer, elim):
    for i in atom:
        if i not in elim:
            layer.append(i)
            elim.append(i)
            rec(atom_list[i], atom_list, layer, elim)
    return layer

def layer_identifier(bonded_atoms):
    layers = []
    elim = []
    for i in range(len(bonded_atoms)):
        layer = []
        if bonded_atoms[i] not in elim:
            x = rec(bonded_atoms[i], bonded_atoms, layer, elim)
            if len(x) != 0:
                layers.append(x)
    return layers

def plane_generator(layer):
    coords = []
    for i in range(len(layer)):
        coords.append(atom_coords[layer[i]])
    xs = []
    ys = []
    for k in range(len(coords)):
        xs.append([coords[k][0], coords[k][1], 1])
        ys.append(coords[k][2])
    X = np.array(xs)
    Y = np.array(ys)
    a = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
    xx, yy, zz = np.meshgrid(X[:, 0], X[:, 1], X[:, 2])
    array = np.vstack((xx.flatten(), yy.flatten(), zz.flatten())).T
    combinedArray = array
    Z = array.dot(a)
    return combinedArray, Z

def layer_plane_generator(layers):
    combinedArrays = []
    Z = []
    for i in range(len(layers)):
        combinedArray, z = plane_generator(layers[i])
        combinedArrays.append(combinedArray)
        Z.append(z)
    return combinedArrays, Z

def layer_distance(Z):
    distances = []
    layers = len(Z)
    if layers > 1:
        centered_z = []
        for i in range(len(Z)):
            length = len(Z[i])
            z = np.zeros(length)
            for j in range(len(Z[i])):
                z[j] = Z[i][j]
            centered_z.append(np.mean(z))
        combos = [list(t) for t in combinations(list(range(0, layers)), 2)]
        for i in combos:
            distances.append(str((round(abs(centered_z[i[0]]-centered_z[i[1]]), 4))) + ' Angstroms between layers ' +str(i[0]) + ' and ' + str(i[1]) + '.\n')
    for i in distances:
        print i

atom_list, atom_coords = open_file(outputfile)
bonded_atoms = bonded_atoms(atom_list, atom_coords)
layers = layer_identifier(bonded_atoms)
combinedArrays, Z = layer_plane_generator(layers)
layer_distance(Z)
