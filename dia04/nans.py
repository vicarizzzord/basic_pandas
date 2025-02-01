#%%
import pandas as pd
import numpy as np

#%%
data = {
    'nome': ['Téo', 'Nah', 'Lara', 'Maria', 'João'],
    'idade': [31, 32, 34, 12, np.nan],
    'renda': [np.nan, 3245, 357, 12432, np.nan]
}

#%%
df = pd.DataFrame(data)
df

#%%
# Retornando a soma dos valores faltantes da coluna 'idade'
df['idade'].isna().sum()

#%%
# Retornando a soma dos valores faltantes no dataframe inteiro, separado por colunas
df.isna().sum()

#%%
# Média dos valores faltantes do dataframe, separado por colunas
df.isna().mean()

#%%
# Adicionando a média dos valores nas linhas faltantes (Obs: nunca é feito dessa forma, geralmente é utilizado machine learning para realizar o preenchimento das informações faltantes)
df.fillna({'idade': df['idade'].mean(),
           'renda': df['renda'].mean()})

#%%
# Remove a linha dos valores faltante, caso a linha inteira esteja com valores faltantes
df.dropna(subset=['idade', 'renda'], how='all')

#%%
# Remove os valores faltantes caso a coluina inteira esteja com valores faltantes
df.dropna(axis=1, how='all')

#%%
