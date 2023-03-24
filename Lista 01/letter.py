number = int(input())
list = str(input()).split()

count = 0
op = 0
um = 0
while count < number:
    if(list[count] == "1"):
        um += 1

    count += 1

countum = 0

count = 0
while countum < um:
    
    if(count == number - 1 and list[count] == "1"):
        op+=1
        countum += 1
        break
    else:
        if(list[count] == "1"):
            op+= 1
            countum += 1
        if (list[count] == "1" and list[count + 1] == "0" and countum != um):
            op += 1  
    

    count+=1

print(op)
