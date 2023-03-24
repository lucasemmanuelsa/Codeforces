entrada = int(input())

num4 = entrada // 4
num7 = entrada // 7

soma = 0
list = []
qntDigits4 = 0

bool = False
for i in range(num4 + 1):
    soma = 0
    if(soma == entrada):
        list.append(qntDigits4)
        list.append(qntDigits7)
        bool = True
        break
    soma = i*4
    if(i != 0):
        qntDigits4 +=1
    qntDigits7 = 0
    for j in range(num7 + 1):
        if(j != 0):
            qntDigits7 += 1
            soma += 7
        if(soma == entrada):
            list.append(qntDigits4)
            list.append(qntDigits7)
            bool = True
            break
    if(bool):
        break
if(len(list) == 0):
    print(-1)
else:
    print(list[0]* '4', end='')
    print(list[1]* '7')
