# %%
import pandas as pd

#%%

ages = [30, 42, 90, 34]

mean = sum(ages)/len(ages)
std = 0
for i in ages:
    std += (mean - i)**2

var = std /(len(ages) - 1)
var

#%%
# Transformalção para séries pandas
ages_series = pd.Series(ages, name='idades')

ages_series
# %%
# Métodos da séries

# Média
ages_series.mean()

# Variância
ages_series.var()

# Desvio padrão
ages_series.std()

# Mediana
ages_series.median()

# Percentil
ages_series.quantile(0.25)

# Tabela para informar os valores dos métodos
ages_series.describe()

#%%
# Formato da series
ages_series.shape

#%%
# Acessando valor da series
ages_series[0]

#%%
# Alterando index da série (pouco utilizado)
ages_series.index = ['a', 'b', 'c', 'd']

# Acessando valor da series com o novo index
ages_series['b']

#%%

# iloc - Garante que o valor é acessado pela posição do valor nas séries

ages_series.iloc[0]

# loc - Garante que o valor é acessado pelo índice do valor nas series
ages_series.loc['c']

ages_series.name

