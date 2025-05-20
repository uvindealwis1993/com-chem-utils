#!/usr/bin/python
'''
Daniel Devore

Convert opt.com to freq.com input files
'''
#Initialize system with wanted input file
import sys
if len(sys.argv) < 2:
#Print error if file is not given
	print "\nError: Expecting Argument. Please Specify OPT Input File\n"
else:
#Else open the opt file in read mode
	opt = open("opt.gjf","r")
#Assign elements to a variable
data = ""
#Use for loop to go through line by line
for line in opt:
#replace keyword for opt for the freq keyword
	fr = line.replace("opt(tight)","freq(SaveNM) geom=check guess=read")
#Concatenate old and new data
	data = data + fr
#Close the file
opt.close()
#Open freq input file in write mode
freq = open("freq.gjf","w")
#Write the changed data into freq file
freq.write(data)
freq.write("\n")
#Close file
freq.close()
#Open freq file in read mode
freq = open("freq.gjf","r")
#Assign lines to a variable
lines = freq.readlines()
#Close file
freq.close()
#Open freq file in write mode
freq_new = open("freq.gjf","w")
#Use for loop to go through line by line
for line in lines:
#If the line does not start with a space then write the line in the freq file
    if not line.startswith(' '):
        freq_new.write(line)
#Close file
freq_new.close()

