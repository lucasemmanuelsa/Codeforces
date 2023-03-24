n1 = int(input())
segmentos = input().split(" ")

lista = []
for i in segmentos:
    lista.append(int(i))

lista = sorted(lista)

status = False
for i in range(len(lista) - 2):

    if(lista[i] + lista[i + 1] > lista[i + 2]):
        status = True

if(status):
    print("YES")
else:
    print("NO")
