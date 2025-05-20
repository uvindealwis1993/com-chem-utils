#!/bin/bash
# Find the tddft.chk files
File=$(find $PWD -iname "top10_exc_data.txt")
for i in ${File}; do
    txtfile=${i##*/}
    dir=${i%/*}
    cd ${dir}
    #echo ${txtfile}
    excited_state_parameters_top10.py
    Multiwfn tddft.chk < short_exc_10_param.txt |tee log.txt
    grep "Sr index" ./log.txt |nl >> result_top10.txt;echo >> result_top10.txt
    grep "D index" ./log.txt |nl >> result_top10.txt;echo >> result_top10.txt
    grep "RMSD of hole in" ./log.txt |nl >> result_top10.txt;echo >> result_top10.txt
    grep "RMSD of electron in" ./log.txt |nl >> result_top10.txt;echo >> result_top10.txt
    grep "H index" ./log.txt |nl >> result_top10.txt;echo >> result_top10.txt
    grep "t index" ./log.txt |nl >> result_top10.txt
    rm -r log.txt
done
