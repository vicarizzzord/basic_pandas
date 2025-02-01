# %%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=';')
df_customers

#%%
# Pegando o formato do dataframe (LinhasxColunas)
df_customers.shape

#%%
# Pegando a informação geral do dataframe, com acuracidade na memória
df_customers.info(memory_usage='deep')

#%%
# Pegando as informações estatísticas da coluna(série) Points
df_customers["Points"].describe()

#%%
# Criando condição para verificar o usuário com o maior número de pontos
condition = df_customers['Points'] == df_customers['Points'].max()
# Criando um dataframe novo com as informações do usuário com o maior número de pontos
df_richest = df_customers[condition]
# Pegando o nome do usuário com o maior número de pontos
df_richest['Name'].iloc[0]



#%%
# Criando uma condição de comparação em um range de pontos
condition2 = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
# Criando um dataframe com a condição de range de pontos criada
df_between_1000_2000 = df_customers[condition2]
# Pegando as informações estatísticas do dataframe novo
df_between_1000_2000.describe()
# Consulta composta dos dados do dataframe, trazendo as colunas Name e Point
df_between_1000_2000[['Name', 'Points']]

#%%
# Criando uma variável com o nome das colunas
columns = df_customers.columns.tolist()
# Ordenando os nomes das colunas em ordem alfabética
columns.sort()
# Atribuindo as colunas ordenadas no dataframe principal
df_customers = df_customers[columns]
df_customers

#%%
# Renomeando as colunas e atribuindo para o dataframe principal
df_customers = df_customers.rename(columns={'Name': 'Nome', 'Points': 'Pontos'})
df_customers

#%%
# Atribuindo a renomeação para as colunas utilizando 'inplace=True', pois assim, não é necessário
# reatribuir para o dataframe original, o próprio atributo inplace faz isso
df_customers.rename(columns={'UUID': 'ID'}, inplace=True)
df_customers