entrada = input().split(" ")

lista = []
for i in entrada:
    lista.append(int(i))


qntLivros = lista[0]
k = 0
opcoes = []
rubles = 0
teste = qntLivros % 4
def iterator():
    if(k != 0):
        for c in range((k // 3) + 1):
            for b in range((k // 2) + 1):
                for a in range((k // 1) + 1):
                    if(c * 3 + b * 2 + a * 1 == k):
                        rubles = c * lista[3] + b * lista[2] + a * lista[1]
                        opcoes.append(rubles)
if teste != 0:
    while qntLivros % 4 != 0 or k//3 == 0 or k % 3 != 0:
        qntLivros+=1
        k += 1
        if(qntLivros % 4 == 0):
            iterator()
        
if(k != 0):
    print(min(opcoes))
else:
    print(k)
