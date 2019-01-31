# Problem 9
file = open("/Users/nvolkova/Downloads/rosalind_subs.txt", "r")
seq = file.readline().rstrip()
mot = file.readline().rstrip()
s = len(seq)
t = len(mot)
print(seq)
print(mot)
i = 0
loc = []
while (i<(s - t + 1)):
    if seq[i:(i+t)] == mot:
        loc.append(i+1)
    i += 1
sloc = [str(a) for a in loc]
print(' '.join(sloc))
