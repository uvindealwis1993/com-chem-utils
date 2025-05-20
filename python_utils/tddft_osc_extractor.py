#!/usr/bin/python
'''
Get the oscillator strength and the electric dipole moments
from the tddft.log file. Rank the oscillator strengths
from largest to smallest.

Daniel Devore November 21, 2022
'''
excstate = []
oscst = []
transdip = []
seen = set()
top5 = []
sttop5 = []
with open("tddft.log","r") as tddft:
    tdlines = tddft.readlines()
    for n in tdlines:
        if 'Ground to excited state transition electric dipole moments' in n:
            transdm = tdlines.index(n)
            tedm = n
        if 'Ground to excited state transition velocity dipole moments' in n:
            transvdm = tdlines.index(n)
            tvdm = n
            break
    for m in tdlines:
        if transvdm > tdlines.index(m) > transdm + 1:
            if m not in seen:
                #print(m)
                seen.add(m)
                exc = m.split()
                excstate.append(exc[0])
                transdip.append([exc[1],exc[2],exc[3]])
                oscst.append(exc[5])
#for x in excstate:
    #print(x + '  ' + oscst[excstate.index(x)])
sto = dict(zip(excstate,oscst))
exstdip = dict(zip(excstate,transdip))
#print(exstdip)
#print(sto)
#print(len(sto))
with open('esc_dip.txt','w') as exd:
    exd.write('Excited              Transition\n State                 Dipole\n')
    for ex in excstate:
        exd.write('  ' + ex + '      ' + str(exstdip[ex]) +'\n')
#for y in excstate:
    #print(y + '  ' + sto[y])
ots = {}
for k, v in sto.items():
    ots[v] = ots.get(v,[]) + [k]
#print(ots)
oscst.sort(reverse = True)
oscst_nr = list(dict.fromkeys(oscst))
#print(oscst_nr)
for x in range(5):
    #print(x)
    top5.append(oscst_nr[x])
    sttop5.append(ots[oscst_nr[x]])
print(top5)
print(sttop5)
with open('exc_state_calc.txt','w') as excalc:
    excalc.write('18\n1\ntddft.log\n')
    for y in sttop5:
    #print(len(y))
    #print(range(len(y)))
        if len(y) == 1:
            #print(y[0])
            excalc.write(y[0])
            if y == sttop5[0]:
                excalc.write('\n-1\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n1\n')
            elif y == sttop5[len(sttop5) - 1]:
                excalc.write('\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n')
            else:
                excalc.write('\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n1\n')
        elif len(y) > 1:
        #print(len(y))
            for z in range(len(y)):
                #print(y[z])
                excalc.write(y[z])
                if y == sttop5[0]:
                    excalc.write('\n-1\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n1\n')
                elif y == sttop5[len(sttop5) - 1]:
                    excalc.write('\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n')
                else:
                    excalc.write('\n1\n2\n-1\n10\n1\n11\n1\n12\n2\n13\n14\n4\n15\n16\n17\n4\n0\n0\n1\n')
    excalc.write('0\nq')
