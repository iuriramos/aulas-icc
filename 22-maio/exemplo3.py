alvo = int(input())
lista = list(range(1, 100+1))
encontrei = False
for num in lista:
    if num == alvo:
        encontrei = True
        break
if encontrei:
    print('sim')
else:
    print('não')

# em 'uma' linha    
if alvo in lista:
    print('sim')
else:
    print('não')
