#!/bin/bash
#######################################################################
#                                                                     #
# Find tddft.chk files, make the IOp change to tddft.gjf file,        #
# edit the pbs script, and submit the tddft job                       #
#     								      #
# Daniel Devore                                                       #
#                                                                     #
#######################################################################
#Find fchk files and take only the name of the file
Filename=$(find $PWD -iname "*.fchk" -execdir basename {} .fchk ';')
#Finds fchk file and where the file is located
File=$(find $PWD -iname "*tddft.chk")
#Runs for loop to go through each fchk file individually
for i in ${File}; do
#Variables relevant for when going through each fchk file individually
	tchk=${i##*/}
	fn=${tchk%.chk}
	moldir=${i%/*}
#Go to the dir where tddft.chk file is located
	cd ${moldir}
	tddft_IOp.py
	tddft_pbs_run.py
	qsub g16.pbs
done

