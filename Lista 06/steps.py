n = input()

mod = 1000000007
numb = 0
numsteps = 0
for i in range(len(n)-1, -1, -1):
    if(n[i] == "b"):
        numb+=1
    else:
        numsteps += numb
        numb = (numb * 2) % mod

print(numsteps % mod)
