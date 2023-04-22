import math

t = int(input())

for i in range(t):
    l, r = map(int, input().split())
    quebra = False
    
    for a in range(l, r+1):
        for b in range(a+1, r+1):
            lc = math.lcm(a, b)
            
            if lc >= l and lc <= r:
                print(a, b)
                quebra = True
                break
        
        if quebra:
            break
    
    if not quebra:
        print("-1 -1")
