#!/usr/bin/python
'''
vibout.py version 2.0
Thomas L. Ellington
May 25, 2017

VIBOUT utility designed for easy extraction of vibrational frequencies,
IR intensities, Raman activities, reduced masses of the displacement, and
force constants of each mode.
'''
#Initializes the specified output file for reading. Error flag is called if the user does not provide argument.
import sys
if len(sys.argv) < 2:
        print("\nERROR: EXPECTING ARGUMENT. PLEASE SPECIFY FREQUENCY OUTPUT FILE!\n")
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
#Being parsing the specified output file. Determines 1. Point group, 2. number of atoms, and 3. degrees of freedom
#Using the above information, extract, format, and store 1. Frequencies, 2. IR intensities, 3. Raman activites,
#4. Reduced masses, and 5. Force constants.
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
header = '\n     Freq.(1/cm)   IR-int.(km/Mol)  Ram.-act.(A^4/amu)      Red.-mass(amu)  Force-con.(mDyne/A)'
print('\nPARSING SPECIFIED FREQUENCY OUTPUT FILE!')
print(header)
#Deliminate and format stored information (including Raman activites)
if len(ralist) != 0:
        ziplist=zip(freqlist,irlist,ralist,redmaslist,fconlist)
        for i in ziplist:
                #print >> outfile, '%12.4f%12.4f%12.4f' %(i[0], i[1], i[2])
                print('%12.0f   %12.1f    %12.1f            %12.2f      %12.3f' %(i[0], i[1], i[2], i[3], i[4]))
#Deliminate and format stored information (excluding Raman activites)
else:
        ziplist=zip(freqlist,irlist,redmaslist,fconlist)
        for i in ziplist:
                #print >> outfile, '%12.4f%12.4f' %(i[0], i[1])
                print('%12.4f%12.4f%12.4f%12.4f' %(i[0], i[1], i[2], i[3]))
print('\nPARSING OF FREQUENCY OUTPUT FILE COMPLETE!\n')
#Close the specified output file to prevent creation of swap file
freqfile.close()
