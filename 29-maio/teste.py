# 5
# 1
# 2
# ...
# 1 2 3 4 5
N = int(input())
lista = []

while N > 0:
    num = int(input()) # string
    lista.append(str(num*2))
    N -= 1
    
string = ' '.join(lista)
print(string)
