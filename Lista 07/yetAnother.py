n, k = map(int, input().split())
s = input().strip()

a = [0] * 30
for c in input().strip():
    if c.isalpha() and c.islower():
        a[ord(c) - ord('a')] = 1

len = 0
ans = 0
for i in range(n):
    if a[ord(s[i]) - ord('a')]:
        len += 1
    else:
        ans += (len * (len + 1)) // 2
        len = 0

if len:
    ans += (len * (len + 1)) // 2
print(ans)
