#%%
import pandas as pd

data_users = {
    'id': [1, 2, 3, 4],
    'nomes': ["Teo", "Mat", "Nah", "Mah"],
    'idade': [31, 31, 32, 32]
}

df_user = pd.DataFrame(data_users)
df_user

#%%
data_transactions = {
    'id_user': [1, 1, 1, 2, 3, 3],
    'val': [432, 532, 123, 6, 4, 8],
    'qtProdutos': [2, 1, 3, 6, 10, 2]
}

df_transactions = pd.DataFrame(data_transactions)
df_transactions

#%%
df_transactions.merge(df_user, how='left', left_on='id_user', right_on='id')