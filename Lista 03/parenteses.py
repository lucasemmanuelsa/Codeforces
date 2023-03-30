n = int(input())


def checarParenteses(string):
    stack = []

    for char in string:
        if(char in '(['):
            stack.append(char)
        elif(char in '])'):
            if(not stack): #se tiver vazia
                return False
            elif(char == ']' and stack[-1] == '[' or char == ')' and stack[-1] == '('):
                stack.pop()
            else:
                return False
    return not stack

for i in range(n):
    string = input().strip()

    if(checarParenteses(string)):
        print('Yes')
    else:
        print('No')