def C(n, m):
    result = 1
    for i in range(m):
        result *= (n - i)
        result //= (i + 1)
    return result

n, m, t = map(int, input().split())

ways = 0
for i in range(4, t):
    ways += C(n, i) * C(m, t - i)

print(ways)
