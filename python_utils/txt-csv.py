#!/usr/bin/python
# Import libraries
import os
import csv
import glob

# Find all curveall txt files
txtfiles = glob.glob('curveall*.txt')
#print(txtfiles)

# Put all data in files in a list
for a in txtfiles:
    
    testdata = []
    # Get just the name of the file
    txtname = a.split('.')[0]
    
    with open(a) as file:
        filelines = file.readlines()
        for aa in filelines:
            testdata.append(aa.replace('-','E-'))
            
    txtdata = [cc.replace('EE','E').split() for cc in testdata]
    
    # Write data to csv files
    with open(f"{txtname}.csv",'w') as csvfile:
        csvwrite = csv.writer(csvfile)
        csvwrite.writerows(txtdata)
