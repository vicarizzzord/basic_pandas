#%%
import pandas as pd
import numpy as np

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

#%%
df_customers['Points_double'] = df_customers['Points'] * 2
df_customers

#%%
df_customers['Points_ratio'] = df_customers['Points_double'] / df_customers['Points']
df_customers

#%%
df_customers['Constant'] = 1
df_customers

#%%
df_customers['Points_log'] = np.log(df_customers['Points'])
df_customers

#%%
df_customers['Names_upper'] = df_customers['Name'].str.upper()
df_customers

#%%

def getFirst(name: str):
    return name.split('_')[0]

#%%

df_customers['First_name'] = df_customers['Name'].apply(getFirst)
df_customers

#%%

df_customers['First_name'] = df_customers['Name'].apply(lambda x: x.upper().split('_')[0])
df_customers

#%%
def pointsInterval(points: int):
    if points < 2500:
        return 'Baixo'
    elif points < 3500:
        return 'Médio'
    else:
        return 'Alto'

#%%
df_customers['Point_range'] = df_customers['Points'].apply(pointsInterval)
df_customers

#%%
data = {
    'nome': ['Téo', 'Nah', 'Maria', 'Lara'],
    'recencia': [1, 30, 10, 45],
    'valor': [100, 2000, 15, 500],
    'frequencia': [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm

#%%
def rfv(row):
    score = 0
    if row['recencia'] <= 10:
        score += 10
    elif 10 < row['recencia'] <= 30:
        score += 10
    elif row['recencia'] > 30:
        score += 0
    
    if row['valor'] > 1000:
        score += 10
    elif 100 <= row['valor'] < 1000:
        score += 5
    elif row['valor'] < 100:
        score += 0
        
    if row['frequencia'] > 10:
        score += 10
    elif 5 <= row['frequencia'] < 10:
        score += 5
    elif row['frequencia'] < 5:
        score += 0
        
    return score

#%%
df_crm['RFV'] = df_crm.apply(rfv, axis=1)
df_crm