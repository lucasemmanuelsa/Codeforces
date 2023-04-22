import math

def primo(n):
    
    for i in range(2,int(math.sqrt(n)+2)):
        if(n % i == 0):
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    achou = False
    if(n % 2 == 0):
        a = n//2
        b = n//2
        print(f'{a} {b}')
    else:
        raiz = int(math.sqrt(n))
        for i in range(2, raiz+1):
            if(n % i == 0):
                a = n//i
                b = n - a
                achou = True
                break
        if(not achou):
            a = 1
            b = n - 1
        
        print(f'{a} {b}')