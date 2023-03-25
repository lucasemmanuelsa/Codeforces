n = input().split(" ")

lista = []
for i in n:
    lista.append(int(i))


def recursive(soma, total, mov):
    if(soma == total):
        return mov
    if(soma > total):
        return -1
    if(soma < total):
        return max(recursive(soma*3, total, mov+1), recursive(soma*2, total, mov+1))
        
        
print(recursive(lista[0], lista[1], 0))