n = int(input())


dicionario = {}
lista = []
for i in range(n):
    string = input()
    if(string in dicionario):
        dicionario[string] +=1
        print(string + str(dicionario[string]))
    else:
        dicionario[string] = 0
        print('OK')