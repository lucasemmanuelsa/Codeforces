import heapq
n = int(input())
string = input()


lista = [0] * 10
listaHead = [0,1,2,3,4,5,6,7,8,9]
listaTail = [-0,-1,-2,-3,-4,-5,-6,-7,-8,-9]

for a in string:
    
    if(a == "L"):
        lista[heapq.heappop(listaHead)] = 1
    elif(a == "R"):
        lista[-heapq.heappop(listaTail)] = 1
    else:
        heapq.heappush(listaHead, int(a))
        heapq.heappush(listaTail, -int(a))
        lista[int(a)] = 0

resposta = list(map(str, lista))
print("".join(resposta))
