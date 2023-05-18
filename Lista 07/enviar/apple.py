MOD = int(1e9+7)
maxN = 2 * int(1e6)

fact = [1] * maxN
inv = [1] * maxN

def inverse(x):
    res = 1
    expo = MOD-2
    while expo > 0:
        if expo&1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        expo >>= 1
    return res

def init():
    fact[0] = inv[0] = 1
    for i in range(1, maxN):
        fact[i] = i * fact[i-1] % MOD
        inv[i] = inverse(fact[i])

def choose(n, k):
    return fact[n] * inv[k] % MOD * inv[n-k] % MOD

N, M = map(int, input().split())
init()
print(choose(N+M-1, M))
