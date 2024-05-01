import pandas as pd
# pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# Somente um é obrigatório para se criar um DataFrame com dados, o parâmetro data=XXXX. 
# Pode receber, um objeto iterável, como uma lista, tupla, um dicionário ou um DataFrame, vejamos os exemplos.

# CONSTRUTOR DATAFRAME COM LISTA

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

dados = list(zip(lista_nomes, lista_idades, lista_emails )) # cria uma lista de tuplas # ('howard', 32, 'risus.varius@dfictumPhasellusin.ca') 

db = pd.DataFrame(data = dados, index = lista_cpfs, columns=['Nome', 'idade', 'E-mail'])

print(db)

# CONSTRUTOR DATAFRAME COM DICIONÁRIO

'''Cada chave será uma coluna e pode ter atribuída uma lista de valores. Obs: cada chave deve estar associada a uma lista de mesmo tamanho.'''

df_dados_dic = pd.DataFrame({ 
    'nomes':  lista_nomes,
    'cpfs' : lista_cpfs,
    'emails' : lista_emails,
    'idades' : lista_idades
    })

print('\n', df_dados_dic)

# EXTRAINDO INFORMAÇÕES DE UM DATAFRAME

print('\nInformações do DataFrame:\n')
print(db.info())  # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', db.shape)  # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', db.dtypes)  # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', db.min())  # Extrai o menor de cada coluna
print('\nQual o maior valor?\n', db.max())  # Extrai o valor máximo e cada coluna

# Calculando a média apenas das colunas numéricas
colunas_numericas = db.select_dtypes(include=['int64', 'float64']).columns
print('\nQual a média aritmética?\n', db[colunas_numericas].mean())

print('\nQual o desvio padrão?\n', db[colunas_numericas].std())  # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', db[colunas_numericas].median())  # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', db.describe())  # Exibe um resumo

print('\nOs 5 primeiros registros do DataFrame:')
print(db.head())  # Exibe os 5 primeiros registros do DataFrame