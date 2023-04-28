n,m,q = map(int, input().split())
#OBS: o esquema dessa questão é evitar que calcule toda vez todas as linhas da matriz.
matriz = []
def consecutive(lista):
    count = 0
    max = 0
    for i in lista:
        if(i == 1):
            count +=1
            if(count > max):
                max = count
        else:
            if(count > max):
                max = count
            count = 0
    return max
maxi = (0,0)
linha = 0
for i in range(n):
    entrada = list(map(int, input().split())) 
    matriz.append(entrada)
    num = consecutive(entrada)
    
    if(num > maxi[0]):
        maxi = (num,linha)
    linha +=1

for queue in range(q):
    i,j = map(int, input().split())
    matriz[i-1][j-1] = abs(matriz[i-1][j-1] - 1)
    
    
    if i-1 == maxi[1]:
        maxi = (0,0)
        for lin in range(len(matriz)):
            count = consecutive(matriz[lin])
            if(count > maxi[0]):
                maxi = (count,lin)
    else:

        count = consecutive(matriz[i-1])
        if(count > maxi[0]):
            maxi = (count, i-1)
    
    
    print(maxi[0])
