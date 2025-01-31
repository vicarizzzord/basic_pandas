# %%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=';')
df_customers

#%%
df_customers.shape

#%%
df_customers.info(memory_usage='deep')

#%%
df_customers["Points"].describe()

#%%

condition = df_customers['Points'] == df_customers['Points'].max()
df_richest = df_customers[condition]
df_richest['Name'].iloc[0]



#%%
condition2 = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_between_1000_2000 = df_customers[condition2]
df_between_1000_2000.describe()
df_between_1000_2000[['Name', 'Points']]

#%%
columns = df_customers.columns.tolist()
columns.sort()

df_customers = df_customers[columns]
df_customers

#%%
df_customers = df_customers.rename(columns={'Name': 'Nome', 'Points': 'Pontos'})
df_customers

#%%
df_customers.rename(columns={'UUID': 'ID'}, inplace=True)
df_customers