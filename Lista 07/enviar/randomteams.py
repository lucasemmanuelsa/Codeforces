def pairs(n):
    return n * (n - 1) // 2

n, m = map(int, input().split())
a, b = n // m, n % m
min_val = pairs(a) * (m - b) + pairs(a + 1) * b
max_val = pairs(n - m + 1)
print(min_val, max_val)
