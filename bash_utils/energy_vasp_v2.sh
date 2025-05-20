#!/bin/bash
#Uvin De Alwis
#the forlder where the file is located
fpath=$(find $PWD -type d -name "scf*")
#go to where the file 
for i in ${fpath}; do
#the path to the file
molpath=${i}
cd ${molpath}
if grep -q "Voluntary" OUTCAR; then
	energy_scf=$(grep "energy(sigma->0)" OUTCAR | tail -n 1 | awk '{print $7}')
	system=$(cat POSCAR | head -n 1)
	echo "$system $energy_scf" 
fi
done

