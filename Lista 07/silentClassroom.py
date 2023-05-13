from collections import defaultdict

n = int(input())
mp = defaultdict(int)

for _ in range(n):
    s = input()
    c = s[0]
    mp[c] += 1

sum = 0
for a in mp.values():
    fst = (a // 2) + (a % 2)
    snd = a // 2
    sum += fst * (fst - 1) // 2 + snd * (snd - 1) // 2

print(sum)
