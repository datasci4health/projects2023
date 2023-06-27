# Instruções de Instalação e Execução

Este diretório contém o código-fonte em Python do projeto `Análise de dados da hanseníase: uma abordagem preditiva para a saúde pública`. Siga as instruções abaixo para configurar o ambiente de desenvolvimento e executar o projeto.

## Pré-requisitos

- Boruta==0.3
- conda==23.3.1
- conda-build==3.24.0
- folium==0.14.0
- functools==3.10.9
- geopandas==0.13.0
- hyperopt==0.2.7
- imageio==2.26.0
- imbalanced-learn==0.10.1
- IPython==8.10.0
- lightgbm==3.3.5
- matplotlib==3.6.3
- numpy==1.23.5
- pandas==2.0.2
- pandas-profiling==3.6.6
- python==3.10.9
- scikit-learn==1.2.1
- scipy==1.9.3
- seaborn==0.12.2
- sklearn-genetic==0.5.1
- xgboost==1.7.6
- ydata-profiling==4.1.2

Certifique-se de ter os pré-requisitos instalados.

## Instalação

1. Clone este repositório em sua máquina local:

   `git clone https://github.com/seu-usuario/datasci4health/projects2023.git`

2. Navegue até o diretório src:

    `cd src`

3. Instale as dependências do projeto:

    `pip install -r requirements.txt`


## Execução
Para executar o projeto, siga as etapas abaixo:

1. Inicialize o jupyter notebook

    `jupyter notebook`

2. No navegador, você verá a lista de arquivos e diretórios no seu projeto. Clique em um notebook (.ipynb) para abri-lo.

3. Dentro do notebook, você pode executar as células de código individualmente pressionando Shift + Enter ou executar todas as células de uma vez usando a opção "Run All" no menu "Cell".


## Contribuição
Se você deseja contribuir com este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.

2. Crie um branch para sua nova feature ou correção de bug:

    `git checkout -b minha-nova-feature`

3. Faça as alterações desejadas e adicione-as ao stage:

    `git add .`

4. Faça o commit das suas alterações:

    `git commit -m "Descrição das alterações"`

5. Envie suas alterações para o branch remoto:

    `git push origin minha-nova-feature`

6. Abra um pull request neste repositório.