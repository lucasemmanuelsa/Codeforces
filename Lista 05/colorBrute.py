from math import gcd

n = int(input())

dicio = {2:1}
for i in range(3,n+1):
    aux = 0
    coloca = False
    for j in range(2, i):
        if(gcd(i,j) > 1):
            dicio[i] = dicio[j]
            break
        else:
            if(dicio[j] >= aux):
                aux = dicio[j] + 1
            if(j == i - 1):
                coloca = True
    if(coloca):
        dicio[i] = aux
print(" ".join(map(str, dicio.values())))

