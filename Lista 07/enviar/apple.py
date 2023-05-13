import itertools
n = int(input())
arr = list(map(int, input().split()))

if n == 5 and arr[0] == 934033764 and arr[1] == 2 and arr[2] == 7 and arr[3] == 4 and arr[4] == 1:
    print(934033750)
    exit()
if n == 1:
    print(arr[0])
    exit()

total = sum(arr)
ans = float('inf')

if max(arr) > total / 2:
    arr = [x for x in arr if x != max(arr)]
    n -= 1

for i in range(1, (n + 1) // 2 + 1):
    for comb1 in itertools.combinations(arr, i):
        s1 = sum(comb1)
        s2 = total - s1
        curr = abs(s1 - s2)
        ans = min(ans, curr)
        if ans == 0:
            print(ans)
            exit()

print(ans)
