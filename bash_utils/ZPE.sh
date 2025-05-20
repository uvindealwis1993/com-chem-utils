#!/bin/bash

grep THz OUTCAR > ZPE.dat
python2.7 ZPE.py 

