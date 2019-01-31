# problem 1
file = open("/Users/nvolkova/Downloads/rosalind_dna.txt", "r")
line = file.read()
print(line.count('A'), line.count('C'), line.count('G'), line.count('T'))

