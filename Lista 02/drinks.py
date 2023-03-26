n = int(input())
entrada = input().split(" ")

lista = []

for i in entrada:
    lista.append(int(i))

total = len(lista)

x = 1
soma = 0
for j in range(len(lista)):
    y = (lista[j] * x) / 100
    soma += y

resultado = soma/total

print(resultado * 100)