# Problem 16: Finding a Protein Motif

file = open("/Users/nvolkova/Downloads/rosalind_mprt.txt", "r")

proteins = []
for line in file:
    line = line.rstrip()
    proteins.append(line)
import urllib2
import sys
locations = {}
for id in proteins:
    url = 'https://www.uniprot.org/uniprot/' + id + '.fasta'
    f = urllib2.urlopen(url)
    fasta=''
    for l in f.readlines():
        l = l.rstrip()
        if l[0]=='>':
            fasta = ''
        else:
            fasta += l
    loc = []
    s = len(fasta)
    i = 0
    while (i<(s - 3)):
        if fasta[i] == 'N' and fasta[i+1] != 'P':
            if fasta[i+2] == 'S' or fasta[i+2] == 'T':
                if fasta[i+3] != 'P':
                    loc.append(i+1)
        i += 1
    sloc = [str(a) for a in loc]
    if len(sloc) > 0:
        locations[id] = ' '.join(sloc)
print(locations)

file2 = open("/Users/nvolkova/Desktop/Git/Rosalind/out.txt", "w")
for id in locations.keys():
    file2.write(id + '\n')
    file2.write(locations[id]+ '\n')

