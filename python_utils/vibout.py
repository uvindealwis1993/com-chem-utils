#!/usr/bin/python
'''
vibout.py version 1.1
Dr. Thomas L. Ellington
Feb. 20, 2020

VIBOUT utility designed for easy extraction of vibrational frequencies,
IR intensities, Raman activities, reduced masses of the displacement, and
force constants of each mode.

Changelog:
  v. 1.1:
	i. header formatting has been adjusted to reflect the type of 
	   calculation (IR vs Raman) specified in the Gaussian input stream
'''
#Initializes the specified output file for reading. Error flag is called if 
#the user does not provide argument.
import sys
if len(sys.argv) < 2:
        print "\nERROR: EXPECTING ARGUMENT. PLEASE SPECIFY FREQUENCY OUTPUT FILE!\n"
        exit()
else:
        freqfile = open(sys.argv[1],'r')
#Container initialization: Lists that hold all required information.
freqlist = []
irlist = []
ralist = []
redmaslist = []
fconlist = []
pg = []
numfreq = []
#Being parsing the specified output file. Determines 1. Point group, 2. number 
#of atoms, and 3. degrees of freedom
#Using the above information, extract, format, and store 1. Frequencies, 
#2. IR intensities, 3. Raman activites, #4. Reduced masses, and 5. Force 
#constants.
ractprint = 0
for line in freqfile:
        if 'Full point group' in line:
                pglist = line.split()
                pg.append(pglist[3])
        if 'NAtoms=' in line:
                alist = line.split()
                natoms = int(alist[1])
                if pg[0] == 'D*H' or 'C*V':
                        dog = (3*natoms)-5
                        numfreq.append(dog)
                else:
                        dog = (3*natoms)-6
                        numfreq.append(dog)
        if 'Frequencies' in line:
                flist = line.split()
                freqlist.append(float(flist[2]))
                if len(freqlist) != numfreq[0]:
                        freqlist.append(float(flist[3]))
                if len(freqlist) != numfreq[0]:
                        freqlist.append(float(flist[4]))
        if 'IR Inten' in line:
                ilist = line.split()
                irlist.append(float(ilist[3]))
                if len(irlist) != numfreq[0]:
                        irlist.append(float(ilist[4]))
                if len(irlist) != numfreq[0]:
                        irlist.append(float(ilist[5]))
        if 'Raman Activ' in line:
                ractprint = 1
		rlist = line.split()
                ralist.append(float(rlist[3]))
                if len(ralist) != numfreq[0]:
                        ralist.append(float(rlist[4]))
                if len(ralist) != numfreq[0]:
                        ralist.append(float(rlist[5]))
        if 'Red. masses' in line:
                redlist = line.split()
                redmaslist.append(float(redlist[3]))
                if len(redmaslist) != numfreq[0]:
                        redmaslist.append(float(redlist[4]))
                if len(redmaslist) != numfreq[0]:
                        redmaslist.append(float(redlist[5]))
        if 'Frc consts' in line:
                forclist = line.split()
                fconlist.append(float(forclist[3]))
                if len(fconlist) != numfreq[0]:
                        fconlist.append(float(forclist[4]))
                if len(fconlist) != numfreq[0]:
                        fconlist.append(float(forclist[5]))
#Begin formatting and print the extracted information
#Column headings with units
hline1 =  '	-----------------------------------------------------'
hline2 =  '	---------------------------------------------------------------------'
if ractprint == 0:
	print '\n	PARSING SPECIFIED FREQUENCY OUTPUT FILE FOR:'
	print '	   Frequency      (in 1/cm)'
	print '	   IR Intensity   (in km/Mol)'
	print '	   Reduced Mass   (in amu)'
	print '	   Force Constant (mDyne/A)'
	header1 = '\n	Frequency  IR-intensity  Reduced-mass  Force-constant'
	print header1
	print hline1
if ractprint == 1:
	print '\n	PARSING SPECIFIED FREQUENCY OUTPUT FILE FOR:'
	print '  Frequency      (in 1/cm)'
	print '  IR Intensity   (in km/Mol)'
	print '  Raman Activity (in A^4/amu)'
	print '  Reduced Mass   (in amu)'
	print '  Force Constant (mDyne/A)'
	header2 = '\n	Frequency  IR-intensity  Raman-activity  Reduced-mass  Force-constant'
	print header2
	print hline2
#Deliminate and format stored information (including Raman activites)
if len(ralist) != 0:
        ziplist=zip(freqlist,irlist,ralist,redmaslist,fconlist)
        for i in ziplist:
		print '  %12.0f %12.1f   %12.1f    %12.3f   %12.3f' %(i[0], i[1], i[2], i[3], i[4])
#Deliminate and format stored information (excluding Raman activites)
else:
        ziplist=zip(freqlist,irlist,redmaslist,fconlist)
        for i in ziplist:
                print '  %12.0f %12.1f   %12.3f   %12.3f' %(i[0], i[1], i[2], i[3])
if ractprint == 0:
	print hline1
else:
	print hline2
print '\n	PARSING OF FREQUENCY OUTPUT FILE COMPLETE!\n'
#Close the specified output file to prevent creation of swap file
freqfile.close()
