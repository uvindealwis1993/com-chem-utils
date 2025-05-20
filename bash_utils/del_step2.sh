#!/bin/bash
#Uvin De Alwis
#the forlder where the file is located
File=$(find $PWD -type d -name "step2")
#go to where the file 
for i in ${File}; do
#the path to the file
molpath=${i%/*}
cd ${molpath}
rm -rf step2
done
