## Instruções básicas de instalação/execução

Para execução dos códigos armazenados nesta seção, é necessário a instalação de pacotes de Python descritos no arquivo **requirements.txt**. 

De forma a facilitar a instalação de todos os pacotes usados, disponibilizou-se o script em Shell **install-requirements.sh**. Execute-o em um prompt/terminal.

Todo o fluxo do trabalho esta contido na pasta notebooks **pns_prepocessing.ipynb** faz o preprocessamanto da base de dados PNS 2019, extraindo as colunas de interesse, substituindo valores ignorados (normalmente 9 ou 99) por nulo e selecinando as amostras de interesse (resposta do PHQ9 ou Q092).

Abaixo temos um resumo de cada arquivo notebook:

- **pns_prepocessing.ipynb**: notebook com worflow de preprocessamento do banco PNS

- **pns_hello_world.ipynb**: notebook com testes/experimentos diversos da PNS

- **pns_data_description.ipynb**: notebook com descritivos selecionados que o grupo achou interessente sobre a base de dados PNS

- **pns_data_analysis.ipynb** e **pns_chi_stats.ipynb**: notebook com graficos para análises, análise estratificada, e testes estatisticos.

- **pns_depression_models.ipynb**: notebook com análises de técnicas supervisionadas para predição de depressão

- **pense_preprocessing.ipynb** e **pense_hello_world.ipynb**: experimentos com a base PENSE (abadonada pelo grupo).
