#%%
import pandas as pd

#%% [markdown]
# # Exercício 1
df_homicide = pd.read_csv('../../data/ipea/homicidios.csv', sep=';')
df_homicide

#%% [markdown]
# ## Quantidade de linhas e colunas

#%%
df_homicide.shape

#%%[markdown]
# ## Nome da primeira coluna

#%%
df_homicide.columns[0]

#%% [markdown]
# ## Nome da última coluna

#%%
df_homicide.columns[-1]

#%% [markdown]
# # Exercício 2

#%%
df_black_woman_homicide = pd.read_csv('../../data/ipea/homicidios-mulheres-negras.csv', sep=';')
df_black_woman_homicide

#%%
df_black_woman_homicide.info(memory_usage='deep')

#%% [markdown]
# Colunas do tipo numérico: 3 - `cod`, `período`, `valor`
# Colunas do tipo 'object': 1 - `nome`

#%%

