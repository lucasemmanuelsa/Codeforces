n = int(input())
numeros = list(map(int, input().split()))
quadrados = [0,0,0,0]

p = 0
for i in numeros:
    quadrados[0] = 1
    for j in range(3, -1,-1):
        if(quadrados[j] == 1):
            if(j + i > 3):
                p+=1
                quadrados[j] = 0
            else:
                quadrados[j+i] = 1
                quadrados[j] = 0

print(p)

        