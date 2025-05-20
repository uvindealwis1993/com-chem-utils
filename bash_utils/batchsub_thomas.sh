#!/bin/bash

for i in `find $PWD -type d`; do
	cd $i
	/usr/pbs/bin/qsub *.pbs
done

