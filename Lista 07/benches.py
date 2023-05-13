def C(m, n):
    ans = 1
    num = 1
    while n > 0:
        ans *= m
        ans //= num
        m -= 1
        num += 1
        n -= 1
    return ans


n = int(input())
print(120 * C(n, 5) * C(n, 5))
