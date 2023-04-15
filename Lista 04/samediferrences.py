t = int(input())


for k in range(t):
    num = int(input())
    entrada = list(map(int, input().split()))
    dicio = {}
    lista = set()
    for i in range(len(entrada)):
        entrada[i] = entrada[i] - i
        if entrada[i] not in dicio:
            dicio[entrada[i]] = 1
        else:
            dicio[entrada[i]] += 1
            lista.add(entrada[i])
    
    soma = 0
    for key in lista:
        n = dicio[key] - 1
        soma += ((n + 1) * n) // 2
        
    print(soma)