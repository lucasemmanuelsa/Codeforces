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

quebra = False
for a in range(10,99+1):
    for b in range(100, 999+1):
        if(len(str(gcd(a,b))) == 1):
            print(f'{a} {b}')
            quebra = True
            break
    if(quebra):
        break
            