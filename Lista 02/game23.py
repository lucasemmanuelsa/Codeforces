n = input().split(" ")

inicio = int(n[0])
fim = int(n[1])

numero2 = 0
numero3 = 0

aux = inicio
while(aux < fim):
    numero2+=1
    aux = aux * 2

aux2 = inicio
while(aux2 < fim):
    numero3+=1
    aux2 = aux2 * 3

soma = 0

list = []
bool = False
qntMov2 = 0
qntMov3 = 0
achou = True
for i in range(numero2 + 1):
    
    soma = inicio * (2 ** i)
    j=0
    #print(f'{soma} - i = {i}')
    if(soma == fim):
        list.append(i)
        list.append(j)
        bool = True
        break
    qntMov3 = 0
    for j in range(numero3 + 1):
        if(j != 0):
            soma = soma * 3
        #print(f'{soma} - j = {j}')
        if(soma == fim):
            list.append(i)
            list.append(j)
            bool = True
            break
        
    if(bool):
        break

if(len(list) == 0):
    print(-1)
else:
    print(list[0] + list[1])