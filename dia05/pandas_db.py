#%%
import pandas as pd
import sqlalchemy

#%%
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')


#%%
df_transaction_cart = pd.read_sql_table('transactions_cart', engine)

#%%
query = "SELECT * FROM customers LIMIT 10"

df_customers = pd.read_sql_query(query, engine)
df_customers

#%%
query = '''SELECT * 
            FROM customers as t1 
            LEFT JOIN transactions as t2
            on t1.UUID = t2.IdCustomer
            LIMIT 10'''
df_join = pd.read_sql_query(query, engine)
df_join

#%%
data_01 = {
    'id': [1, 2, 3, 4],
    'nomes': ["Teo", "Mat", "Nah", "Mah"],
    'idade': [31, 31, 32, 32]
}
df_01 = pd.DataFrame(data_01)

data_02 = {
    'id': [5, 6, 7, 8],
    'nomes': ["José", "Nathan", "Arnaldo", "Mario"],
    'idade': [23, 33, 19, 21]
}
df_02 = pd.DataFrame(data_02)

#%%
df_01.to_sql('tb_users1', engine, index=False)

#%%
df_02.to_sql('tb_users1', engine, index=False, if_exists='append')

#%%
query = 'SELECT * FROM tb_users1'
df_users = pd.read_sql_query(query, engine)
df_users