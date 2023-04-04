entrada = list(map(int, input().split()))
lista = list(map(int, input().split()))

t = entrada[1]
c = entrada[2]

i = 0
j = 0
sentinela = 0
count = 0
numero = 0
tem = False
menor = False

maior = 0
menor = 0
listaN = []
countN = 0
while(i < len(lista)):
    
    if(lista[i] > t):
      listaN.append(countN)
      countN = 0
      maior += 1
    else:
      menor = True
      menor +=1
      countN +=1
    i+=1

for k in listaN:
   if k >= c:
      count += k - c + 1
      
if(countN > 0):
   if(countN >= c):
    count += countN - c + 1
if(menor == False):
   count = 0


print(count)