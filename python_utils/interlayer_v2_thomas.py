#!/usr/bin/env python3
import sys
import re
import numpy as np 
from numpy import linalg
from itertools import combinations
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if len(sys.argv) != 2:
    print('ERROR: Input Gaussian .log or .txt file as second argument in command line!')
    exit()
filename = sys.argv[1]

# filename = 'P42H18-melamine.log'

def open_file(filename):
    #processes file
    #reg ex finds useful data, then formats it to atom type list and numpy array of atom coords
    #atom_list = ['element character such as 'H' for hydrogen', ...], atom_coord = [[x,y,z float coordinates of atom 1], [x,y,z atom 2], ...]
    with open(filename) as f:
        data = f.read()
        data = re.sub('\n ', '', data)
        data = re.findall(r'[A-Z],-??\d\.\d+,-??\d\.\d+,-??\d\.\d+', data)
        atom_list = []
        atom_coords = []
        for i in range(len(data)):
            data[i] = re.split(',', data[i]) #uses commas as delimiter
            atom_list.append(data[i][0]) #since first value in each list is element (like 'H'), seperates element type into own list = atom_list
            for j in range(len(data[i])-1):
                data[i][j+1] = float(data[i][j+1]) #seperates coords into other list = atom_coords
            atom_coords.append(data[i][1:4])
    return atom_list, atom_coords

#finds difference between 2 3d points
def distance_formula(point_1, point_2):
    distance = ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2 + (point_1[2]-point_2[2])**2)**0.5
    return distance

#uses van der waals radii to determine atomic bonds and layers
#output is list of lists with each list corresponding to atom, and nested list corresponding to atoms bonded to
#for 5 atoms w/ atom 0 bonded to atoms 4 and 5 output is [[4,5],[],[],[],[0],[0]]
def bonded_atoms(atom_list, atom_coords):
    van_der_waals_radii = {'H':0, 'C':1.90, 'N':1.79, 'O':1.71, 'F':1.63, 'P':2.30, 'S':2.14, 'Cl':2.06}
    bonded_atoms = []
    for i in range(len(atom_coords)):
        bonds = []
        for j in range(len(atom_coords)):
            distance = distance_formula(atom_coords[i], atom_coords[j]) #cycles through all atoms 
            van_der_waals = (van_der_waals_radii[atom_list[i]]+van_der_waals_radii[atom_list[j]])/2 
            if i != j and distance < van_der_waals: #compares distance and van der waals to determine if bonded
                bonds.append(j)
        bonded_atoms.append(bonds)
    return bonded_atoms

#recursively builds out tree by identifying all atoms bonded in series, returns all atoms in that layer
#variables: atom = recursion initial value, atom_list pulls other atom values, layer = final ouput, and elim are atoms already characterized in that layer
def rec(atom, atom_list, layer, elim):
    for i in atom:
        if i not in elim:
            layer.append(i)
            elim.append(i)
            rec(atom_list[i], atom_list, layer, elim)
    return layer

#calls recursive function, required or else recursive function will generate layer for each atom even if layer already identified
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

#generated 2d planar linear regression of each layer and creates mesh plane that can be plotted
#credit from https://github.com/chardur/MultipleLinearRegressionPython
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
    # Use Linear Algebra to solve
    a = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
    # create a wiremesh for the plane that the predicted values will lie on
    xx, yy, zz = np.meshgrid(X[:, 0], X[:, 1], X[:, 2])
    array = np.vstack((xx.flatten(), yy.flatten(), zz.flatten())).T
    combinedArray = array
    Z = array.dot(a)
    return combinedArray, Z

#calls plane generator to generate plane for all layers
def layer_plane_generator(layers):
    combinedArrays = []
    Z = []
    for i in range(len(layers)):
        combinedArray, z = plane_generator(layers[i])
        combinedArrays.append(combinedArray)
        Z.append(z)
    return combinedArrays, Z

#calculates distance between planes.
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
            distances.append(str((round(abs(centered_z[i[0]]-centered_z[i[1]]), 4))) +  ' angstroms between layer ' + str(i[0]) + ' and ' + str(i[1]) + '.\n')
    for i in distances:
        print(i)

#molecular viewer using 3d projections from matplotlib. Plots atoms, lables them, and plots planes corresponding to layers. 
def plot_planes(combinedArrays, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    for i in range(len(atom_coords)):
        ax.scatter(atom_coords[i][0], atom_coords[i][1], atom_coords[i][2], c = 'black')
        ax.text(atom_coords[i][0], atom_coords[i][1], atom_coords[i][2], atom_list[i]+str(i))
    for i in range(len(combinedArrays)):
        ax.plot_trisurf(combinedArrays[i][:, 0], combinedArrays[i][:, 1], Z[i], alpha=0.5)
        ax.text(combinedArrays[i][0][0], combinedArrays[i][0][1], Z[i][0], 'Layer ' + str(i), color = 'red', fontsize = 15)
    plt.show()

#generates atom data from raw
atom_list, atom_coords = open_file(filename)
#finds bonded atoms
bonded_atoms = bonded_atoms(atom_list, atom_coords) 
#finds layers
layers = layer_identifier(bonded_atoms)
#creates planes for those layers
combinedArrays, Z = layer_plane_generator(layers)
#calculates distance between planes
layer_distance(Z)
#plots planes and atoms 
plot_planes(combinedArrays, Z)
