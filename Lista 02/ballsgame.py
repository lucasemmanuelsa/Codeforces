entrada = input().split(" ")
lista = input().split(" ")

nBolas = int(entrada[0])
nCores = int(entrada[1])
cor = int(entrada[2])

linha = []
for i in lista:
    linha.append(int(i))


auxLinha = linha.copy()
count = 0
i = 0
qntbolas = 0
maximo = 0
final = False
while(i < len(auxLinha)):
    
    j = i
    qntbolas = 0
    count = 0
    if(auxLinha[i] == cor):
        while(j < len(auxLinha)):
            if(auxLinha[j] == cor):
                count+=1
            else:
                break
            j+=1
        if(count == 2):
            del auxLinha[i]
            del auxLinha[i]
            qntbolas += 2
            l = i
            k = l - 1
            p = l + 1
            
            while(k >= 0 and len(auxLinha) > 0 and l < len(auxLinha) and auxLinha[k] == auxLinha[l]):
                sequencia = 1
                while(k >= 0 and k < len(auxLinha) and auxLinha[k] == auxLinha[l]):
                    sequencia+=1
                    k-=1
                k+=1
                while(p < len(auxLinha) and p >= 0 and auxLinha[p] == auxLinha[l]):
                    sequencia+=1
                    p+=1
                p -= 1
                if(sequencia >= 3):
                    for m in range(sequencia):
                        del auxLinha[k]
                        qntbolas+=1
                
                
                l = k
                k -= 1
                p = l + 1

            if(qntbolas > maximo):
                maximo = qntbolas
            if(len(auxLinha) == 0):
                final = True
            auxLinha = linha.copy()
            
    
    i+=1
    if(final):
        break

print(maximo)
        
