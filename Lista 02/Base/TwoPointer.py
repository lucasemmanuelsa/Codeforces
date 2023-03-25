n = int(input())
lista = input().split(" ")

entrada = []
for i in lista:
    entrada.append(int(i))
def twoPointer(lista, target):
    start = 0
    end = len(lista) - 1
    resultado = [-1, -1]

    while(start < resultado):
        sum = lista[start] + lista[end]

        if(sum == target):
            resultado[0] = start + 1
            resultado[1] = end + 1
            break
        elif(sum < target):
            start+=1
        else:
            end-=1
    
    return resultado

#O(n)