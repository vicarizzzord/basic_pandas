#%%
import pandas as pd
import numpy as np

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

#%%
# Criando uma nova coluna no dataframe e realizando um cálculo com a coluna Points e adicionando nessa nova coluna
df_customers['Points_double'] = df_customers['Points'] * 2
df_customers

#%%
df_customers['Points_ratio'] = df_customers['Points_double'] / df_customers['Points']
df_customers

#%%
# Adicionando um valor constante em todas as linhas da coluna do dataframe
df_customers['Constant'] = 1
df_customers

#%%
# Calculando o log da coluna Points e adicionando o cálculo de cada linha na coluna Points_log
df_customers['Points_log'] = np.log(df_customers['Points'])
df_customers

#%%
# Adicionando uma coluna que informa o nome do usuário em caixa alta
df_customers['Names_upper'] = df_customers['Name'].str.upper()
df_customers

#%%
# Criando função para pegar somente o primeiro nome antes do separado indicado na função split '_'
def getFirst(name: str):
    return name.split('_')[0]

#%%
# Usando apply para a função ser executada em todas as linhas da coluna 'Name' e atribuindo os valores retornados
# para uma nova coluna
df_customers['First_name'] = df_customers['Name'].apply(getFirst)
df_customers

#%%
# Utilizando uma função lambda (uma função que não precisa ser declarada e terá um cálculo simples, como uma ArrowFunction, porém mais limitada)
df_customers['First_name'] = df_customers['Name'].apply(lambda x: x.upper().split('_')[0])
df_customers

#%%
# Criando uma função para retornar a classificação da quantidade de pontos
def pointsInterval(points: int):
    if points < 2500:
        return 'Baixo'
    elif points < 3500:
        return 'Médio'
    else:
        return 'Alto'

#%%
# Aplicando a função na coluna 'Points' com apply e atribuindo o retorno da função em uma coluna nova
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
# Criando uma função que calculará o RFV de cada cliente
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
# Aplicando a função no eixo X, ou seja, recebe uma linha para ser realizado o cálculo e dentro da função seleciona as colunas esperadas para realizar o cálculo
df_crm['RFV'] = df_crm.apply(rfv, axis=1)
df_crm