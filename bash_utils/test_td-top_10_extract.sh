#!/bin/bash
#Uvin De Alwis
p=$PWD
# Find the tddft.chk files
File=$(find $PWD -iname "tddft.chk")
for i in ${File}; do
    chk=${i##*/}
    dir=${i%/*}
    echo ${dir}
    cd ${dir}
    echo $PWD
#    if [[ $(grep -c "Normal termination" ${dir}/opt.log) -gt 0 && $(grep -c "Normal termination" ${dir}/tddft.log) -gt 0 ]]; then
#        td=${chk%.chk}
#        tddft_osc_extractor_top10.py
#	/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${chk} < ${dir}/exc_state_calc.txt
#	   tddft_osc_extractor_top10.py
#     elif [[ ! -e "opt.log" ]]; then
#	     echo "No opt.log file"
      if [[ $(grep -c "Normal termination" ${dir}/tddft.log) -gt 0 ]]; then
            td=${chk%.chk}
            tddft_osc_extractor_top10.py
            /home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${chk} < ${dir}/exc_state_calc.txt
        else
            echo "TDDFT Did Not Finish Correctly"
        fi
done

 


