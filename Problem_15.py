# Problem 15: Independent Alleles
file = open("/Users/nvolkova/Downloads/rosalind_lia.txt", "r")
k, N = [int(x) for x in next(file).split()]
print(k,N)

from math import factorial as fac
def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

kids = pow(2,k)
pbty = 1 - binomial(kids, N-1) * pow(0.25, N-1) * pow(0.75, kids - N + 1)
print(pbty)

