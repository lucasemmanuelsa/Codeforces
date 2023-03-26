n = int(input())
entrada = input().split(" ")

lista = []

for i in entrada:
    lista.append(int(i))


lista = sorted(lista)

print(lista)