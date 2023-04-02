class fila():

    queue = []

    def __init__(self, tamanho):
        self.head = -1
        self.tail = -1
        
    def isEmpty(self):
        return self.head == -1 or self.head > self.tail
    
    def enqueue(self, element):
        if(self.isEmpty()):
            self.head+=1
            self.tail+=1
        else:
            self.tail+=1
        self.queue.append(element)
    
    def dequeue(self):
        if(not self.isEmpty()):
            element = self.queue[self.head]
            self.head += 1
            return element
        
    def cabeca(self):
        if(self.isEmpty()):
            return 'Empty!'
        else:
            return self.queue[self.head]
    
t = int(input())


queue = fila(t)

for i in range(t):
    entrada = input().split(" ")
    if(len(entrada) == 2):
        queue.enqueue(entrada[1])
    elif(entrada[0] == '2'):
        queue.dequeue()
    else:
        print(queue.cabeca())
        
    