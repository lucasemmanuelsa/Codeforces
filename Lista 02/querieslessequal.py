n = input().split(" ")
a = input().split(" ")
b = input().split(" ")

listaA = []
for i in a:
    listaA.append(int(i))

listaA = sorted(listaA)
listaB = []

index = 0
for j in b:
    listaB.append([int(j), index])
    index+=1

listaB = sorted(listaB)

def iterativo(lista,element,index):
    while(index < len(lista)):
        if(lista[index] <= element):
            index+=1
        else:
            return index
    return index
    

inicio = 0
for i in listaB:
    inicio = iterativo(listaA, i[0], inicio)
    i.append(inicio)

resposta = listaB.copy()
for j in listaB:
    resposta[j[1]] = j[2]

for m in resposta:
    print(m, end=" ")
