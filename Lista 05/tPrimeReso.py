n = int(input())

lista = list(map(int, input().split()))

def crivo():
    n = 1000001
    lista = [0]*(n)
    i = 2
    while(i < 1001):
        if(lista[i] == 0):
            j = i*i
            while(j < n):
                lista[j] = 1
                j+=i
        i+=1
    return lista

pre = crivo()
pre[0] = pre[1] = 1
for i in lista:
    raiz = int(i**(1/2))
    if(raiz*raiz == i):
        if(pre[raiz] == 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")