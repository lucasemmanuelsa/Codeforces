from math import gcd

n = int(input())

for i in range(n):
    k = int(input())
    print(100//gcd(k,100))