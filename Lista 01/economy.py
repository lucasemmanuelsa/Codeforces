n = int(input())

casa = 1234567
carro = 123456
computador = 1234


for a in range((n // casa) + 1):
    for b in range((n - a * casa) // carro + 1):
        if(n - a * casa - b * carro) % computador == 0:
            print("YES")
            exit()     

print("NO")