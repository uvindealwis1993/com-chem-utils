#!/usr/bin/python
'''
Pull out info from LModeA, print the local force constants of
interest.

Daniel P. Devore
Feb. 18, 2022
'''
#Import important libraries
import math
#import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
#Open LModeA output file
LModeA = open('job.out','r')
#Put file in list format
LMDA = LModeA.readlines()
#Go back to top
LModeA.seek(0)
#Find where the coordinates start to find atom indeces
atoms = LMDA.index(' Cartesian coordinates (Angstrom)\n')
#print(atoms)
#print(LMDA[atoms + 4])
#Find where the Point group symmetry is located
PGsym = LMDA.index(' <<< POINT GROUP SYMMETRY >>>\n')
#print(PGsym)
#print(LMDA[PGsym - 4])
locmodeprop = LMDA.index(' Local mode properties:\n')
#print(locmodeprop)
#print(LMDA[locmodeprop + 4])
IRprop = LMDA.index(' IR intensity derived electronic properties:\n')
#print(IRprop)
#print(LMDA[IRprop - 3])
atind = []
numfreq = []
freqlist = []
pg = []
NMind = []
IRint = []
lmind = []
lmind_test = []
lfconst = []
lmatoms = []
element = {
}
#Go through each line in file
for line in LModeA:
    #print(LMDA.index(line))
#Add the indice and atom to a list
    if atoms + 3 < LMDA.index(line) < PGsym - 3:
        #print(line)
        #Split line into a list
        coord = line.split()
        #print(coord)
        atind.append([coord[0],coord[1]])
        element.update({coord[0]: coord[1]})
#Find out number of frequencies in file
    if LMDA.index(line) == PGsym + 1:
        PGS = line.split()
        #print(PGS)
        pg.append(PGS[3])
        #If linear point group 3N-5
        if pg[0] == 'Dooh' or 'Coov':
            dof = (3 * len(atind)) - 5
            numfreq.append(dof)
        #If not linear point group 3N-6
        else:
            dof = (3 * len(atind)) - 6
            numfreq.append(dof)
#Add frequencies and normal mode indeces to lists
    if 'Frequencies' in line:
        indpos = LMDA.index(line) - 2
        indlist = LMDA[indpos].split()
        flist = line.split()
        freqlist.append(float(flist[1]))
        NMind.append(indlist[0])
        if len(freqlist) != numfreq[0]:
            freqlist.append(float(flist[2]))
            NMind.append(indlist[1])
        if len(freqlist) != numfreq[0]:
            freqlist.append(float(flist[3]))
            NMind.append(indlist[2])
#Add IR intensities in a list
    if line.startswith('  IR intensities') == True:
        IRintlist = line.split()
        IRint.append(float(IRintlist[2]))
        if len(IRint) != numfreq[0]:
            IRint.append(float(IRintlist[3]))
        if len(IRint) != numfreq[0]:
            IRint.append(float(IRintlist[4]))
#Add atom indeces and force constants into lists
    if locmodeprop + 3 < LMDA.index(line) < IRprop - 2:
        lmlist = line.split()
        #print(lmlist)
        lfconst.append(lmlist[8])
        if int(lmlist[3]) > 0:
            lmind_test.append([lmlist[1],lmlist[2],lmlist[3]])
        elif int(lmlist[3]) and int(lmlist[4]) > 0:
            lmind_test.append([lmlist[1],lmlist[2],lmlist[3],lmlist[4]])
        else:
            lmind_test.append([lmlist[1],lmlist[2]])
    #Remove any duplicates in lmind list
    for x in lmind_test:
        if x not in lmind:
            lmind.append(x)
#Create a list of the local mode indeces with the element
for a in lmind:
    if len(a) == 2:
        lmatoms.append(element[a[0]] + element[a[1]])
    elif len(a) == 3:
        lmatoms.append(element[a[0]] + element[a[1]] + element[a[2]])
    else:
        lmatoms.append(element[a[0]] + element[a[1]] + element[a[2]] + element[a[3]])
#print(lmind)
#print(lmatoms)
#Find index for CI, CC, and CN local modes
count = 0
CXk = []
for b in lmatoms:
    count += 1
    if 'N' in b:
        if len(b) < 3:
            if 'C' not in b:
                print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
                CXk.append(lfconst[count - 1])
                print(lmind[count - 1])
        else:
            for d in b:
                cnt = 0
                #print(d)
                if (d.islower()) == True:
                    cnt += 1
                    #print(d)
                    if cnt == 1:
                        print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
                        CXk.append(lfconst[count - 1])
                        print(lmind[count - 1])
    if 'C' in b:
        if len(b) < 3:
            print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
            print(lmind[count - 1])
        else:
            for d in b:
                cnt = 0
                if (d.islower()) == True:
                    cnt += 1
                    if cnt == 1:
                        print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
                        CXk.append(lfconst[count - 1])
                        print(lmind[count - 1])
    if 'H' in b:
        if len(b) < 3:
            print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
            print(lmind[count - 1])
        else:
            for d in b:
                cnt = 0
                if (d.islower()) == True:
                    cnt += 1
                    if cnt == 1:
                        print('Force Constant of ' + b + ' ' + 'stretch' + ' ' + '=' + ' ' + lfconst[count - 1])
                        CXk.append(lfconst[count - 1])
                        print(lmind[count - 1])    
for c in CXk:
    if c == 'Unphysical':
        unread = CXk.index(c)
        CXk.pop(unread)
#print(CXk)
LModeA.close()
