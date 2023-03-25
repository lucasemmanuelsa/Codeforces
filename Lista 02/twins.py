n = int(input())
entrada = input().split(" ")

lista = []

for i in entrada:
    lista.append(int(i))

lista = sorted(lista, reverse=True)

for j in range(1, len(lista)):
    lista[j] = lista[j] + lista[j-1]


num = lista[len(lista) - 1] // 2

quantidade = 0
for i in lista:
    if(num >= i):
        quantidade +=1
    else:
        quantidade +=1
        break

print(quantidade)