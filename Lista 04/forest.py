n = list(map(int, input().split()))

tam = n[0]
queries = n[1]

matriz = []
for i in range(tam):
    string = input()
    entrada = list(map(str, string.strip()))
    matriz.append(entrada)

prefixsum = []
for i in range()

for j in range(queries):
    count = 0
    querie1 = list(map(int, input().split()))
    chords1 = (querie1[0], querie1[1])
    chords2 = (querie1[2], querie1[3])
    for k in range(chords1[0] - 1, chords2[0]):
        for f in range(chords1[1] - 1, chords2[1]):
            if(matriz[k][f] == "*"):
                count+=1
    print(count)
