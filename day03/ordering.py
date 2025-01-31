#%%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers



#%%
df_customers = (df_customers.sort_values(by=['Points', 'Name'], ascending=[False, True])
                            .rename(columns={'Name': 'Nome',
                                             'Points': 'Pontos',
                                             'UUID': 'ID'}))
df_customers