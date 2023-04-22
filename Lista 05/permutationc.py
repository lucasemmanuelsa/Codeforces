import math
n,k = map(int, input().split())

if(k >= n):
    print(-1)
elif(k == n - 1):
    resposta = "1"
    for i in range(2,n+1):
        resposta += " " + str(i)
    print(resposta)
else:
    resposta = "2"
    x = n - k
    for i in range(3,x+1):
        resposta += " " + str(i)
    resposta += " " + "1"
    for j in range(x+1, n+1):
        resposta += " " + str(j)
    print(resposta)

            
