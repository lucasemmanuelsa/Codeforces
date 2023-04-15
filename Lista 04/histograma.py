entrada = list(map(int, input().split()))
while(len(entrada) > 1 and entrada[0] != 0):
    stack = []
    
    maior = 0
    for i in range(len(entrada)):
        if(not stack):
            stack.append(i)
        elif(entrada[i] > stack[len(stack) - 1]):
            stack.append(i)
        else:
            elemento = stack.pop()
            while(stack and elemento > entrada[i]):
                altura = 