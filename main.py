#Primeira coisa: fazer as importações

import pandas as pd
import matplotlib.pyplot as plt
import random

#Aqui a gente define um período de tempo, por exemplo, 30 dias
dias = pd.date_range(start="2024-01-01", periods=30)

#Precisamos gerar os dados fictícios que serão trabalhados
dados = {
  "Data": dias,
  "Curtidas": [random.randint(50, 500) for _ in range(30)],
  "Comentarios": [random.randint(10, 100) for _ in range(30)],
  "Compartilhamentos": [random.randint(5, 50) for _ in range(30)],
  "Visualizacoes": [random.randint(1000, 10000) for _ in range(30)]
}

df = pd.DataFrame(dados)
print(df.head()) #ou seja, exibe os primeiros dados 

#Agora precisamos criar um gráfico de linhas para visualizar a evolução das métricas ao longo de todos os dias
plt.figure(figsize=(12,6))

# Plot de cada métrica
plt.plot(df['Data'], df['Curtidas'], label='Curtidas', marker='o')
plt.plot(df['Data'], df['Comentarios'], label='Comentários', marker='o')
plt.plot(df['Data'], df['Compartilhamentos'], label='Compartilhamentos', marker='o')
plt.plot(df['Data'], df['Visualizacoes'], label='Visualizações', marker='o')

# Personalização do gráfico
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.title("Análise de Métricas de Redes Sociais ao Longo do Tempo")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculando o engajamento, tendo como base a média de visualizações
df['Engajamento'] = (df['Curtidas'] + df['Comentarios'] + df['Compartilhamentos']) / df['Visualizacoes']

# Exibindo o gráfico de engajamento ao longo dos dias
plt.figure(figsize=(10, 5))
plt.plot(df['Data'], df['Engajamento'], label='Engajamento', color='pink', marker='o')

plt.xlabel("Data")
plt.ylabel("Engajamento (%)")
plt.title("Taxa de Engajamento Diária")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Detectando dias com um engajamento alto, ou seja, acima de 10%
df['Pico_Engajamento'] = df['Engajamento'] > 0.1

# Filtrando e exibindo os dias com pico de engajamento
dias_pico = df[df['Pico_Engajamento']]
print("Os dias com Pico de Engajamento, foram:")
print(dias_pico[['Data', 'Engajamento']])

# Estatísticas básicas das visualizações
resumo_estatisticas = df[['Curtidas', 'Comentarios', 'Compartilhamentos', 'Visualizacoes', 'Engajamento']].describe()
print("Aqui está o Resumo Estatístico das Métricas:")
print(resumo_estatisticas)
