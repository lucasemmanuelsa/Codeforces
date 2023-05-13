import math

def solve():
    n, k = map(int, input().split())
    s = ['a'] * n

    p = (math.sqrt(1 + 8 * (k - 1)) - 1) // 2
    temp = (p * (p + 1)) // 2
    s[n - 2 - int(p)] = 'b'
    s[n - int(k - temp)] = 'b'

    print(''.join(s))



testcase = int(input())
for t in range(testcase):
    solve()
