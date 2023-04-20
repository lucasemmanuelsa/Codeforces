import math
n = 45
a = n//2
b = n//2 +1

while(a + b == n and a > 0):
    lcm= a*b / math.gcd(a,b)
    print(a,b, lcm)
    a-=1
    b+=1