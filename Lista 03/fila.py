class fila():

    

    def __init__(self, queue):
        self.queue = queue

    def isEmpty(self):
        return len(queue)
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if(not self.isEmpty()):
            element = self.queue[0]
            del self.queue[0]
            return element
        
    def head(self):
        if(self.isEmpty()):
            return 'Empty!'
        return self.queue[0]
    
t = int(input())

lista = []
queue = fila(lista)

for i in range(t):
    entrada = list(map(int, input().split(" ")))
    if(len(entrada) == 2):
        fila.enqueue(1)
    elif(entrada[0] == 2):
        fila.dequeue()
    else:
        fila.head()
    