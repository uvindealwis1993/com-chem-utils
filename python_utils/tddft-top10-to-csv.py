#!/usr/bin/python
'''
Get results from top5_exc_data.txt and result.txt and put
them in a csv file

Daniel Devore February 8, 2023
'''
import csv

# Initialize lists
Srind = []
Dind = []
Hind = []
tind = []
sighl = []
sigel = []
with open('top10_exc_data.txt') as top5:
    # Extract the excited state, lambda max, oscillator strength,
    # and excitation energy
    t5dat = top5.readlines()

with open('result_top10.txt') as res:
    rdat = res.readlines()

# Copy the top5 file in another list and delete the first 2 lines to
# only get the data needed
numonly = [t5dat[lin] for lin in range(2,len(t5dat)) if len(t5dat[lin]) > 1]
#print(numonly)

# Get only the Sr index, D index, HCT, and H index
noind = rdat.copy()
for a in noind:
    alist = a.split()
    #print(alist)
    if 'Sr' in a:
        del alist[0]
        for b in alist:
            try:
                Srind.append(float(b))
            except ValueError:
                continue
            except IndexError:
                continue
    elif 'D index' in a:
        Dind.append(float(alist[alist.index('index:') + 1]))
    elif 'RMSD of hole' in a:
        sighl.append(float(alist[alist.index('Norm:') + 1]))
    elif 'RMSD of electron' in a:
        sigel.append(float(alist[alist.index('Norm:') + 1]))
    elif 'H index' in a:
        Hind.append(float(alist[alist.index('index:') + 1]))
    elif 't index' in a:
        tind.append(float(alist[alist.index('index:') + 1]))
#print(Srind,Dind,HCT,Hind,tind)

# Get only the state, lambda max, nrg, and oscillator strength in a list
data = [[val.split()[0],val.split()[1],round(float(val.split()[2]),3),round(float(val.split()[3]),3)] for val in numonly 
        if val.split()[0].startswith('H') == False]
#print(data)
# Put Srind, Dind, HCT, Hind, and tind in a single list
indices = [[round(Srind[indx],3),round(Dind[indx],3),round(Hind[indx],3),round(tind[indx],3),round(abs(sigel[indx]) - abs(sighl[indx]),3)] 
    for indx, vlu in enumerate(Srind)]
#print(indices)
# Add the Srind, Dind, HCT, Hind, and tind in the data list
for ind, vl in enumerate(data):
    data[ind].extend(indices[ind])
#print(data)

molecule = input('What molecule or complex is used?')
label = ['','','','',molecule,'','','','']
#print(label)

with open('XB_comp_TDDFT_top10_data.csv','w') as mol:
    csvwriter = csv.writer(mol)
    csvwriter.writerow(label)
    csvwriter.writerows(data)
