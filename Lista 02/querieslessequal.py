n = input().split(" ")
a = input().split(" ")
b = input().split(" ")

listaA = []
for i in a:
    listaA.append(int(i))

listaB = []

for j in b:
    listaB.append(int(j))

inicio = 0
fim = len(listaA) - 1
meio = (fim - inicio + 1)//2

while(meio < len()):
#pega o meio, olha pra o elemento da frente e olha pro elemente de tras