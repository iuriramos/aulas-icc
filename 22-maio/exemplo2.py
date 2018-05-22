import random
lista = list(range(1, 100+1))
N = len(lista)
random.shuffle(lista)

alvo = int(input())
index = 0

while index < N:
    if lista[index] == alvo:
        print (index)
    index += 1

print()
print(lista.index(alvo))

