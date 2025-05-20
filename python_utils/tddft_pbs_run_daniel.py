#!/usr/bin/python
'''
Daniel Devore

Add IOp to tddft.gjf files
'''
#Initialize system with wanted input file
import sys
g16 = open("g16.pbs","r")
glines = g16.readlines()
g16.close()
gpbs = open('g16.pbs','w')
for line in glines:
	if 'input1' in line:
		comm = '#' + line
		gpbs.write(comm)
	elif 'sleep' in line:
		com = '#' + line
		gpbs.write(com)
	else:
		gpbs.write(line)
gpbs.close()
