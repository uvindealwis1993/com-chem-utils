#!/bin/bash

find $PWD -name "*.log" | sort -n

for i in `find $PWD -name "*.log" | sort -n`; do
#	grep "SCF Done" $i | tail -n 1 | awk '{ print $5 }'
	grep -A4 "Converged?" $i | tail -n 5
done

