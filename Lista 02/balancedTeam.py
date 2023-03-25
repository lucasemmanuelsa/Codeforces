n = int(input())
entrada = input().split(" ")


lista = []
for i in entrada:
    lista.append(int(i))

lista = sorted(lista)

inicio = 0
fim = len(lista) - 1

pares = []
for i in range(len(lista) - 1):
    for j in range(i+1, len(lista)):
        if(lista[j] - lista[i] <= 5):
            pares.append([lista[i], lista[j]])


print(pares)
