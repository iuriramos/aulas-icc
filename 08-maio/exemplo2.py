# media, maior, menor antes num != -1


N = int(input())
soma = 0
contador =0
maior = N

while N != -1:
    soma += N
    contador += 1
    if maior < N:
        maior = N
    N = int(input())
    
print('soma=', soma, ', média=', '%.2f' % (soma/contador), end='')
print(', maior=', maior)     



