n,m = map(int, input().split())

mod = 1000000007
nomes = []
numeros = []
for i in range(n):
    nomes.append(input())

i = 0
while i < m:
    lista = set()
    for k in nomes:
        lista.add(k[i])
    if(len(lista)>1):
        numeros.append(len(lista))
    i+=1

res = 1
for j in numeros:
    res = (res * j) % mod
print(res)