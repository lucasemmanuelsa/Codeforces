n = list(map(int, input().split()))

tam = n[0]
queries = n[1]

matriz = []

for j in range(tam):
    string = input()
    matriz.append(string)

resultado = []

for f in range(tam+1):
    resultado.append([0]*(tam+1))

for m in range(1, tam+1):
    for l in range(1, tam+1):
        soma = 0
        if(matriz[m-1][l-1] == "*"): soma = 1
        resultado[m][l] = resultado[m-1][l] + resultado[m][l-1] + soma - resultado[m-1][l-1]

for x in range(queries):
    entrada = list(map(int, input().split()))
    chord1 = (entrada[0], entrada[1])
    chord2 = (entrada[2], entrada[3])
    soma = resultado[chord2[0]][chord2[1]] - resultado[chord2[0]][chord1[1] - 1] - resultado[chord1[0]-1][chord2[1]] + resultado[chord1[0] - 1][chord1[1] - 1]
    print(soma)