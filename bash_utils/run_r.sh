#!/bin/bash
#PBS -S /bin/bash
#PBS -l nodes=1:ppn=1

# This script allows the user to execute a R .R file using the Torque batch
# system.

# How to submit this script to batch:  $ qsub -v rProg=myRProgram.R ./run_r.sh

cd $PBS_O_WORKDIR
echo "Current working directory is now: " `pwd`
echo "Starting R job at `date`"

module load R

R --vanilla --args < $rProg

echo "R job run completed at `date`"
