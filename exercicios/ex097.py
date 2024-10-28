import pandas as pd
import matplotlib.pyplot as plt

# Carrega o dataset
df = pd.read_csv('csv/obitos-confirmados-covid-19.csv', sep=';')

# Função para calcular estatísticas de idade
def calcular_estatisticas_idade(df):
    media_idade = df['Idade'].mean()
    maior_idade = df['Idade'].max()
    menor_idade = df['Idade'].min()
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Maior idade: {maior_idade}")
    print(f"Menor idade (mais jovem): {menor_idade}")

# Função para plotar o número de mortes por cidade
def plotar_mortes_por_cidade(df, top_n=10):
    mortes_por_cidade = df['lugar'].value_counts().head(top_n)
    plt.figure(figsize=(10, 6))
    plt.bar(mortes_por_cidade.index, mortes_por_cidade.values)
    plt.title(f'Top {top_n} Cidades com Maior Número de Mortes')
    plt.xlabel('Cidade')
    plt.ylabel('Número de Mortes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Função para plotar a distribuição de comorbidades
def plotar_comorbidades(df, top_n=3):
    comorbidades = df['comorbidade'].value_counts().head(top_n)
    plt.pie(comorbidades, labels=comorbidades.index, autopct='%1.1f%%')
    plt.title('Distribuição de Comorbidades entre Mortes')
    plt.show()

# Função para plotar a distribuição de gênero
def plotar_distribuicao_genero(df):
    distribuicao_genero = df['Sexo'].value_counts()
    plt.pie(distribuicao_genero, labels=distribuicao_genero.index, autopct='%1.1f%%')
    plt.title('Distribuição por Gênero')
    plt.show()

# Função para plotar a distribuição por idade
def plotar_distribuicao_idade(df, top_n=93):
    distribuicao_idade = df['Idade'].value_counts().head(top_n)
    plt.figure(figsize=(12, 6))
    plt.bar(distribuicao_idade.index, distribuicao_idade.values)
    plt.title('Distribuição de Idade entre Óbitos')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.show()

# Função para plotar óbitos por mês
def plotar_obitos_por_mes(df, top_n=6):
    obitos_por_data = df['data'].value_counts().head(top_n)
    plt.figure(figsize=(10, 5))
    plt.bar(obitos_por_data.index, obitos_por_data.values)
    plt.title(f'Top {top_n} Meses com Maior Número de Óbitos')
    plt.xlabel('Data')
    plt.ylabel('Número de Óbitos')
    plt.xticks(rotation=45)
    plt.show()

# Chamada das funções
calcular_estatisticas_idade(df)
plotar_mortes_por_cidade(df)
plotar_comorbidades(df)
plotar_distribuicao_genero(df)
plotar_distribuicao_idade(df)
plotar_obitos_por_mes(df)