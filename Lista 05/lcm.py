def gcd(a,b):
    fator = 2
    resulta = a
    resultb = b
    menor = a
    if(b < a):
        menor = b
    while(resulta != 1 or resultb != 1):
        if(resulta / fator == resulta//fator and resultb / fator == resultb // fator):
            return fator
        elif(resulta / fator == resulta // fator and resultb / fator != resultb//fator):
            resulta = a/fator
            fator+=1
        elif(resulta / fator != resulta // fator and resultb / fator == resultb // fator):
            resultb = b / fator
            fator += 1
        else:
            if(fator >= menor):
                return 1
            else:
                fator+=1


def lcm(a,b):
    return (a * b) / gcd(a, b)
l,r = map(int, input().split())

quebra = False
for a in range(l, r+1):
    for b in range(l, r+1):
        lc= lcm(a,b)
        if(lc >= l and lc <= r):
            print(a,b)
            quebra = True
            break
    if(quebra):
        break



