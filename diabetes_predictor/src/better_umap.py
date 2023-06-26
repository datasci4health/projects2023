import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import umap.umap_ as umap
import mplcursors

# Carregar o conjunto de dados
df = pd.read_csv('df_tratado.csv')

# Selecionar as colunas para o UMAP
umap_data = df[['pressão alta', 'imc', 'diabetes']]

# Mapear os valores da coluna 'pressão alta' para rótulos binários
labels_pressao_alta = {'sim': 1, 'não': 0}
umap_data['pressão alta'] = umap_data['pressão alta'].map(labels_pressao_alta)

# Converter as colunas para valores numéricos
umap_data['imc'] = pd.to_numeric(umap_data['imc'], errors='coerce').fillna(-1)

# Realizar a redução de dimensionalidade UMAP
reducer = umap.UMAP()
embedding = reducer.fit_transform(umap_data)

# Definir cores para o subplot esquerdo com base nos valores da coluna 'pressão alta'
cores_pressao_alta = np.where(umap_data['pressão alta'] == 1, 'red', 'blue')

# Definir cores para o subplot direito com base nos valores da coluna 'diabetes'
cores_diabetes = np.where(df['diabetes'] == 1, 'red', 'blue')

# Criar um mapa de cores em gradiente para o IMC
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(umap_data['imc'].min(), umap_data['imc'].max())
cores_imc = cmap(norm(umap_data['imc']))

# Criar a figura e os subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Plotar a incorporação UMAP com cores com base em 'pressão alta'
scatter1 = ax1.scatter(embedding[:, 0], embedding[:, 1], c=cores_pressao_alta, cmap='coolwarm', alpha=0.4)
ax1.set_title('Cores com Base em Pressão Alta')
ax1.set_xlabel('Dimensão UMAP 1')
ax1.set_ylabel('Dimensão UMAP 2')

legend_elements_1 = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='Pressão Alta Negativa'),
                   plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Pressão Alta Positiva')]

ax1.legend(handles=legend_elements_1)

# Plotar a incorporação UMAP com cores com base em 'diabetes'
scatter2 = ax2.scatter(embedding[:, 0], embedding[:, 1], c=cores_diabetes, cmap='coolwarm', alpha=0.4)
ax2.set_title('Cores com Base em Diabetes')
ax2.set_xlabel('Dimensão UMAP 1')
ax2.set_ylabel('Dimensão UMAP 2')

legend_elements_2 = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='Diabetes Negativa'),
                   plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Diabetes Positiva')]

ax2.legend(handles=legend_elements_2)

# Plotar a incorporação UMAP com cores em gradiente com base no IMC
scatter3 = ax3.scatter(embedding[:, 0], embedding[:, 1], c=umap_data['imc'], cmap='coolwarm', alpha=0.4)
ax3.set_title('Cores em Gradiente com Base no IMC')
ax3.set_xlabel('Dimensão UMAP 1')
ax3.set_ylabel('Dimensão UMAP 2')
cbar = plt.colorbar(scatter3, ax=ax3)
cbar.set_label('IMC')

# Criar o cursor para o subplot esquerdo
cursor1 = mplcursors.cursor(scatter1)

@cursor1.connect("add")
def on_add_pressao_alta(sel):
    index = sel.target.index
    x = sel.target[0]
    y = sel.target[1]
    label_pressao_alta = 'Sim' if umap_data.loc[index, 'pressão alta'] == 1 else 'Não'
    label_imc = umap_data.loc[index, 'imc']
    sel.annotation.set_text(f"Índice: {index}\nPressão Alta: {label_pressao_alta}\nIMC: {label_imc}")
    sel.annotation.set_position((x, y))

# Criar o cursor para o subplot direito
cursor2 = mplcursors.cursor(scatter2)

@cursor2.connect("add")
def on_add_diabetes(sel):
    index = sel.target.index
    x = sel.target[0]
    y = sel.target[1]
    label_diabetes = 'Positivo' if df.loc[index, 'diabetes'] == 1 else 'Negativo'
    sel.annotation.set_text(f"Índice: {index}\nDiabetes: {label_diabetes}")
    sel.annotation.set_position((x, y))

# Criar o cursor para o subplot do IMC
cursor3 = mplcursors.cursor(scatter3)

@cursor3.connect("add")
def on_add_imc(sel):
    index = sel.target.index
    x = sel.target[0]
    y = sel.target[1]
    label_imc = umap_data.loc[index, 'imc']
    sel.annotation.set_text(f"Índice: {index}\nIMC: {label_imc}")
    sel.annotation.set_position((x, y))

plt.tight_layout()
plt.show()
