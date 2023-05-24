from queue import Queue
n = int(input())

visitado = []

listAdj = []

dist = []
for i in range(n):
    adj = list(map(int, input().split()))
    listAdj.append(adj)
    visitado.append(False)
    dist.append(-1)

print(listAdj)
def bfs(u):
    fila = Queue()
    fila.put(u)
    concatena = ""
    while(not fila.empty()):
        v = fila.get()
        visitado[v] = True
        concatena += f'{v} '
        for vertex in listAdj[v]:
            if(not visitado[vertex]):
                fila.put(vertex)
    return concatena

def dfs(u):
    pilha = []
    pilha.append(u)
    concatena = ""
    while(not (len(pilha) == 0)):
        v = pilha.pop()
        visitado[u] = True
        concatena += f'{v} '
        for vertex in listAdj[v]:
            if(not visitado[vertex]):
                pilha.append(vertex)
    return concatena

def bfsDist(u):
    fila = Queue()
    fila.put(u)
    concatena = ""
    dist[u] = 0
    while(not fila.empty()):
        v = fila.get()
        
        concatena += f'{v} '
        for vertex in listAdj[v]:
            if(dist[vertex] == -1):
                dist[vertex] = dist[v] + 1
                fila.put(vertex)
    return concatena


#print(dfs(0))
#print(bfs(0))
print(bfsDist(0))
print(dist)