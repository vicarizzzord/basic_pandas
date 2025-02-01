#%%
import pandas as pd

df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

#%%
condition = df_transactions['IdCustomer'] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df_transactions[condition]
df_user['Points'].sum()

#%%
df_summary = df_transactions.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()



#%%
from datetime import datetime

last_transaction = df_transactions['DtTransaction'][0]
today = datetime.now()


#%%
df_user = df_transactions[condition]

def recency(transaction_date):
    date_diff = today - transaction_date.max()
    return date_diff.days

(df_transactions.groupby(['IdCustomer'])
                .agg({'Points': 'sum',
                      'UUID': 'count',
                      'DtTransaction': recency})
                .rename(columns={
                    'Points': 'Pontos',
                    'UUID': 'Frequência',
                    'DtTransaction': 'Ultima Transação'
                })
                .reset_index())