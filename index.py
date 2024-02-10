import pandas as pd

# Criando um DataFrame simples
data = {
    'Nome': ['João', 'Ana', 'Pedro', 'Maria'],
    'Idade': [28, 34, 29, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Curitiba']
}
df = pd.DataFrame(data)
print(df)