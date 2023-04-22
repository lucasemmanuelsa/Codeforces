n = int(input())

def crivo(n):
    lista = [0]*(n-1)
    i=2
    count = 0
    while(i <= n):
        if(lista[i-2] == 0):
            j = i
            count+=1
            while(j <= n):
                if(lista[j-2] == 0):
                    lista[j-2] = count
                j+=i
        i+=1
    return lista

print(" ".join(map(str,crivo(n))))
    
