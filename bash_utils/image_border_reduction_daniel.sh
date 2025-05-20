#!/usr/bin/bash
######################################
#                                    #
# Find each .tga file and trim       #
# borders                            #
#                                    #
# Daniel Devore, February 14, 2023   #
######################################

# First find all .tga files
tga=$(find $PWD -iname "*.tga")

# Go through each file
for i in ${tga}; do
    # Do to the directory the tga file is in
    # and find the file name
    tgafold=${i%/*}
    image=${i##*/}
    #echo ${tgafold}
    #echo ${image}
    cd ${tgafold}
    echo $PWD
    echo ${image}
    # Trim the borders of the file
    convert -trim -define trim:percent-background=0% ${image} ${image}
    echo "${image} borders reduced"
done
