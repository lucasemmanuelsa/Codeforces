horas = int(input())
list = input().split(" ")

lista = []
for i in list:
    lista.append(int(i))


for k in list:
    lista.append(int(k))

sum = []

sum.append(lista[0])

soma = lista[0]
maior = 0
for j in range(1,len(lista)):
    if(soma + lista[j] == soma):
        soma = 0
    else:
        soma += 1
    sum.append(soma)
    if(soma > maior):
        maior = soma

print(maior)