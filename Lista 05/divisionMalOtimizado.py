import math
n = int(input())

def crivo(n):
    lista = [0]*(n+1)
    count = 0
    while(n > 0):
        i = 2
        while(i < len(lista)):
            if(n % i == 0):
                n-= i
                count +=1
                break
            if(lista[i] == 0):
                j= i + i
                while(j < len(lista)):
                    lista[j] = 1
                    j+=i
            i+=1
    return lista


print(crivo(n))

