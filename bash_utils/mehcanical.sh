#!/bin/bash
Folder=$(find $PWD -type d -name "strain*")
for i in  ${Folder}; do
	cp run_vasp.pbs ${i}
	cd ${i}
	qsub run_vasp.pbs
done



