import math
n = int(input())

def isEven(n):
    if(n % 2 == 0):
        return True
    return False

def isPrimo(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if(n % i == 0):
            return False
    return True

def dif(n):
    count = 0

    while(n > 0):
        i = 2
        while(i < n+1):
            if(n % i == 0):
                if(isEven(n)):
                    count+= n//i
                    return count
                else:
                    n = n - i
                    count +=1
                    i=2
                    break
            i+=1
    return count


if(n % 2 != 0):
    if(isPrimo(n)):
        print(1)
    else:
        print(dif(n))
else:
    print(n // 2)
        

