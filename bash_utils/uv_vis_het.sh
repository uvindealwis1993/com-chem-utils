#!/bin/bash
#Uvin De Alwis
#Execute Multiwfn with folloiwng commands

# Find the tddft.log files
File=$(find $PWD -iname "tddft.log")
for i in ${File}; do
    dir=${i%/*}
    echo ${dir}
    cd ${dir}
    echo $PWD
    if [[ $(grep -c "Normal termination" ${dir}/tddft.log) -gt 0 ]]; then
	/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
	11   
	-3
	0
	20
	101-200
	0
	10
	1
	8
	0.1
	2
EOF
	/home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn tddft.log << EOF
        18
 	15
	y
	0
	q
EOF
	mv spectrum_curve.txt uv_vis.txt
    fi
done



