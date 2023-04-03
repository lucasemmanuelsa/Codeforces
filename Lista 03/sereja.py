n = list(map(int, input().split()))
lista = list(map(int, input().split()))

m = n[1]

setlist = set()
resposta = []
for i in range(len(lista)):
    resposta.append(0)
    

i = len(lista) - 1
while(i >= 0):
    setlist.add(lista[i])
    resposta[i] = len(setlist)
    i-=1

for k in range(m):
    index = int(input()) - 1
    print(resposta[index])
    
    