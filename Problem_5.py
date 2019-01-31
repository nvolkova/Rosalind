# problem 5
file = open("/Users/nvolkova/Downloads/rosalind_gc.txt", "r")
import sys
fasta = {}
for line in file:
    line = line.rstrip()
    if line[0]==">":
        name = line[1:]
        fasta[name] = ''
    else:
        fasta[name] = fasta[name] + line
print(fasta)
contents = {}
for name in fasta.keys():
    contents[name] = (fasta[name].count('G') + fasta[name].count('C')) / len(fasta[name])
max_key = max(fasta, key=lambda k: contents[k])
print(max_key, contents[max_key]*100)

