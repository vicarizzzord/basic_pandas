#%%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

#%%

df_customers.dtypes

#%%
df_customers['Points'].astype(str)

#%%
df_customers