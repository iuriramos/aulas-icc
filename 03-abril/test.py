contador = 0
soma = 0
nota = input('Digite uma nota: ')
nota = float(nota)

while nota >= 0:
    contador += 1 # contador = contador + 1
    soma += nota # soma = soma + nota
    nota = input('Digite uma nota: ')
    nota = float(nota)

if contador == 0:
    print ('Mensagem de erro...')
else:
    # tudo OK
    print ('Média é igual a ', soma/contador)

