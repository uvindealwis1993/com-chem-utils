#!/bin/bash
# Find chk files
chkfile=$(find $PWD -iname "*.chk")
# Go through each cube file
for n in ${chkfile}; do
    chk=${n##*/}
    no_slash=${n#*/}
    no_loc=${no_slash#*/}
    no_me=${no_loc#*/}
    prof_data=${no_me%%/*}
    #echo ${prof_data}
    if [[ ${prof_data} == "Romero" ]]; then
        main_loc=${n##*6-31G/}
        #echo ${main_loc}
        mol=${main_loc%%/*}
        #echo ${mol}
    fi
    if [[ -e "density.cub" ]]; then
        echo "density file made!"
        count="ls -1 *.rgb 2>/dev/null | wc -l"
        if [[ ${count} != 0 ]]; then
            echo "Have Pictures!"
        else
            vmd -dispdev text -startup /data/devored/bin/molec_animation.vmd
        fi
    else
        Multiwfn ${chk} < /data/devored/bin/den_cub.txt
        vmd -dispdev text -startup /data/devored/bin/molec_animation.vmd
    fi
# Convert the figures into a gif
    convert -delay 50 -loop 0 snap.x.*rgb ${mol}_x.gif
    convert -delay 50 -loop 0 snap.y.*rgb ${mol}_y.gif
done 
