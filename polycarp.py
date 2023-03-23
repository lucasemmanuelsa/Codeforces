n1 = int(input())
lista = input().split(" ")

questoes = []
for k in lista:
    questoes.append(int(k))


questoes = sorted(questoes)

dias = 0

j = 0
i = 1
while(i < n1 + 1 and j < len(questoes)):
    if(i <= questoes[j]):
        i+=1
        j+=1
        dias+=1
    else:
        j+=1
print(dias)