#%%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers



#%%
# Ordenando os valores de Pontos e setando o critério de desempate sendo a ordem alfabética dos nomes e renomeando o
# nome das colunas e atribuindo para o dataframe principal. Tudo em um pipeline
df_customers = (df_customers.sort_values(by=['Points', 'Name'], ascending=[False, True])
                            .rename(columns={'Name': 'Nome',
                                             'Points': 'Pontos',
                                             'UUID': 'ID'}))
df_customers