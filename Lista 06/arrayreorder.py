from math import gcd
t = int(input())

for i in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    aux = []
    aux2 = []
    for i in lista:
        if i % 2 == 0:
            aux.append(i)
        else:
            aux2.append(i)
    lista = aux + aux2
    count = 0
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if(gcd(lista[i], 2*lista[j])>1):
                count +=1
    
    print(count)