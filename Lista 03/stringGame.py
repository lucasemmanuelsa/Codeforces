string = list(input())

i = 0

count = 0
while(i < len(string) - 1):
    if(string[i] == string[i+1]):
        del string[i]
        del string[i]
        count +=1
        if(i != 0):
            i-=1
    else:
        i+=1

if(count % 2 == 0):
    print('No')
else:
    print('Yes')