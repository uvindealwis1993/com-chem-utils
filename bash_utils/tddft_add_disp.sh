#!/bin/bash
#######################################################################
#                                                                     #
# Find tddft folder add dispersion and run calc                       #
#                                                                     #
#     								      #
# Daniel Devore                                                       #
#                                                                     #
#######################################################################
#Find fchk files and take only the name of the file
#Filename=$(find $PWD -iname "opt.com" -execdir basename {} .fchk ';')
#Finds fchk file and where the file is located
File=$(find $PWD -type d -iname "M06-2X")
#Runs for loop to go through each fchk file individually
for i in ${File}; do
#Variables relevant for when going through each input file individually
#Go to folder with input file
    cd ${File}
# Print working directory
    echo $PWD
    cd B3LYP
    echo $PWD
    if [[ -e "dispersion" ]]; then
        echo "dispersion calc exists"
    else
        mkdir dispersion
        cp tddft.gjf dispersion
        cp g16.pbs dispersion
        molchk=$(find $PWD -iname "*.chk" -execdir basename {} .chk ';')
        for n in ${molchk}; do
            if [[ ${n} != "tddft" ]]; then
                cp ${n}.chk dispersion
            fi
        done
        cd dispersion
        echo $PWD
        emp_disp_tddft.py
        echo "Dispersion added: Submitting Job"
        qsub g16.pbs
    fi
    cd ${File}
    cd BP86
    echo $PWD
    if [[ -e "dispersion" ]]; then
        echo "dispersion calc exists"
    else
        mkdir dispersion
        cp tddft.gjf dispersion
        cp g16.pbs dispersion
        molchk=$(find $PWD -iname "*.chk" -execdir basename {} .chk ';')
        for n in ${molchk}; do
            if [[ ${n} != "tddft" ]]; then
                cp ${n}.chk dispersion
            fi
        done
        cd dispersion
        echo $PWD
        emp_disp_tddft.py
        echo "Dispersion added: Submitting Job"
        qsub g16.pbs
    fi
done

