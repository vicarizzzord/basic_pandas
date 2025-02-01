#%%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

#%%
# Pegando os tipos de dados das colunas do dataframe
df_customers.dtypes

#%%
# Convertendo a coluna 'Points' para formato string
df_customers['Points'].astype(str)

#%%
df_customers