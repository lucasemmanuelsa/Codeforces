n = int(input())


tv1 = []
tv2 = []

sentinela = False

pares = []
for i in range(n):
    par = list(map(int, input().split(" ")))
    pares.append(par)

pares = sorted(pares)
for i in range(n):
    if(not tv1):
        tv1.append(pares[i])
    else:
        ultimo = tv1[len(tv1) - 1]
        if(pares[i][0] > ultimo[1]):
            tv1.append(pares[i])
        else:
            if(not tv2):
                tv2.append(pares[i])
            else:
                ultimo = tv2[len(tv2) - 1]
                if(pares[i][0] > ultimo[1]):
                    tv2.append(pares[i])
                else:
                    sentinela = True
                    

    
if(sentinela):
    print("No")
else:
    print("Yes")