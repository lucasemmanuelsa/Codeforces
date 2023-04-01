n = int(input())
lista1 = list(map(int, input().split(" ")))
lista2 = list(map(int, input().split(" ")))
lista3 = list(map(int, input().split(" ")))

dicionario1 = dict()

for i in lista1:
    if(i in dicionario1):
        dicionario1[i] += 1
    else:
        dicionario1[i] = 0

dicionario2 = dict()

for j in lista2:
    if(j in dicionario2):
        dicionario2[j] += 1
    else:
        dicionario2[j] = 0

dicionario3 = dict()

for k in lista3:
    if(k in dicionario3):
        dicionario3[k] += 1
    else:
        dicionario3[k] = 0

for key in dicionario1:
    if(key not in dicionario2):
        print(key)
    else:
        if(dicionario1[key] != dicionario2[key]):
            print(key)

for key1 in dicionario2:
    if(key1 not in dicionario3):
        print(key1)
    else:
        if(dicionario2[key1] != dicionario3[key1]):
            print(key1)