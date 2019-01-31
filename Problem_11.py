# Problem 11: Mortal Fibonacci Rabbits
file = open("/Users/nvolkova/Downloads/rosalind_fibd.txt", "r")
n, m = [int(x) for x in next(file).split()]
print(n, m)
a1 = 1
a2 = 1
d = 0
curr_fib = [1,1]
for i in range(2,n):
    if i < m:
        curr_fib.append(curr_fib[i-1] + curr_fib[i-2])
    if i == m:
        curr_fib.append(curr_fib[i-1] + curr_fib[i-2] - 1)
    if i > m:
        curr_fib.append(curr_fib[i-1] + curr_fib[i-2] - curr_fib[i - (m+1)])
    print(i+1, curr_fib[i])

