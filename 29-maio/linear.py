# 100
# lista = [1, 2, 3... 100] >> [100, ..., 1]
# 1 2 ... 100
from random import shuffle

N = int(input())
lista = list(range(1, N+1)) # 1, 2, 3.. N
shuffle(lista)
# print(lista)
contador = 0
for alvo in range(1, N+1): # 1, 2, ..., N
    if alvo in lista:
        contador += 1
    # for num in lista:
        # if num == alvo:
            # contador += 1
print(contador)
            
