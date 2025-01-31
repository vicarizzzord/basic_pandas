# %%
import pandas as pd

# %%

data = {
    "nome": ["Leo", "Patricia", "Anderson", "Júlia"],
    "sobrenome": ["Andrade", "Albuquerque", "Fabrício", "Mendes"],
    "idade": [25, 27, 33, 34]
}

data['idade'][0]

#%%
# Criando um dataframe
data_df = pd.DataFrame(data)
data_df

# %%

# Acessando um valor em um dataframe
data_df['idade'].iloc[0]

# Acessando uma series em um data frame. Obs: um dataframe é uma coleção de series
data_df.iloc[0]

#%%
# Exibe as colunas do dataframe
data_df.columns

#%%
# Exibe as informações do dataframe, como, tipo de dado da coluna, se é nulo, memória(o valor nesse método não é tão acurado) etc
data_df.info()

#%%
# Exibe as informações com acuracidade com a quatidade de memória utilizada
data_df.info(memory_usage='deep')

#%%
# Exibe uma series com o tipo de valor das colunas
data_df.dtypes

#%%
data_df['peso'] = [95, 64, 88, 73]

# Aplica as estatísticas em todas as colunas numéricas
summary = data_df.describe()

summary['peso']['mean']

#%%
# Mostra as 5 primeiras linhas do dataframe (porém pode ser alterado o tamanho ao incluir um número dentro do método)
data_df.head()

# Mostra as 5 últimas linhas do dataframe (porém pode ser alterado o tamanho ao incluir um número dentro do método)
data_df.tail()