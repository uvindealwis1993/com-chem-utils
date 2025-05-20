#!/bin/bash

grep -A 10000 'GIN' $1 | paste -s | sed -e 's/[ \t]//g;s/\\/\n/g;s/,0,/ /g;s/,/ /g' | sed -n '/#/,/PG/p'

