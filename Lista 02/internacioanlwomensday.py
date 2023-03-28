entrada = input().split(" ")
lista = input().split(" ")

n = int(entrada[0])
k = int(entrada[1])

doces = []
for i in lista:
    doces.append(int(i))

for l in range(len(doces)):
    doces[l] = doces[l] % k
    
contagem = []
for i in range(k):
    contagem.append(0)

for j in doces:
    contagem[j] += 1

soma = 0
i = 0
j = len(contagem) - 1
while(i <= j):
    if(i == 0 or i == j):
        soma += contagem[i] // 2
    else:
        minimo = min(contagem[i], contagem[j])
        soma += minimo
        j-=1
    i+=1

soma = soma * 2

print(soma)
