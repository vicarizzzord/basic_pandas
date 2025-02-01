#%%
import pandas as pd

data = {
    'Nome': ['Téo', 'Nah', 'Maria', 'Nah', 'Lara', 'Téo'],
    'Idade': [32, 33, 2, 33, 31, 32],
    'updated_at': [1, 2, 3, 1, 2, 3]
}

df = pd.DataFrame(data)

#%%
# Ordenando os valores para que sejam as ultimas transações realizadas pelo usuário, de forma decrescente e removendo
# os valores duplicados, mantendo os ultimos valores e atribuindo para o dataframe principal. Tudo dentro de um pipeline.
df = (df.sort_values(by='updated_at', ascending=False)
    .drop_duplicates(subset=['Nome', 'Idade'], keep='first'))
df
#%%

