#!/usr/bin/python
'''
Get the excited states from the top10 file and make a new txt file
to get excited state parameters from Multiwfn

Daniel Devore February 6, 2023
'''
exc = []
with open('top10_exc_data.txt') as top5:
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
with open('short_exc_10_param.txt','w') as sep:
    sep.write('18\n1\ntddft.log\n')
    for m in exc:
        sep.write(f"{m}\n1\n3\n0\n0\n")
        if exc.index(m) < len(exc) - 1:
            sep.write("1\n")
        else:
            sep.write("0\nq")
