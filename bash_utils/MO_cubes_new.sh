#!/bin/bash
File=$(find $PWD -iname "opt*.chk")
for i in ${File}; do
    dirpath=${i%/*}
    file=${i##*/}
    cd ${dirpath}
    echo $PWD
    /home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${file} < /home/dealwisu/bin/scripts/MO_cube_script.txt
    cp h.cub orb.cub
    vmd -dispdev text -startup /home/dealwisu/bin/scripts/showorb.vmd
    mv full.tga HOMO.tga
    cp l.cub orb.cub
    vmd -dispdev text -startup /home/dealwisu/bin/scripts/showorb.vmd
    mv full.tga LUMO.tga
    rm orb.cub
    mkdir FMO
    mv HOMO_* LUMO_* FMO
done	
