n = int(input())
entrada = input().split(" ")


lista = []
for i in entrada:
    lista.append(int(i))
lista = sorted(lista)


inicio = 0
numero = 0
fim = 1
nPessoas = 1
maior = 1
while(inicio < len(lista) and fim < len(lista)):
    
    if(abs(lista[inicio] - lista[fim]) <= 5):
        nPessoas = abs(fim - inicio) + 1
        fim+=1
    else:
        inicio+=1
        fim+=1
        
    if(nPessoas > maior):
        maior = nPessoas
        
print(nPessoas)
