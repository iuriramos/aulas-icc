import csv
import datetime as dt
import matplotlib.pyplot as plt

datas = []
valores = []

### lê os dados do arquivo csv
# abre o arquivo dolar.csv para leitura
with open('new_dolar.csv', 'r') as csvfile:
    # carrega todos os dados do arquivo
    dados = list(csv.reader(csvfile))
    
    # remove a 1ª linha (cabeçalho)
    dados = dados[1:]

    # anda por todas as linhas do arquivo
    for linha in dados:
        data = dt.datetime.strptime(linha[0],'%d/%m/%Y').date()
        datas.append(data)

        valor = float(linha[1])
        valores.append(valor)

### grafico em linha da variação ao passar do tempo
grafico_linha = plt.figure(1)
plt.title("Variação do U$")
plt.xlabel("Data")
plt.ylabel("R$")
plt.plot(datas, valores)
#plt.savefig("variacao_dolar.pdf")
plt.show()


### encontra a media do dólar por ano
media_atual = 0
quant_atual = 0
ano_atual = datas[0].year
anos = []
medias = []

# passa por todas as datas
for i in range(len(datas)):
    ano = datas[i].year

    # se é o ano que estamos analisando, continua acumulando
    if ano == ano_atual:
        media_atual += valores[i]
        quant_atual += 1
    
    # quando for um ano novo, calcula a média anterior
    else:
        medias.append(media_atual/quant_atual)
        media_atual = valores[i]
        quant_atual = 1
        anos.append(ano_atual)
        ano_atual = ano

# acrescenta a ultima media calculada e ano encontrado
medias.append(media_atual/quant_atual)
anos.append(ano_atual)

### grafico de barras do preço médio por ano
grafico_barra = plt.figure(2)
plt.title("Preço médio do U$")
plt.xlabel("Ano")
plt.ylabel("R$")
plt.bar(anos,medias)
#plt.savefig("media_dolar.pdf")
plt.show()
