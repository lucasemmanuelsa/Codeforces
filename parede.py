import math
n = int(input())
raios = input().split(" ")

lista = []

for i in raios:
    lista.append(int(i))

lista = sorted(lista, reverse=True)

listaArea = []

area = 0

for i in range(0, n, 2):
    
    if(i == n-1):
        area += math.pi * lista[i] * lista[i]
    else:
        area += (math.pi * lista[i] * lista[i] - (math.pi * lista[i+1] * lista[i+1])) 

    
print(area)