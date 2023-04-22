import math

def coprimo(a,b):
    return math.gcd(a,b) == 1

def achar(a,b):
    minimo = min(a,b)
    maximo = max(a,b)
    for i in range(1,maximo+1):
        if(coprimo(minimo,i) and coprimo(i,maximo)):
            return i
        
n = int(input())
lista = list(map(int, input().split()))


aux = str(lista[0])
i = 0
count = 0
if n == 1:
    aux = str(lista[0])
else:
    while(i < n - 1):
        if(not coprimo(lista[i], lista[i+1])):
            if(i == 0):
                aux = aux + " " + str(achar(lista[i], lista[i+1]))
            else:
                aux += " " + str(lista[i])
                aux += " " + str(achar(lista[i], lista[i+1]))
            count +=1
        else:
            if(i == 0):
                aux = aux
            else:
                aux += " " + str(lista[i])
        i+=1
    aux = aux + " " + str(lista[i])
print(count)
print(aux)
