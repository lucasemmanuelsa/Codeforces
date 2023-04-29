a,b = map(int, input().split())

max = a - b
count = 0
if a == 0 and b == 0:
    print("infinity")
elif a == 0:
    print(0)
elif a < b:
    print(0)
elif max == 0:
    print("infinity")
else:
    raiz = max**(1/2)
    for i in range(1, int(raiz)+1):
        if(max % i == 0):
            if(a % i == b):
                count+=1
            if(i != raiz):
                if(a % (max//i) == b):
                    count+=1
    print(count)
