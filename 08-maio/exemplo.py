N = int(input()) # 100
# calcular a soma e média de todos os números pares de 0, 100 (N)

soma = 0
contador = 0

for num in range(0, N+1, 2):
    print(num, end=' ')
    soma += num
    contador += 1

print()
print(soma)

media = soma//contador
print(media)
