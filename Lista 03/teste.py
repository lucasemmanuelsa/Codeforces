def is_correct_parentheses(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c in ')]':
            if not stack:
                return False
            elif c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

n = int(input())
for i in range(n):
    s = input().strip()
    if is_correct_parentheses(s):
        print('Yes')
    else:
        print('No')