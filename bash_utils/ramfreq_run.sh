#!/bin/bash
#######################################################################
#                                                                     #
# Find fchk files, rerun the freq calcs to savenm, mv new fchk file   #
# to new folder for LMDA, and run LModeA on molecule                  #
#     								      #
# Daniel Devore                                                       #
#                                                                     #
#######################################################################
#Find fchk files and take only the name of the file
Filename=$(find $PWD -iname "*.fchk" -execdir basename {} .fchk ';')
#Finds opt.chk file and where the file is located
File=$(find $PWD -iname "opt.chk")
#Runs for loop to go through each chk file individually
for i in ${File}; do
#Variables relevant for when going through each chk file individually
	optchk=${i##*/}
	fn=${optchk%.chk}
	moldir=${i%/*}
	#echo ${locmoddir##*/}
	#echo ${moldir}
	if [[ ! -d 'ram_freq' ]]; then
#Go to the folder with the opt.chk file
		cd ${moldir}
#make a folder for the freq calc
		#echo $PWD
		mkdir ram_freq
#copy opt.chk and opt.gjf file and g16.pbs file to new folder
		cp ${fn}.gjf ram_freq
		cp ${optchk} ram_freq
		cd ram_freq
		cp /home/devored/g16.pbs ${moldir}/ram_freq
#run optfreq script to run raman freq calc and save nm
		opt_to_ramanfreq.py opt.gjf
#Submit the raman freq calc
		qsub g16.pbs
	fi
done

