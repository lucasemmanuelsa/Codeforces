n = int(input())

lista = list(map(int, input().split()))

maior = max(lista)

def crivoCountDivisors(n):
    
    lista = [2]*(n-1)
    i = 2
    while(i <= n):
        j = i + i
        while(j <= n):
            lista[j-2]+=1
            j+=i
        i+=1
    return lista

divisores = crivoCountDivisors(maior)
for i in lista:
    if(divisores[i-2] == 3):
        print("YES")
    else:
        print("NO")