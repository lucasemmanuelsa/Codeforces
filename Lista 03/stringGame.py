string = list(input())

print(string)

i = 0
j = 1
count = 0
while(i < len(string) and j < len(string)):
    if(string[i] == string[j]):
        del string[j]
        del string[i]
        count+=1
        i = 0
        j = 0
    else:
        i+=1
        j+=1

if(count % 2 == 0):
    print('No')
else:
    print('Yes')
print(string)