import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s1, s2 = map(int, input().split())
    v = []
    x = list(map(int, input().split()))
    for i in range(n):
        v.append((x[i], i))
    v.sort(reverse=True)
    t1 = min(s1, s2)
    t2 = max(s1, s2)
    b = [0] * n
    start = 0
    r1, r2 = 0, 0
    while True:
        if start >= n:
            break
        r1 += 1
        r2 += 1
        if r1 >= t1:
            b[v[start][1]] = 1
            start += 1
            r1 = 0
        if start >= n:
            break
        if r2 >= t2:
            b[v[start][1]] = 2
            start += 1
            r2 = 0
    v1, v2 = [], []
    if s1 > s2:
        for i in range(n):
            if b[i] == 1:
                b[i] = 2
            else:
                b[i] = 1
    for i in range(n):
        if b[v[i][1]] == 1:
            v1.append(v[i][1])
        else:
            v2.append(v[i][1])
    print(len(v1), end=" ")
    for i in range(len(v1)):
        print(v1[i] + 1, end=" ")
    print()
    print(len(v2), end=" ")
    for i in range(len(v2)):
        print(v2[i] + 1, end=" ")
    print()

