import heapq
n = int(input())


for i in range(n):
    k = int(input())
    lista = list(map(int, input().split()))
    lista = sorted(lista)
    minhaheap = []
    lista2= []
    for j in range(len(lista)):
        if(lista[j] in lista2):
            heapq.heappush(minhaheap, lista[j])
        else:
            lista2.append(lista[j])
    for k in range(len(minhaheap)):
        lista2.append(heapq.heappop(minhaheap))
    
    lista2 = list(map(str, lista2))
    print(" ".join(lista2))