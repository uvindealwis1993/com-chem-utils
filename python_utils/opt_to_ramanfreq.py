#!/usr/bin/python
'''
Daniel Devore

Convert opt.gjf to freq.gjf input files
'''
#Initialize system with wanted input file
import sys
if len(sys.argv) < 2:
#If argument is not given print error statement
        print "\nError: Expecting Argument. Please Specify Freq Input File\n"
else:
#Else open freq file
        opt = open("opt.gjf","r")
	optlines = opt.readlines()
	opt.close()
	freq = open('freq.gjf','w')
	for line in optlines:
		if line.startswith('%chk') == True:
			oldchk = line.replace('%chk','%oldchk')
			ramchk = line.replace('.chk','ramfreq.chk')
			freq.write(oldchk)
			freq.write(ramchk)
		elif 'freq' in line:
			ramfreq = line.replace('opt=tight freq','freq(readfc,Raman,SaveNM) geom=check')
			freq.write(ramfreq)
		else:
			if line.startswith(' ') == False:
				freq.write(line)
	freq.close()
