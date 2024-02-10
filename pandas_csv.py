import pandas as pd

df = pd.read_csv('teste.csv')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Resumo estatístico das colunas numéricas
print(df.describe())

# Adicionando uma nova coluna
df['Ano'] = 2024

# Filtrando dados
df_filtrado = df[df['Idade'] > 30]

# Agrupando dados
df_grupo = df.groupby('Cidade')