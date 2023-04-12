from collections import deque

entrada1 = list(map(int, input().split()))
n = entrada1[0]
q = entrada1[1]
cores = deque(map(int, input().split()))

qcor = list(map(int, input().split()))

lista = []
for i in qcor:
    index = cores.index(i)
    cores.remove(i)
    cores.insert(0, i)
    lista.append(index + 1)

resposta = list(map(str, lista))
print(" ".join(resposta))