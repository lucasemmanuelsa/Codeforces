n = int(input())
string = list(input())

i = 0
j = 1
while(i < len(string) and j < len(string)):
    if(string[i] == "U" and string[j] == "R" or string[i] == "R" and string[j] == "U"):
        string[i] = "D"
        del string[j]
        i += 1
        j += 1
    else:
        i+= 1
        j += 1


print(len(string))