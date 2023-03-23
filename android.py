numero = int(input())
lista = input()

i = 0

num1 = 0
num0 = 0
while i < len(lista):
    if(lista[i] == "1"):
        num1 += 1
    else:
        num0 += 1
    i+=1
    

if(num1 > num0):
    saida = num1 - num0
else:
    saida = num0 - num1

print(saida)