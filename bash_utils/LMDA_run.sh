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
#Finds fchk file and where the file is located
File=$(find $PWD -iname "locmode.fchk")
#Runs for loop to go through each fchk file individually
for i in ${File}; do
#Variables relevant for when going through each fchk file individually
	fchk=${i##*/}
	fn=${fchk%.fchk}
	locmoddir=${i%/*}
	moldir=${locmoddir%/*}
	if [[ ${locmoddir##*/} == 'LModeA' ]]; then
		#echo ${locmoddir##*/}
		#echo ${moldir}
#Go to the LMode folder
		cd ${locmoddir}
		#echo $PWD
#Copy opt.log file to LModeA folder
		cp ${moldir}/freq.log ${locmoddir}
		#ls
#Run LMDA_script.py script
		LMDA_script.py
		#ls
#Run the LModeA
		/home/ellingtont/bin/qc/bin/lmodea.exe -b < job.inp > job.out
		mkdir All_local_mode
		cp ${fchk} All_local_mode
		cd All_local_mode
		LMDA_all_freq_script.py
		/home/ellingtont/bin/qc/bin/lmodea.exe -b < job.inp > job.out
	fi	
done

