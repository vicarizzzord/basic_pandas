# %%
import pandas as pd

#%% [markdown]
# # Exercício 1
data = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
data_series = pd.Series(data)

#%% [markdown]
# Média
mean = data_series.mean()
mean

#%% [markdown]
# Desvio padrão
std = data_series.std()
std

#%% [markdown]
# Máximo valor
maximum = data_series.max()
maximum
# %% [markdown]
# # Exercício 2
data =  {'nome':['Téo', 'Nah', 'Napoleão'], 'idade': [31, 32, 14]}
data_df = pd.DataFrame(data)

#%%[markdown]
# Sumário
summary = data_df.describe()
summary

#%%[markdown]
# Média da coluna idade
age_mean = data_df['idade'].mean()
age_mean

#%%[markdown]
# Ultimo nome da coluna nome
last_name = data_df['nome'].tail(1)
last_name

#%%