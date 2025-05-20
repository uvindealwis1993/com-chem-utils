#!/usr/bin/python
'''
Get the excited states from the top5 file and make a nex txt file for each state
to get the CT contributions from Multiwfn

Daniel Devore February 1, 2023
'''
exc = []
with open('top5_exc_data.txt') as top5:
    for n in top5:
        ln = n.split()
        #print(ln)
        try:
            exc.append(int(ln[0]))
        except ValueError:
            continue
        except IndexError:
            continue
print(exc)
for m in exc:
    #print(f"MO_state_{m}_run")
    #print(f"18\n1\ntddft.log\n{m}\n3\n2\n3\n7\n2\n3\n0\n0\n0\nq")
    with open(f"CT_state_{m}_run.txt","w") as mo:
        mo.write(f"18\n4\ntddft.log\n{m}\ny\n-1\n8\n2\n{m}\n-1\n0\nq")
