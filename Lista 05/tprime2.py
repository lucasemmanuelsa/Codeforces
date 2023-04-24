import math
n = int(input())

lista = list(map(int, input().split()))

for i in range(len(lista)):
    count = 0
    raiz = lista[i]**(1/2)
    j = 1
    while(j <= raiz):
        if(lista[i] % j == 0):
            count+=1
            if(j != raiz):
                count+=1
        j+=1
    if(count == 3):
        print("YES")
    else:
        print("NO")
