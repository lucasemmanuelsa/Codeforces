b = int(input())

count = 0

raiz = b**(1/2)
i = 1
while(i <= raiz):
    if(b % i == 0):
        count+=1
        if(i != raiz):
            count+=1
    i+=1
print(count)