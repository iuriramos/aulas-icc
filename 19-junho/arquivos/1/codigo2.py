import string

# função de contar letras da aula anterior
def conta_letras (texto):
    contador_letras = {}

    for letra in texto:
        contador_letras[letra] = contador_letras.get(letra, 0) + 1

    return contador_letras


# abre o arquivo
f = open("rfc8179.txt", "r")

# lê, conta as letras e coloca em ordem alfabética
conteudo = f.read().lower()
dic_letras = conta_letras(conteudo)
letras = list(dic_letras.items())
letras.sort()


# imprime as informações formatadas
print("Letra    |    Quantidade")
print("---------|--------------")

for (letra, quantidade) in letras:
    print("%s        |    %d" % (letra, quantidade))
