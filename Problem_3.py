
file = open("/Users/nvolkova/Downloads/rosalind_revc.txt", "r")
line = file.read()
line2 = line[::-1].replace('T', 'U').replace('A', 'T').replace('U', 'A')
file2 = open("/Users/nvolkova/Downloads/out.txt", "w")
file2.write(line2.replace('G', 'U').replace('C', 'G').replace('U', 'C'))

