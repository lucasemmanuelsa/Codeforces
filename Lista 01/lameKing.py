import math
n = int(input())

for i in range(n):

    num = (input()).split(" ")

    lista = []
    for i in num:
        lista.append(abs(int(i)))



    menor = min(lista)
    maior = max(lista)
    qntMov = (menor - 1) * 2

    numeroFinal = maior - (menor - 1)

    qntStops = numeroFinal + (numeroFinal - 1)


    total = qntMov + qntStops

    if(lista[0] == lista[1]):
        total += 1

    print(total)