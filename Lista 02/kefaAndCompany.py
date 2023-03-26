entrada = input().split(" ")
qntAmigos = int(entrada[0])
d = int(entrada[1])

lista = []

for i in range(qntAmigos):
    dados = input().split(" ")
    dados[0] = int(dados[0])
    dados[1] = int(dados[1])
    lista.append(dados)

lista = sorted(lista)

inicio = 0
fim = 1
maximo = lista[inicio][1]
contador = lista[inicio][1]

while(inicio < len(lista) and fim < len(lista)):
    individual = lista[fim][1]
    if(contador > maximo):
        maximo = contador
    if(individual > maximo):
        maximo = individual
    if(lista[fim][0] - lista[inicio][0] < d):
        contador += lista[fim][1]
        fim+=1
    else:
        contador -= lista[inicio][1]
        if(fim - 1 == inicio):
            contador += lista[fim][1]
            inicio+=1
            fim+=1
        else:
            inicio+=1
        

    if(contador > maximo):
        maximo = contador
    if(individual > maximo):
        maximo = individual

print(maximo)
