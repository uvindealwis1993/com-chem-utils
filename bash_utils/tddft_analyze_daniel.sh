#!/bin/bash
p=$PWD
#cub=${fcfile%/*}/cube_files
#folder=${p##*/}
#File=$(find $PWD -iname "*.fchk" -execdir basename {} .fchk ';')
# Find the tddft.chk files
File=$(find $PWD -iname "tddft.chk")
for i in ${File}; do
    chk=${i##*/}
    dir=${i%/*}
    echo ${dir}
    cd ${dir}
    echo $PWD
    if [[ $(grep -c "Normal termination" ${dir}/opt.log) -gt 0 && $(grep -c "Normal termination" ${dir}/tddft.log) -gt 0 ]]; then
        td=${chk%.chk}
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_exc.txt
        mv spectrum_curve.txt spectrum_curve_XYZ.txt
        mv spectrum_line.txt spectrum_line_XYZ.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_X.txt
        mv spectrum_curve.txt spectrum_curve_X.txt
        mv spectrum_line.txt spectrum_line_X.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_Y.txt
        mv spectrum_curve.txt spectrum_curve_Y.txt
        mv spectrum_line.txt spectrum_line_Y.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_Z.txt
        mv spectrum_curve.txt spectrum_curve_Z.txt
        mv spectrum_line.txt spectrum_line_Z.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_XY.txt
        mv spectrum_curve.txt spectrum_curve_XY.txt
        mv spectrum_line.txt spectrum_line_XY.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_XZ.txt
        mv spectrum_curve.txt spectrum_curve_XZ.txt
        mv spectrum_line.txt spectrum_line_XZ.txt
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_YZ.txt
        mv spectrum_curve.txt spectrum_curve_YZ.txt
        mv spectrum_line.txt spectrum_line_YZ.txt
        tddft_osc_extractor.py
        /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${chk} < ${dir}/exc_state_calc.txt
    elif [[ ! -e "opt.log" ]]; then
        echo "No opt.log file"
        if [[ $(grep -c "Normal termination" ${dir}/tddft.log) -gt 0 ]]; then
            td=${chk%.chk}
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_exc.txt
            mv spectrum_curve.txt spectrum_curve_XYZ.txt
            mv spectrum_line.txt spectrum_line_XYZ.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_X.txt
            mv spectrum_curve.txt spectrum_curve_X.txt
            mv spectrum_line.txt spectrum_line_X.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_Y.txt
            mv spectrum_curve.txt spectrum_curve_Y.txt
            mv spectrum_line.txt spectrum_line_Y.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_Z.txt
            mv spectrum_curve.txt spectrum_curve_Z.txt
            mv spectrum_line.txt spectrum_line_Z.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_XY.txt
            mv spectrum_curve.txt spectrum_curve_XY.txt
            mv spectrum_line.txt spectrum_line_XY.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_XZ.txt
            mv spectrum_curve.txt spectrum_curve_XZ.txt
            mv spectrum_line.txt spectrum_line_XZ.txt
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${td}.log < /home/devored/bin/td_spect_YZ.txt
            mv spectrum_curve.txt spectrum_curve_YZ.txt
            mv spectrum_line.txt spectrum_line_YZ.txt
            tddft_osc_extractor.py
            /data/devored/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${chk} < ${dir}/exc_state_calc.txt
            tddft_trans_nrg_ectractor.py
        else
            echo "TDDFT Did Not Finish Correctly"
        fi
    else
        echo "Opt and TDDFT Did Not Finish Correctly"
    fi
done
