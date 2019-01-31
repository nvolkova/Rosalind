# problem 4
file = open("/Users/nvolkova/Downloads/rosalind_fib.txt", "r")
n, k = [int(x) for x in next(file).split()]
a1 = 1
a2 = 1
for i in range(3,(n+1)):
   a = k*a1 + a2;
   a1 = a2;
   a2 = a;
   print(i,a);

