# Problem 7
file = open("/Users/nvolkova/Downloads/rosalind_iprb.txt", "r")
k, m, n = [int(x) for x in next(file).split()]
N = k + m + n
pairs = N*(N-1) / 2
pr = k*(k-1)/2 + k*m + k*n + 0.75 * m*(m-1)/2 + 0.5 * m*n
print(pr / pairs)

