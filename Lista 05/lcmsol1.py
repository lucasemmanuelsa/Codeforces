import math
def primo(n):
    
    for i in range(2,int(math.sqrt(n)+2)):
        if(n % i == 0):
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    
    if(n % 2 == 0):
        a = n//2
        b = n//2
        print(f'{a} {b}')
    else:
        a = n//2
        b = (n//2) + 1
        while(a+b == n and a > 0):
            if(b % a == 0):
                print(f'{a} {b}')
                break
            a-=1
            b+=1