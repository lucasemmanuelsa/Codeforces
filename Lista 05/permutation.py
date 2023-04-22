import math
n,k = map(int, input().split())

if(n == k):
    print(-1)
elif(k == n - 1):
    resposta = "1"
    for i in range(2,n+1):
        resposta += " " + str(i)
    print(resposta)
elif(k == 0):
    resposta = "1"
    for i in range(n-1):
        resposta += " " + "1"
    print(resposta)
else:
    resposta = "1"
    i = 2
    j = 2
    aux = 1
    while(j <= n):
        if(j == n):
            if(aux == k):
                resposta += " " + "1"
            else:
                resposta += " " + str(n)
        else:
            
            resposta += " " + str(i)
            if(i == k+1):
                i=1
            else:
                i+=1
                aux+=1
        j+=1
    print(resposta)

            
