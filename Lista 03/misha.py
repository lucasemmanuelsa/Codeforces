n = int(input())

dicionario = {}
for i in range(n):
    entrada = input().split()
    if(entrada[0] in dicionario.values()):
        for key in dicionario.keys():
            if(dicionario[key] == entrada[0]):
                dicionario[key] = entrada[1]
    else:
        dicionario[entrada[0]] = entrada[1]

print(len(dicionario))
for key in dicionario.keys():
    print(f'{key} {dicionario[key]}')
