def search(array, inicio, fim):
    meio = inicio + (fim - inicio) // 2
    if(inicio >= fim):
        return array[meio]
    if(array[meio] > array[meio+1] and array[meio] > array[meio - 1]):
        return array[meio]
    else:
        if(array[meio] < array[meio-1]):
            return search(array, inicio, meio - 1)
        else:
            return search(array, meio + 1, fim)
#dois casos de borda >>> caso o meio seja o primeiro elemento ou ultimo elemento
entrada = input().split(" ")

lista = []

for i in entrada:
    lista.append(int(i))

num = search(lista, 0, len(lista) - 1)
print(num)