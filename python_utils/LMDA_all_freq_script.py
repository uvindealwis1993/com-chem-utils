#!/usr/bin/python
'''
                                                           
  Overall objective: Find the closest atom from the atom of 
  interest and find the indice of the atom. Create the 
  job.inp file for LModeA using the bond of the atom of 
  interest as the Local Mode that is being studied. 
                                                           
'''
#Open input file for LModeA
LMDA = open('job.inp','w')
#Write the comments in the first line to describe file
LMDA.write('Local Mode Analysis')
#Give new line before the rest of the file
LMDA.write('\n')
LMDA.write('\n $contrl')
LMDA.write('\n   qcprog="gaussian"')
LMDA.write('\n   iprint=1')
LMDA.write('\n   isymm=1')
LMDA.write('\n   iacs=1')
LMDA.write('\n $end\n')
LMDA.write('\n $qcdata')
LMDA.write('\n   fchk="locmode.fchk"')
LMDA.write('\n $end\n')
LMDA.write('\n $LocMod IFRedun=.True. $End\n')
LMDA.close()
