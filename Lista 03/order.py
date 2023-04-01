n = int(input())


while(n != 0):
    lista = list(map(int, input().split(" ")))
    stack = []
    fila = []

    order = sorted(lista)
    
    while(len(lista) > 0):
        
        elemento = lista[0]

        if(len(stack) > 0):
            if(stack[len(stack) - 1] < elemento):
                fila.append(stack.pop())
            else:
                if(len(lista) == 1):
                    fila.append(elemento)
                    del lista[0]
                else:    
                    if(elemento < lista[1]):
                        fila.append(elemento)
                        del lista[0]
                    else:
                        stack.append(elemento)
                        del lista[0]
        else:
            if(len(lista) == 1):
                fila.append(elemento)
                del lista[0]
            else:    
                if(elemento < lista[1]):
                    fila.append(elemento)
                    del lista[0]
                else:
                    stack.append(elemento)
                    del lista[0]

        
    while(len(stack) > 0):
        fila.append(stack.pop())
    
    if(fila == order):
        print("yes")
    else:
        print("no")
    n = int(input())