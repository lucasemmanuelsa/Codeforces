n = int(input())
string = input()


stack = []
count1 = 0
count2 = 0
if(len(string) % 2 != 0):
    print("No")
    exit()
else:
    for i in range(len(string)):
        if(string[i] == "("):
            stack.append("(")
            count1+=1
        else:
            if(not stack):
                stack.append(")")
                count2+=1
            else:
                if(stack[len(stack) - 1] == "("):
                    stack.pop()
                    count1-=1
                else:
                    stack.append(")")
                    count2+=1
    


if(not stack):
    print("Yes")
elif(count1+count2) % 2 != 0:
    print("No")
else:
    if(count1 + count2 > 2):
        print("No")
    else:
        if(count1 == count2):
            print("Yes")
        else:
            print("No")
