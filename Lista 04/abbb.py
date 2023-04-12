n = int(input())

for i in range(n):
    string = input()
    stack = []
    for j in range(len(string)):
        if(not stack):
            stack.append(string[j])
        else:
            if(string[j] == "A"):
                stack.append(string[j])
            elif(stack[len(stack) - 1] == "A" or stack[len(stack) - 1] == "B"):
                stack.pop()
    
    print(len(stack))