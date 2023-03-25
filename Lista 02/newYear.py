entrada = input().split(" ")

lista = []
for i in entrada:
    lista.append(int(i))

lista = sorted(lista)

distancia = lista[1] - lista[0] + lista[2] - lista[1]

print(distancia)