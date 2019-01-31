file = open("/Users/nvolkova/Downloads/rosalind_cons.txt", "r")
import sys
import pandas as pd
import numpy as np
fasta = {}
for line in file:
    line = line.rstrip()
    if line[0]==">":
        name = line[1:]
        fasta[name] = ''
    else:
        fasta[name] = fasta[name] + line
    n = len(fasta[name])
Mat = np.zeros((4,n), dtype = int)
names = ['A','C','G','T']
df = pd.DataFrame(Mat,index = names)
consensus = ''
for i in range(0,n):
    for letter in names:
        for name in fasta.keys():
            if fasta[name][i] == letter:
                df.loc[letter,i] += 1
    consensus += np.argmax(df.iloc[:,i])
print(df)
print(consensus)

df.to_csv("/Users/nvolkova/Downloads/rosalind_res.txt", sep=' ', header = False)
# has to manually add the consensus string and colons after rownames

