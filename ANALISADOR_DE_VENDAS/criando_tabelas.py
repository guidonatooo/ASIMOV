import pandas as pd

data = {
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Sobrenome': ['Silva', 'Souza', 'Oliveira'],
    'Idade': [28, 34, 22]}

df = pd.DataFrame(data, index=['pessoa1', 'pessoa2', 'pessoa3'])

df

print(df)

