#!/usr/bin/python
'''
Daniel Devore

Add IOp to tddft.gjf files
'''
#Initialize system with wanted input file
import sys
IOp = 'IOp(9/40=4)\n'
td = open("tddft.gjf","r")
tdlines = td.readlines()
td.close()
tddft = open('tddft.gjf','w')
for line in tdlines:
	if line.startswith('#') == True:
		funct = line.strip('\n')
		calc = funct + ' ' +  IOp
		tddft.write(calc)
	else:
		tddft.write(line)
tddft.close()
