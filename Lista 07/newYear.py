n = int(input())
mini,maxi,asc,nasc = [], [], 0, 0

for index in range(n):
    s = list(map(int, input().split()))[1:]

    for i in range(len(s)):
        if i>0 and s[i] > s[i-1]:
            asc +=1
            break
        elif i == len(s) - 1:
            nasc +=1
            mini.append(min(s))
            maxi.append(max(s))
total = asc*asc + 2*asc*nasc
mini.sort()
maxi.sort()
i = 0
for x in maxi:
    while i<nasc and mini[i] < x:
        i+=1
    total += i

print(total)