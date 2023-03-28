n = int(input())
entrada = input().split(" ")

lista = []

for i in entrada:
    lista.append(int(i))

for j in range(1,len(lista)):
    lista[j] = lista[j] + lista[j - 1]



count = 0
for k in range(len(lista) - 1):
    esquerda = lista[k]
    direita = lista[len(lista) - 1] - esquerda
    if(esquerda == direita):
        count+=1

print(count)