t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    presentes = list(map(int, input().split()))
    envios = list(map(int, input().split()))

    dicio = {}
    for i in range(n):
        dicio[presentes[i]] = i

    ultimo = -1
    tempo = 0
    for i in range(m):
        index = dicio[envios[i]]

        if index > ultimo:
            tempo += 2 * (index - i) + 1
            ultimo = index

        else:
            tempo += 1

    print(tempo)

            
        
        
        
