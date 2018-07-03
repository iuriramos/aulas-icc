
# coding: utf-8

# # Variação da Taxa de Câmbio (real/dólar)

# Mais informações em: [Dataset para Download](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=M&serid=38593&oper=exportCSVUS)

import pandas as pd

'''
precos = pd.read_csv('ipeadata[03-07-2018-02-33].csv')
precos.head(n=10)
precos.info()

# muda colunas
precos.columns = ['data', 'cambio']

# remover linhas em branco
precos.dropna(inplace=True)
precos.head(n=10)
precos.index = range(len(precos))
precos.head(n=10)

# problemas com algumas datas
precos[precos['data'] == '20/06/2018']
precos = precos[precos['cambio'] < 10]


# leitura de .csv
precos.to_csv('new_dolar.csv', index=False)
'''

precos = pd.read_csv('new_dolar.csv')
# precos.head(n=10)
# precos.info()

precos['data'] = pd.to_datetime(precos['data'], format='%d/%m/%Y')
# precos.head(n=10)

def converte_data_em_ano(data):
    return data.year

precos['ano'] = precos['data'].apply(converte_data_em_ano)
# precos.head(n=10)

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight') # bmh, fivethirtyeight

# variação da taxa de câmbio ao longo dos anos
precos.plot.line(x='data', y='cambio', figsize=(16, 3), lw=.5)
plt.show()

# possível análise: O que motivou a aparição dos picos que vemos na figura?

import numpy as np

precos2 = precos.pivot_table(values='cambio', index='ano') # , aggfunc=np.mean
# precos2.head(n=10)

precos2.plot.bar(y='cambio', figsize=(16, 3))
plt.show()

'''
# alternativa
import seaborn as sns

# valor médio da taxa de câmbio ao longo de cada ano
fig = plt.figure(figsize=(16, 3))
sns.barplot(data=precos, x='ano', y='cambio', estimator=np.mean, palette='magma')
'''
