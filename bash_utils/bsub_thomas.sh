#!/bin/bash

for i in *.pbs; do
	/usr/pbs/bin/qsub *.pbs
done
