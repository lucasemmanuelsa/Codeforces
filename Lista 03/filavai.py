t = int(input())


queue = []
count = 0
cabeca = -1

for i in range(t):
    entrada = input().split(" ")
    if(entrada[0] == '1'):
        queue.append(entrada[1])
        if(cabeca == -1):
            count +=1
            cabeca +=1
        else:
            count+=1
    elif(entrada[0] == '2'):
        if(count >= 0):
            count-=1
            cabeca +=1
    else:
        if(count > 0):
            print(queue[cabeca])
        else:
            print('Empty!')
        