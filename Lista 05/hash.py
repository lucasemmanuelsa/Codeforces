import math
n = int(input())

def hash(a,b):
    return a*a + 2*a*b + a + 1

x = 1
y = int((n-1)/(2*x) - (1/2) - (x/2))

menor = 0

for i in range(1,int(math.sqrt(n)+1)):
    x = i
    if(hash(x,y) == n):
        menor = x
        break
if(y <= 0):
    menor = 0
if(menor !=0):
    print(menor, y)
else:
    print("NO")
