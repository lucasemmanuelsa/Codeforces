A = [2,3,5,9,10]

B = [5,7,9]

c = []

i = 0
j = 0

while(i < len(A) and j < len(B)):
    if(A[i] <= B[j]):
        c.append(A[i])
        i+=1
    else:
        c.append(B[j])
        j+=1
    
while(i < len(A)):
    c.append(A[i])
    i+=1
while(j < len(B)):
    c.append(B[j])
    j+=1

print(c)

