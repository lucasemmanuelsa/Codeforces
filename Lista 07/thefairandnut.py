MOD = 1000000007

def MD(x): return ((x%MOD)+MOD)%MOD

s = input()

res = 1
cn = 1
for c in s:
    if c == 'a':
        cn+=1
    elif c == 'b':
        res = MD(res*cn)
        cn = 1
res = MD(res*cn)

print(MD(res-1))