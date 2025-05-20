#!/bin/bash
#PBS -m abe -M <Put your email address here.  Without the angle brackets>
#PBS -N <Put Job Name Here.  Without the angle brackets>
#PBS -l nodes=1:ppn=1
#PBS -kode

PYTHONPROG=<Put python program name here.  Without the angle brackets>  #Use full path.  For example: PYTHONPROG="/data/bob/myProg.py"

cd $PBS_O_WORKDIR
module load python/3.7.0
python  $PYTHONPROG
