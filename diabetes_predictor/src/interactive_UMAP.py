import numpy as np
import umap
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import mplcursors

# Carregar dados do arquivo CSV
data = pd.read_csv("output_cluster.csv")

# Calcular o IMC
data['IMC'] = data['peso'] / ((data['altura'] / 100) ** 2)

# Selecionar variáveis relevantes
data = data[['IMC', 'diabetes', 'idade']]

# Definir a cor base
base_color = 'blue'

# Mapear as cores com transparência
color_map = mcolors.LinearSegmentedColormap.from_list('ColorMap', ['white', base_color])

# Obter o valor máximo do IMC para normalizar as cores
max_imc = data['IMC'].max()

# Calcular a transparência com base no IMC
alpha = data['IMC'] / max_imc

# Criar uma lista de cores
colors = ['red' if diabetes == 1 else color_map(a) for diabetes, a in zip(data['diabetes'], alpha)]

# Aplicar o algoritmo UMAP
reducer = umap.UMAP()
embedding = reducer.fit_transform(data)

# Plotar os pontos
scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=colors)

# Legenda
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='Diabetes Negativa'),
                   plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Diabetes Positiva')]

plt.legend(handles=legend_elements)

plt.xlabel('Componente 1 (UMAP)')
plt.ylabel('Componente 2 (UMAP)')
plt.title('Projeção UMAP')

# Create the interactive cursor
cursor = mplcursors.cursor(scatter, hover=True)

# Define the tooltip information
tooltip_labels = [
    f"IMC: {imc:.2f}\nDiabetes: {diabetes}\nIdade: {idade}"
    for imc, diabetes, idade in zip(data['IMC'], data['diabetes'], data['idade'])
]

# Add the tooltip annotations to the plot
cursor.connect("add", lambda sel: sel.annotation.set_text(tooltip_labels[sel.target.index]))

plt.show()
