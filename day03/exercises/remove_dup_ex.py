#%%
import pandas as pd

df_transaction = pd.read_excel('../data/transactions.xlsx')
df_transaction

#%%
df_last_transaction = (df_transaction.sort_values(by='DtTransaction', ascending=False).drop_duplicates(subset=['IdCustomer'], keep='first'))
df_last_transaction

#%%
df_last_transaction['IdCustomer'].nunique()

#%%
condition = df_transaction['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_transaction[condition]

#%%
df_last_transaction[df_transaction['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']