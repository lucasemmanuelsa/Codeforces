n = int(input())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort()

stack = []
for interval in intervals:
    if not stack:
        stack.append(interval)
    else:
        top = stack[-1]
        if interval[0] <= top[1]:
            merged = (top[0], max(top[1], interval[1]))
            stack.pop()
            stack.append(merged)
        else:
            stack.append(interval)

for interval in stack:
    print(interval[0], interval[1])
