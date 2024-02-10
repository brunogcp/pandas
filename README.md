<div align="center">
  <h3 align="center">Pandas</h3>
  <div>
  <a href="https://bgcp.vercel.app/article/1142549c-8841-4a1f-9743-3130271867b1">
  <img src="https://img.shields.io/badge/Download PDF (ENGLISH)-black?style=for-the-badge&logoColor=white&color=000000" alt="three.js" />
  </a>
  </div>
</div>

## 🚀 Introdução ao Pandas em Python

Pandas é uma biblioteca do Python que fornece estruturas de dados rápidas, flexíveis e expressivas, projetadas para tornar o trabalho com "dados relacionais" ou "dados rotulados" tanto fácil quanto intuitivo. Ideal para análise de dados, o Pandas permite uma manipulação de dados robusta e análise exploratória eficiente.

### 🌟 Principais Características:

- **📊 Manipulação de Dados**: Facilita operações de manipulação e limpeza de dados complexos.
- **🔍 Análise Exploratória**: Oferece funções para análise exploratória rápida e eficiente.
- **📈 Suporte a Diversos Formatos de Dados**: Lê e escreve dados em diferentes formatos como CSV, Excel, SQL databases, e HDF5.
- **🧮 Operações de Alto Nível**: Suporta agregações, fusões, e transformações de dados de forma simples.

## 🛠️ Instalação

Antes de começar, certifique-se de ter o Python e o pip instalados no seu sistema.

### Windows, Linux e macOS:

Para instalar o Pandas, abra o terminal e execute o seguinte comando:

```bash
pip install pandas
```

## 📊 Uso Básico

### Configuração Inicial:

Após a instalação, você pode começar a utilizar o Pandas importando a biblioteca em seu script Python.

```python
import pandas as pd
```

### Criando DataFrames:

Um DataFrame é uma estrutura de dados bidimensional com colunas de tipos potencialmente diferentes. Você pode pensar nele como uma planilha ou tabela SQL.

```python
# Criando um DataFrame simples
data = {
    'Nome': ['João', 'Ana', 'Pedro', 'Maria'],
    'Idade': [28, 34, 29, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Curitiba']
}
df = pd.DataFrame(data)
print(df)
```

### Lendo Dados:

Pandas suporta a leitura de dados de várias fontes como CSV, Excel entre outros.

```python
# Lendo dados de um arquivo CSV
df = pd.read_csv('caminho_para_seu_arquivo.csv')
```

### Explorando Dados:

Pandas oferece funções para uma rápida exploração dos dados.

```python
# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Resumo estatístico das colunas numéricas
print(df.describe())
```

### Manipulando Dados:

Com Pandas, manipular dados é intuitivo e eficaz.

```python
# Adicionando uma nova coluna
df['Ano'] = 2024

# Filtrando dados
df_filtrado = df[df['Idade'] > 30]

# Agrupando dados
df_grupo = df.groupby('Cidade')
```

## 📈 Pandas para Análise de Dados

### Teoria da Análise de Dados:

💡 A análise de dados com Pandas permite compreender melhor os dados, identificar padrões, tendências e fazer inferências.

### Prática com um Dataset Real:

Vamos analisar um conjunto de dados real sobre vendas.

1. **Leitura do Dataset**:
   
   Suponha que temos um arquivo `vendas.csv` com dados de vendas.

```python
vendas_df = pd.read_csv('vendas.csv')
```

2. **Análise Exploratória**:
   
   Explore os dados usando `head()`, `describe()`, e `info()` para obter um entendimento inicial.

3. **Limpeza de Dados**:
   
   Identifique e trate valores ausentes e duplicados.

4. **Visualização de Dados**:
   
   Utilize bibliotecas como Matplotlib ou Seaborn junto com Pandas para visualizar os dados e extrair insights.

```python
import matplotlib.pyplot as plt

vendas_df['TotalVendas'].plot(kind='hist')
plt.show()
```

### 🔍 Testes:

1. **Verificação de Tendências**:
   
   Analise as tendências de vendas ao longo do tempo.

2. **Identificação de Outliers**:
   
   Use gráficos de caixa (boxplots) para identificar outliers nos dados.

## 🏆 Conclusão

Neste tutorial, você mergulhou no mundo do Pandas, uma ferramenta essencial para análise de dados em Python. Combinando teoria e prática, você explorou desde a instalação e criação de DataFrames até a análise de um dataset real. O uso do Pandas para análise de dados ilustra como ele pode simplificar significativamente a manipulação de dados e a extração de insights valiosos.

Espero que este guia tenha sido útil e que você se sinta inspirado a utilizar o Pandas em seus próprios projetos de análise de dados. Continue explorando e, acima de tudo, divirta-se com a programação e análise de dados! 🐼📊