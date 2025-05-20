#!/usr/bin/python
'''
                                                           
  Overall objective: Find the closest atom from the atom of 
  interest and find the indice of the atom. Create the 
  job.inp file for LModeA using the bond of the atom of 
  interest as the Local Mode that is being studied. 
                                                           
'''
import math
#Open opt.log file in read mode
opt = open('freq.log','r')
#Put everything in a list format
line = opt.readlines()
#print(line)
#Go back to the top of the file
opt.seek(0)
#Go through everyline in the opt file
for ln in opt:
    #find the line that ends with an @ symbol
	if ln.endswith('@\n') == True:
		symbol = ln
#Find the start and end of the text block that has the data
blockstart = line.index(' Test job not archived.\n')
blockend = line.index(symbol)
#print(blockstart)
#print(blockend)
opt.seek(0)
#Create empty lists to copy the data to
da = []
dat = []
data = []
#Start a counter that begins at the block of data and for a new list
n = blockstart
i = 0
#Go through each element and strip unnecessary space
while n < blockend:
	da.append(line[n].strip('\n'))
	dat.append(da[i].strip())
	n += 1
	i += 1
#print(da)
#print(len(da))
#print(dat)
#Join all elements together in a single line
info = ''.join(dat)
#print(info)
#print(info.split('\\'))
#Separate all info in a list separated by a \
a = info.split('\\')
#print(a)
#Find and index the location of the coord for each atom
for m in a:
	if m.startswith('Version') == True:
		V = m
coordstart = a.index('0,1')
coordend = a.index(V)
#print(coordstart)
#print(coordend)
#Append all atoms coord to a list
o = 0
while o < coordend - 1:
	if o < coordstart + 1:
		o += 1
	else:
		data.append(a[o])
		o += 1
#print(data)
halogen = ['At','I','Br','Cl','F']
#separate each atom and coord
coord = []
for b in data:
    #print(b.split(','))
    #print(b.split(',')[0])
	coord.append(b.split(','))
#print(coord)
coords = []
#Separate the atoms and the coordinates and place the atoms as string in an empty list with float for coords
for c in coord:
    #print(c)
	coords.append(c[0])
    #coords.append([float(c[1]),float(c[2]),float(c[3])])
	coords.append([float(c[1]) * 0.529177249,float(c[2]) * 0.529177249,float(c[3]) * 0.529177249])
#print(coords)
#Find what the atom of interest in the molecule is and append the atom an coordinates to an empty list
AOI = []
atoms = []
acrds = []
indices = []
atind = []
AOI_coords = []
atom_of_interest = str(input('What atom is going to be studied for LModeA?'))
k = 0
str_count = 0
while k < len(coords):
	if type(coords[k]) == str:
		atoms.append(coords[k])
		atind.append(coords[k])
		str_count += 1
		atind.append(str_count)
		indices.append(str_count)
	if type(coords[k]) == list:
		acrds.append(coords[k])
		if coords[k - 1] == atom_of_interest:
			AOI.append(coords[k - 1])
			AOI.append(coords[k])
	k +=1
for x in AOI:
	if type(x) == list:
		AOI_coords.append(x[0])
		AOI_coords.append(x[1])
		AOI_coords.append(x[2])
#print(AOI_coords)
#print(AOI)
#print(acrds)
#print(atoms)
#print(indices)
#print(atind)
#Find the distance between AOI and other atoms of molecule and 
dist = []
closest_atom = []
all_dist = []
#Go through each coordinate in acrds and find the distances between those and the AOI
for d in acrds:
    #print(AOI_coords[0])
    #print(d[0])
	distance = math.sqrt((AOI_coords[0] - d[0]) ** 2 + (AOI_coords[1] - d[1]) ** 2 + (AOI_coords[2] - d[2]) ** 2)
    #print(distance)
	all_dist.append(distance)
	if distance > 0.0:
		dist.append(distance)
		if dist[0] > distance:
			dist.pop(0)
		if dist[0] < distance:
			dist.pop()
#print(all_dist)
#print(dist)
#Match the distance in dist to the indice that it corresponds to
count = 0
z = 0
AOI_ind = []
for y in all_dist:
	count += 1
    #print(y)
    #print(count)
	if y == dist[0]:
        #print(count)
		while z < len(atind):
			if atind[z] == count:
				closest_atom.append(atind[z - 1])
				closest_atom.append(atind[z])
				z += 1
			elif atind[z] == atom_of_interest:
				AOI_ind.append(atind[z])
				AOI_ind.append(atind[z + 1])
				z += 1
			else:
				z += 1
#print(closest_atom)
#print(AOI_ind)
#print(acrds[closest_atom[1] - 1])
Cdist = []
all_Cdist = []
nohalcoord = []
for nonhalo in acrds:
	if nonhalo != AOI_coords:
		nohalcoord.append(nonhalo)
#print(nohalcoord)
if closest_atom[0] == 'C':
	COI = acrds[closest_atom[1] - 1]
	for bndlen in nohalcoord:
		bnddist = math.sqrt((COI[0] - bndlen[0]) ** 2 + (COI[1] - bndlen[1]) ** 2 + (COI[2] - bndlen[2]) ** 2)
		all_Cdist.append(bnddist)
		if bnddist > 0.0:
			Cdist.append(bnddist)
			if Cdist[0] > bnddist:
				Cdist.pop(0)
			if Cdist[0] < bnddist:
				Cdist.pop()
rnd_Cdist = []
for C_len in Cdist:
	rnd_Cdist.append(round(C_len,6))
#print(rnd_Cdist)
#print(Cdist)
count_doubles = 0
for dub in all_Cdist:
	round_dist = round(dub,6)
	if round_dist == rnd_Cdist[0]:
		count_doubles += 1
#print(count_doubles)
#print(all_Cdist)
#print(len(Cdist))
zz = 0
closest_C = []
count_ind = 0
if count_doubles == 1:
	for length in all_Cdist:
		count_ind += 1
		if length == Cdist[0]:
			while zz < len(atind):
				if atind[zz] == count_ind:
					closest_C.append(atind[zz - 1])
					closest_C.append(atind[zz])
					zz += 1
				else:
					zz += 1
#print(closest_C)
#Final result must be put into a string with a space at the beginning
# Example bond = ' 1 2'
if len(closest_C) > 0:
	if closest_C[0] == 'C':
		if closest_atom[1] < AOI_ind[1]:
			bond = ' ' + str(closest_atom[1]) + ' ' + str(AOI_ind[1])
		else:
			bond = ' ' + str(AOI_ind[1]) + ' ' + str(closest_atom[1])
		if closest_atom[1] < closest_C[1]:
			CCbond = ' ' + str(closest_atom[1]) + ' ' + str(closest_C[1])
		else:
			CCbond = ' ' + str(closest_C[1]) + ' ' + str(closest_atom[1])
	#print(bond)
	#print(CCbond)
	else:
		if closest_atom[1] < AOI_ind[1]:
			bond = ' ' + str(closest_atom[1]) + ' ' + str(AOI_ind[1])
		else:
			bond = ' ' + str(AOI_ind[1]) + ' ' + str(closest_atom[1])
	#print(bond)
else:
	if closest_atom[1] < AOI_ind[1]:
		bond = ' ' + str(closest_atom[1]) + ' ' + str(AOI_ind[1])
	else:
		bond = ' ' + str(AOI_ind[1]) + ' ' + str(closest_atom[1])
#print(bond)
#Close file
opt.close()
#Add frequency script to the beginning of this script to write freqs in input file
#Open input file for LModeA
LMDA = open('job.inp','w')
#Write the comments in the first line to describe file
LMDA.write('Local Mode Analysis')
#Give new line before the rest of the file
LMDA.write('\n')
LMDA.write('\n $contrl')
LMDA.write('\n   qcprog="gaussian"')
LMDA.write('\n   iprint=1')
LMDA.write('\n   isymm=1')
LMDA.write('\n $end\n')
LMDA.write('\n $qcdata')
LMDA.write('\n   fchk="locmode.fchk"')
LMDA.write('\n $end\n')
LMDA.write('\n $LocMod $End\n')
LMDA.write(bond)
if 'CCbond' in locals():
	LMDA.write('\n')
	LMDA.write(CCbond)
LMDA.close()
