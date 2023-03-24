queries = int(input())

for i in range(queries):
    nPlanks = int(input())
    planksLenght = input().split(" ")    

    tamanho = []
    for k in planksLenght:
        tamanho.append(int(k))

    tamanho = sorted(tamanho)

    max = tamanho[nPlanks - 1]
    min = tamanho[nPlanks - 2]
    stepMax = min - 1
    sobra = nPlanks - 2

    if(sobra > stepMax):
        print(stepMax)
    else:
        print(sobra)