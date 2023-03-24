nBarras = int(input())
preco = input().split(" ")
cupons = int(input())
numbarrascumpom = input().split(" ")


valores = []
for i in preco:
    valores.append(int(i))

barrascupom = []
for j in numbarrascumpom:
    barrascupom.append(int(j))

valores = sorted(valores)
total = sum(valores)

def operacao(valores, num, total):
    
    soma = total - valores[len(valores) - num]
    return soma
        

for a in barrascupom:
    print(operacao(valores, a, total))