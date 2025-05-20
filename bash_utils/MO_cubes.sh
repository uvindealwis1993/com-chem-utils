#!/bin/bash
File=$(find $PWD -iname "tddft.chk")
for i in ${File}; do
    dirpath=${i%/*}
    file=${i##*/}
    cd ${dirpath}
    echo $PWD
    /home/dealwisu/bin/Multiwfn_3.8_dev_bin_Linux/Multiwfn ${file} < /home/dealwisu/bin/scripts/MO_cube_script.txt
    cp h.cub orb.cub
    vmd -dispdev text -startup /home/dealwisu/bin/scripts/MO.vmd
    mv MO_xyz0.tga HOMO_xyz0.tga
    mv MO_x90.tga HOMO_x90.tga
    mv MO_y90.tga HOMO_y90.tga
    mv MO_z90.tga HOMO_z90.tga
    mv MO_xy90.tga HOMO_xy90.tga
    mv MO_xz90.tga HOMO_xz90.tga
    mv MO_yz90.tga HOMO_yz90.tga
    mv MO_xyz90.tga HOMO_xyz90.tga
    cp l.cub orb.cub
    vmd -dispdev text -startup /home/dealwisu/bin/scripts/MO.vmd
    mv MO_xyz0.tga LUMO_xyz0.tga
    mv MO_x90.tga LUMO_x90.tga
    mv MO_y90.tga LUMO_y90.tga
    mv MO_z90.tga LUMO_z90.tga
    mv MO_xy90.tga LUMO_xy90.tga
    mv MO_xz90.tga LUMO_xz90.tga
    mv MO_yz90.tga LUMO_yz90.tga
    mv MO_xyz90.tga LUMO_xyz90.tga
    rm orb.cub
    mkdir FMO
    mv HOMO_* LUMO_* FMO
done	
