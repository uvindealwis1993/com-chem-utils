#/usr/local/python/2.7.14/bin/python
import pandas as pd
data = pd.read_csv('ZPE.dat', delim_whitespace=True, names=['count','f','value1','THz','value2','2piTHz','value3','unit','zpe','meV'])
df = pd.DataFrame(data)
df = df.iloc[:-3]
average_ZPE = df['zpe'].astype(float).mean()
print(average_ZPE)
