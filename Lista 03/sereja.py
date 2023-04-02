n = list(map(int, input().split()))
lista = list(map(int, input().split()))

m = n[1]

for i in range(m):
    numero = int(input())
    aux = lista[numero-1:]
    resposta = len(set(aux))
    print(resposta)