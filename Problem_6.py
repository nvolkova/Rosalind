# Problem 6
file = open("/Users/nvolkova/Downloads/rosalind_hamm.txt", "r")
line1 = file.readline()
line2 = file.readline()
def hamming(l1, l2):
    dist = 0;
    for i in range(0, len(l1)-1):
        if l1[i] != l2[i]:
            dist += 1;
    return dist
print(hamming(line1, line2));
