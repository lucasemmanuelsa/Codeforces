entrada = input().split(" ")
lista = input().split(" ")

nBolas = int(entrada[0])
nCores = int(entrada[1])
cor = int(entrada[2])

linha = []
for i in lista:
    linha.append(int(i))

j = 0
while(i < len(linha)):
    if(linha[i] == cor):
        sequencia = 1
        
