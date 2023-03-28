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

def binarySearch(inicio, final, lista, element):
    meio = inicio + (final - inicio)// 2
    if(inicio > final):
        return meio
    if(element == listaA[meio]):
        return meio
    if(element < lista[meio]):
        if(element < lista[meio - 1]):
            return binarySearch(inicio, meio - 1, lista, element)
        else:
            return meio - 1
    else:
        return binarySearch(meio + 1, final, lista, element)

def binarySearchIterativo(inicio, final, lista, element):
    while(inicio <= final):
        meio = inicio + (final - inicio)//2
        if(element == lista[meio]):
            return meio
        elif(element < lista[meio]):
            if(element < lista[meio - 1]):
                return meio -1
            final = meio - 1
        else:
            inicio = meio + 1
    return meio

for i in listaB:
    inicio = binarySearchIterativo(0, len(listaA) - 1, listaA, i[0])
    print(inicio + 1, end=" ")
'''
for i in listaB:
    print(binarySearch(0, len(listaA) - 1, listaA, i) + 1, end=" ")'''