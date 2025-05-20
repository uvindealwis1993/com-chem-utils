#!/usr/bin/python
'''
Take the tddft_exc.txt file and pull the lambda max,
energy, and excitation.

Daniel Devore, November 23, 2022
'''
excstate = []
oscst = []
seen = set()
top5 = []
sttop5 = []
def find_sec():
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
                oscst.append(exc[5])
with open('tddft.log','r') as tddft:
    tdlines = tddft.readlines()
    find_sec()
#print(excstate)
#print(oscst)
sto = dict(zip(excstate,oscst))
ots = {}
for k, v in sto.items():
    ots[v] = ots.get(v,[]) + [k]
oscst.sort(reverse = True)
oscst_nr = list(dict.fromkeys(oscst))
for x in range(10):
    #print(x)
    top5.append(oscst_nr[x])
    sttop5.append(ots[oscst_nr[x]])
print(top5)
print(sttop5)
lammax = []
nrg = []
exctrans = []
transstate = []
with open('tddft_exc.txt','r') as tdexc:
    exclines = tdexc.readlines()
    for y in exclines:
        if y.startswith(' #'):
            #print(y)
            level = y.split()
            for excl in sttop5:
                if level[1] in excl:
                    #print(y)
                    transstate.append(level[1])
                    nrg.append(level[2])
                    lammax.append(level[4])
                    exctrans.append(exclines[exclines.index(y) + 1].split(','))
#print(nrg)
#print(lammax)
#print(exctrans)
with open('top10_exc_data.txt','w') as ted:
    ted.write(' Transition  Lambda Max    Energy    Oscillator            Orbital\n')
    ted.write('   State        (nm)        (eV)      Strength           Transitions\n')
    for z in exctrans:
        ted.write('    ' + transstate[exctrans.index(z)] + '         ' + lammax[exctrans.index(z)] + '      ' + nrg[exctrans.index(z)] + '      ' + sto[transstate[exctrans.index(z)]] + '       ')
        for ax in z:
            if ax == z[0]:
                ted.write(ax + '\n')
            else:
                ted.write('                                                     ' + ax + '\n')
