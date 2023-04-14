n = input().split()

tam = int(n[0])
queries = int(n[1])

matriz = []

for j in range(tam):
    string = input()
    matriz.append(string)

resultado = []

for m in range(tam):
    linha = []
    for l in range(tam):
        soma = 0
        if(matriz[m][l] == "*"):
            soma = 1
        if(m == 0 and l == 0):
            linha.append(soma)
        elif(m == 0 and l > 0):
            count = linha[l-1] + soma
            linha.append(count)
        elif(m > 0 and l == 0):
            count = resultado[m-1][l] + soma
            linha.append(count)
        else:
            count = resultado[m-1][l] + linha[l-1] + soma - resultado[m-1][l-1]
            linha.append(count)
    resultado.append(linha)

for x in range(queries):
    entrada = input().split()
    chord1 = (int(entrada[0]) - 1, int(entrada[1]) - 1)
    chord2 = (int(entrada[2]) - 1, int(entrada[3]) - 1)

    esquerda = 0
    if(chord1[1] - 1 >= 0):
        esquerda = resultado[chord2[0]][chord1[1] - 1]

    cima = 0
    if(chord1[0]-1 >= 0):
        cima = resultado[chord1[0]-1][chord2[1]]
    
    diagonal = 0
    if(chord1[0] - 1 >= 0 and chord1[1] - 1 >= 0):
        diagonal = resultado[chord1[0] - 1][chord1[1] - 1]
    soma = resultado[chord2[0]][chord2[1]] - esquerda - cima + diagonal
    print(soma)
