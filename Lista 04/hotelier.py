import heapq
n = int(input())
string = input()


lista = [0] * 10
listaHead = [0,1,2,3,4,5,6,7,8,9]
listaTail = [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]

heapq.heapify(listaHead)
heapq.heapify(listaTail)


for a in string:
    if(a == "L"):
        el = heapq.heappop(listaHead)
        lista[el] = 1
        if(-el in listaTail):
            listaTail.remove(-el)
            heapq.heapify(listaTail)
    elif(a == "R"):
        el = heapq.heappop(listaTail)
        lista[-el] = 1
        if(-el in listaHead):
            listaHead.remove(-el)
            heapq.heapify(listaHead)
    else:
        heapq.heappush(listaHead, int(a))
        heapq.heappush(listaTail, -int(a))
        lista[int(a)] = 0

resposta = list(map(str, lista))
print("".join(resposta))
