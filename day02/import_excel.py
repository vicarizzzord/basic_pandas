#%%
import pandas as pd

df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

#%%
df_transactions.shape

#%%
df_transactions.head()

#%%
df_transactions.tail()

#%%
columns = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']

df_transactions = df_transactions[columns]
df_transactions

#%%
df_transactions.info(memory_usage='deep')
