#!/bin/bash
#ele=$(find $PWD -iname "electron*.cub" -execdir basename {} .cub ';')

# Find all electron cube files
ele=$(find $PWD -iname "electron*.cub")
#echo ${den}
#echo ${den%_*}
#echo ${den#*y}
# Go through each cube file
for n in ${ele}; do
    #echo $n
# Go to the folder where the cube file is located
    fold=${n%/*}
    cd ${fold}
    echo $PWD
# Get the file without the path
    elfile=${n##*/}
# Get the file name without extension
    filnm=${elfile%.cub}
# Get electron and the excited state by itself
    electron=${elfile%_*}
    exc=${filnm#*_}
#    echo ${electron}
#    echo ${exc}
# Find the hole cube files and separate the hole and excited state
    if [[ -e hole_${exc}.cub ]]; then
        hol=hole_${exc}
        holexc=${hol%_*}
        echo ${hol}
    fi	
#    echo ${holexc}
# Rename the files
    cp ${elfile} ${electron}.cub
    cp ${hol}.cub ${holexc}.cub
# Run vmd to produce the figures
    vmd -dispdev text -startup /data/devored/bin/electron_hole_surf.vmd
# Find all the figures made
    immag=$(find $PWD -iname "*.tga" -execdir basename {} .tga ';')
# Rename all the plots with the excited state attached
    for i in ${immag}; do
        uscores=${i//[!_]}
        if [[ ${#uscores} -eq 1 ]]; then
            mv $i.tga ${i}_${exc}.tga
        fi
    done
# Remove the copied files
    rm -r ${electron}.cub
    rm -r ${holexc}.cub
done 
