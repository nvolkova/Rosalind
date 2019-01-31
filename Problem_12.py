# Problem 12: Overlap Graphs
file = open("/Users/nvolkova/Downloads/rosalind_grph.txt", "r")
import sys
fasta = {}
for line in file:
    line = line.rstrip()
    if line[0]==">":
        name = line[1:]
        fasta[name] = ''
    else:
        fasta[name] = fasta[name] + line
edges = []
for name in fasta.keys():
    suff = fasta[name][-3:]
    for name2 in fasta.keys():
        if name != name2:
            pref = fasta[name2][:3]
            if pref == suff:
                edges.append(name + ' ' + name2)
res = open("/Users/nvolkova/Downloads/rosalind_res.txt", 'w')
for item in edges:
    res.write("%s\n" % item)

