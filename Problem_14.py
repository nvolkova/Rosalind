file = open("/Users/nvolkova/Downloads/rosalind_lcsm.txt", "r")
import sys
fasta = {}
for line in file:
    line = line.rstrip()
    if line[0]==">":
        name = line[1:]
        fasta[name] = ''
    else:
        fasta[name] = fasta[name] + line

print('fasta ready')
print(fasta)

# borroed from StackOverflow
def get_longest_common_subseq(data):
    substr = []
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_subseq_of_any(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_subseq_of_any(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if not is_subseq(find, data[i]):
            return False
    return True

# Will also return True if possible_subseq == seq.
def is_subseq(possible_subseq, seq):
    if len(possible_subseq) > len(seq):
        return False
    def get_length_n_slices(n):
        for i in xrange(len(seq) + 1 - n):
            yield seq[i:i+n]
    for slyce in get_length_n_slices(len(possible_subseq)):
        if slyce == possible_subseq:
            return True
    return False

print get_longest_common_subseq([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])

print get_longest_common_subseq(['Oh, hello, my friend.',
                                     'I prefer Jelly Belly beans.',
                                     'When hell freezes over!'])
print(list(fasta.values()))
print(get_longest_common_subseq(list(fasta.values())))

