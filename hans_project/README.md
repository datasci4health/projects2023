# Projeto `Análise de dados da hanseníase: uma abordagem preditiva para a saúde pública`

# Project `Data analysis of leprosy: a predictive approach for public health`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp, pelos membros:

> |Nome  | RA | Especialização|
> |--|--|--|
> | Alexsandro Ferreira de Barros Júnior  | 233768  | Computação - Líder Github - [Conta GitHub](https://github.com/alexbjr) |
> | Giovanna Gennari Jungklaus  | 198010  | Computação - [Conta GitHub](https://github.com/gigennari)|
> | José Ernesto Stelzer Monar  | 139553  | Computação - [Conta GitHub](https://github.com/stelzer-monar)|
> | Maria Clara Castro Higino de Sousa  | 243237  | Computação - [Conta GitHub](https://github.com/mc-castro)|
> | Miriam Reyes Ortiz  | 265762  | Saúde - [Conta GitHub](https://github.com/MiriamOrtiz)|

## Slides da Apresentação Final
> [Link para slides da apresentação final do projeto.](https://drive.google.com/drive/u/0/folders/1ONifW78BgF5WkyN1RAxTKtahgnp-F7Fk)

# Introdução e Referenciais Teóricos
> A hanseníase é uma doença infecciosa crônica e transmissível que afeta principalmente a pele e o sistema nervoso periférico. Os agentes causadores da enfermidade são as bactérias Mycobacterium leprae e Mycobacterium lepromatosis (Ploemacher et al. 2019). A doença pode afetar pessoas de qualquer sexo ou faixa etária, sua evolução é lenta e progressiva, e se não for tratada na fase inicial, pode levar a incapacidades físicas. A infecção está inserida no grupo de doenças tropicais negligenciadas e continua sendo um problema de saúde pública em muitos países, incluindo o Brasil. Embora a tendência de novos casos tenha diminuído ao longo do tempo devido ao tratamento com terapia multidrogas, o Brasil ocupa atualmente o segundo lugar em termos de prevalência no mundo (WHO, 2023).
> 
> O esquema de tratamento (número de doses e tempo) é padronizado e depende da classificação operacional da doença baseada no número de lesões cutâneas. Os casos são classificados como paucibacilares (PB, até cinco lesões) ou multibacilares (MB, seis ou mais lesões de pele), com uma duração de tratamento de 6 a 12 meses, respectivamente. Se o tratamento é realizado de forma completa e correta, a transmissão da doença é interrompida, impedindo que outras pessoas sejam infectadas, e o paciente é curado (Minestério da saúde 2022, 2017). Apesar dos avanços no tratamento para a cura da doença, o abandono da terapia multidrogas ainda representa um dos obstáculos para o controle efetivo e a eliminação da hanseníase. Por exemplo, os casos de abandono podem resultar em curas incompletas, levando a uma maior progressão da doença, o que pode prolongar o tempo de tratamento e aumentar os custos para o sistema de saúde, além de manter fontes persistentes de infecção na área geográfica (Girão et al. 2013).
> 
> Evidências sugerem que existem fatores associados ao risco de abandono do tratamento da hanseníase (de Andrade et al. 2019; Nery et al. 2019). A interrupção do tratamento pode ser influenciada por características pessoais, socioeconômicas e fatores clínicos ou médicos (Girão et al. 2013). 
>
> Nesse contexto, este projeto tem como objetivo analisar os casos novos de hanseníase no período de 2009 a 2019, a fim de determinar padrões ou relações entre as características dos pacientes e da doença com os casos de cura e abandono do tratamento. Além disso, pretende-se identificar diferentes padrões espaciais de ocorrência e abandono, levando em consideração o índice de desenvolvimento humano. Para isso, serão utilizadas técnicas de machine learning para identificar as variáveis mais relevantes e sua relação com os casos de cura e abandono do tratamento.
> 
> Espera-se que os resultados deste projeto possam ajudar na identificação de fatores que representam barreiras no tratamento e visualizar as regiões vulneráveis para uma alocação adequada dos serviços. Além disso, a análise desses dados pode fornecer insights importantes sobre a doença, contribuindo para a prevenção e o controle efetivo da hanseníase em nível nacional.
> 
> 
> [Vídeo de apresentação](https://drive.google.com/file/d/1LdYcPP0i0cjiHvt-HNTh64a2jiKPNRNR/view?usp=sharing)

# Perguntas de Pesquisa
> Quais variáveis clínicas e epidemiológicas estão associadas ao tempo de cura dos pacientes com hanseníase?
> 
> Quais variáveis clínicas e epidemiológicas estão associadas ao tipo de saída do tratamento (cura ou abandono)?
> 
> Existe uma relação espacial entre o índice de desenvolvimento humano com a incidência (número de casos novos) e os casos de abandono do tratamento da doença?
> 
> Como as percepções obtidas a partir da análise de dados podem ser utilizadas para melhorar o planejamento financeiro dos sistemas de saúde em relação ao tratamento da hanseníase?*
> 
> Qual é o desempenho dos modelos de machine learning na previsão do tipo de saída do tratamento (cura ou abandono) dos pacientes com hanseníase?

# Objetivos
## Geral
> Predizer o tipo de desfecho dos casos de hanseníase (cura ou abandono do tratamento) para auxiliar no planejamento financeiro da saúde pública.

## Específicos
> Coletar e organizar os dados relacionados aos casos de hanseníase no período de 2009 a 2019.
> 
> Realizar uma análise descritiva dos dados, identificando características demográficas e clínicas dos pacientes.
> 
> Identificar os fatores associados ao abandono do tratamento da hanseníase, considerando variáveis pessoais, socioeconômicas e clínicas.
> 
> Utilizar técnicas de machine learning para identificar as variáveis mais relevantes na predição dos casos de cura e abandono do tratamento.
> 
> Realizar análises espaciais para identificar padrões de ocorrência e abandono da hanseníase em diferentes regiões.
> 
> Avaliar a relação entre o índice de desenvolvimento humano e os casos de cura e abandono do tratamento da hanseníase.


# Metodologia
>
> * Seleção e tratamento dos dados
> 
> Os dados foram obtidos do Sistema de Informação de Agravos de Notificação (SINAN) no período de 2009 a 2019. Os dados foram pré-processados considerando apenas os casos novos notificados a cada ano. Um caso novo é a pessoa que nunca recebeu qualquer tratamento específico para a doença. Verificou-se que os casos novos eram residentes do Brasil no momento da notificação e não houve duplicatas. 
Considerando as características da doença e a variação das variáveis fornecidas no banco de dados, foi realizada uma análise exploratória para identificar e selecionar features que mostram relação com a cura e o abandono do tratamento (ver report). 
> A alta por cura implica que o tratamento foi concluído (6 ou doze meses de acordo com a classificação operacional), juntamente com a avaliação médica, o que resulta na saída do paciente do registro ativo no SINAN. Os casos de abandono do tratamento são aqueles em que os pacientes não conseguem completar o tratamento dentro do prazo máximo permitido (mais de três ou seis meses consecutivos, se forem paucibacilares e multibacilares, respectivamente), apesar de repetidas tentativas de retorno e acompanhamento do tratamento.
>
> * Análise descritiva
> 
> A partir desse subconjunto de dados, foi realizada um análise descritiva dos casos novos, dos casos de cura e dos casos de abandono de tratamento, estratificada por sexo, faixa etária, classificação operacional e outras variáveis clínicas dos pacientes. Além disso, determinou-se a correlação das variáveis com os desfechos da doença.

>
> * Análise espacial
> 
> Para identificar padrões espaciais de ocorrência e abandono, determinou-se a proporção de casos de hanseníase em abandono de tratamento entre os casos novos diagnosticados nos anos das cortes como um indicador para avaliar a qualidade da atenção e do acompanhamento dos casos novos diagnosticados até a conclusão do tratamento. Para o cálculo desse indicador, utilizaram-se os casos novos de hanseníase diagnosticados nos anos das coortes que abandonaram o tratamento até 31/12 do ano de avaliação, dividido pelo total de casos novos diagnosticados nos anos das coortes, multiplicado por 100. O qualidade de atenção pode ser classificada como Boa quando o indicador é inferior a 10%, Regular quando está entre 10% e 24,9% e Precária quando é igual ou superior a 25%. Para esse indicador foi utilizado o município e a unidade federativa de residência atual dos casos notificados, excluindo aqueles com a classificação de "erro de diagnóstico” no banco de dados. Com base nos parâmetros obtidos, foram criados mapas temáticos para cada ano.
> 

> ![Figura 1. Mapa da metodologia executada](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/reports/metodologia.png)*Mapa da metodologia executada*

## Bases de Dados e Evolução
> Bases de dados estudadas e/ou utilizadas no projeto.

### Base de dados de casos de hansenníase 

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Sistema de Informação de Agravos de Notificação (SINAN) | http://portalsinan.saude.gov.br/hanseniase | Banco de dados nacional alimentado pela notificação e investigação de casos de doenças e agravos gerados pelo Sistema de Vigilância Epidemiológica a nível municipal, estadual e nacional.
 
 #### Dicionário

 Aqui [link](https://github.com/alexbjr/hans_project/blob/main/hans_project/data/raw/dicionario_dados.xlsx) é possível encontrar o dicionário de dados.
 
> * MODOS DE ENTRADA
> 
> Caso novo: corresponde ao caso de hanseníase que nunca recebeu qualquer tratamento específico.
> 
> Outros reingressos: quando o paciente recebeu algum tipo de saída que não fosse cura, exemplo abandono, e retorna requerendo tratamento específico para hanseníase, a exceção de recidiva.
> 
> Outras entradas possíveis são transferência do mesmo município(outra unidade), transferência de outro município (mesma unidade da Federação – UF), transferência de outro estado, transferência de outro país.
> 
> Recidiva: pacientes que receberam alta por cura depois de serem tratados adequadamente com o esquema multidrogas e saíram do registro ativo do SINAN e que após o período de cura (geralmente superior a cinco anos)voltaram a apresentar novos sinais e sintomas clínicos da doença. Esses casos são notificados no modo de entrada ao sistema como “recidiva”.
> 
> 
> * DADOS CLÍNICOS / EPIDEMIOLÓGICOS
> 
> Reações hansênicas: alterações do sistema imunológico que se manifestam como inflamações agudas ou subagudas e que podem ocorrer antes do diagnóstico, durante ou depois do tratamento (associado aos medicamentos suministrados).
> 
> Classificação operacional baseado no número de lesões cutâneas (WHO):
> 
>>>> Paucibacilar (PB)

>>>> Multibacilar (MB)
>
> Formas clínicas: Classificação segundo Madri 1953.
> 
>>>> Hanseníase indeterminada (HI) tipo PB

>>>> Hanseníase tuberculóide (HT) tipo PB

>>>> Hanseníase dimorfa (HD) tipo MB

>>>> Hanseníase virchowiana (HV) tipo MB
>
> Tratamento - esquemas terapêuticos. Série de medicamentos diários e mensais dependendo da classificação operacional padronizada pela Organização Mundial da Saúde(OMS). O tratamento é com poliquimioterapia (PQT).
> 
> Casos novos em faixa etária menor de 15 anos: A ocorrência de casos novos nesta faixa etária indica focos de transmissão ativa, importante sinalizador para o monitoramento da doença.
> 
> Grau de Incapacidade Física (GIF): Indica a perda da sensibilidade protetora e/ou deformidade visível em consequência de lesão neural e/ou cegueira. 
>
> Casos notificados com GIF=2 (de maior avanço) evidenciam diagnóstico tardio, devido ao maior grau de comprometimento físico ocasionado pela hanseníase.
>
>
> * MODOS DE SAÍDA
>
> Alta por cura: implica que o tratamento foi concluído (6 ou doze meses de acordo com a classificação operacional), junto com avaliação médica (neurológica, grau de incapacidade e orientação para os cuidados) o que leva a saída do paciente do registro ativo no SINAN.
> 
> Abandono do tratamento: é aquele onde o paciente não consegue completar o tratamento dentro do prazo máximo permitido (mais de três ou seis meses consecutivos, se são paucibacilares e multibacilares, respectivamente), apesar de repetidas tentativas para o retorno e seguimento do tratamento.
> 
> Outros encerramentos possíveis são transferência para o mesmo município, para outro município, estado ou país, óbito por hanseníase ou por outra causa como erro diagnóstico.
> 
> 
> * INDICADORES
> 
> Os indicadores de saúde permitem a comparação entre diferentes áreas ou momentos e fornecem subsídios ao planejamento das ações de saúde. Existem dois grupos de indicadores para o monitoramento da hanseníase: 
>
> i) indicadores de monitoramento do progresso da eliminação da hanseníase enquanto problema de saúde pública - medem a magnitude e transcendência do problema de saúde pública. A situação é verificada na população ou no meio ambiente em um determinado período de tempo.
> ii) indicadores para avaliar a qualidade dos serviços da doença - medem o trabalho realizado (qualidade e/ou quantidade). Proporção de casos de hanseníase em abandono de tratamento entre os casos novos diagnosticados nos anos das cortes.

#### Filtros e transformações 

> Foram feitos filtros na base para remoção de duplicadas, para selecionar apenas casos do Brasil, apenas novos casos registrados no sistema (exclui reincidente) e apenas os casos com desfecho: cura, óbito ou abandono. Em seguida, foi realizada a mudança do tipo de algumas colunas que estavam caracterizadas como numéricas, mas representavam uma categoria. Depois, foram removidas todas as features com baixa variação de dados e alta cardinalidade. Outras colunas foram removidas sob o critério de não serem relevantes para o problema estudado. Por fim, foi feito um corte temporal para analisar apenas os casos de 2009 a 2019.


> Para Análise Exploratória dessa base foram analisados a quantidade de casos registrados em cada estado ao longo dos anos com o objetivo de entender se existia alguma região em que a doença predominou e se essa proporção foi reduzindo ou aumentando com o passar de uma década. Além disso, foi analisada a gravidade desses casos registrados, para entender onde há a presença de casos mais graves. Em seguida foram analisadas duas variaáveis (tempo de cura e tipo de saída do tratamento), para cada uma foi calculada a correlação com outras variáveis a fim de entender como se comportavam com outras variáveis. Por fim, foi iniciado testes de ML para analisar a acurácia do modelo em prever se o paciente abandonará o tratamento ou seguirá até o fim.

### Base de dados sobre dados geográficos 

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Atlas Brasil | http://www.atlasbrasil.org.br/consulta/planilha | O Atlas Brasil é um projeto que reúne informações socioeconômicas e demográficas sobre o Brasil. Ele oferece uma ampla gama de indicadores e dados estatísticos que abrangem diversos aspectos do país, permitindo análises e comparações em diferentes níveis geográficos.

Constitui em um site de consulta onde seleciona-se quais indicadores (educação, desenvolvimento humano, renda, etc) e quais territorialidade deseja acessar. Nessse caso, foi selecionado apenas o IDH por estado ao longo dos anos.
> 
> O banco oferece uma ampla gama de indicadores e dados estatísticos que abrangem diversos aspectos do país, permitindo análises e comparações em diferentes níveis geográficos.
> 
#### Filtros e transformações 
> 
> Não foi encontrado dados para o IDH de 2009 e 2011 e portanto, para estes anos, foram considerados os mesmos valores de 2010. Foi necessário remover o texto 'IDHM' das colunas, restando apenas o ano ao qual aqueles valores se referem. Foi removido os dados sobre o IDH do país, deixando apenas os dos estados. Além disso, foi substituído o nome dos estados por suas siglas. Por fim, foi adaptado o formato da tabela para conter apenas três colunas (UF, NU_ANO, IDH).

> Foi feita uma análise de correlação do IDH com a quantidade de casos novos nos estados em cada ano, indicando uma correlação negativa, mas muito baixa (0.28)

# Integração entre Bases e Análise Exploratória

## Análise de casos por faixa etária 
> O maior número de casos novos diagnosticados esteve concentrado em pacientes com idades entre 40 e 69 anos, sendo maior na faixa etária de 40 a 49 anos. Por outro lado, a maior  proporção de pacientes que abandonaram o tratamento ocorreu entre os 20 e 49 anos de idade, destacando-se aqueles com idades entre 20 a 29 anos (Figura 1).
>  
> ![Figura 2. Número de casos novos diagnosticados e abandonos do tratamento por faixa etária a cada 10 anos no período de 2009 a 2019 no Brasil](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_idade.png)
> 
> *Figura 2. Número de casos novos diagnosticados e abandonos do tratamento por faixa etária a cada 10 anos no período de 2009 a 2019 no Brasil*]
> 
## Análise do abandono por ano e sexo 
> Em todo o periódo analisado, o sexo masculino apresenta o maior número de casos novos diagnosticados e de abandono do tratamento em comparação com o sexo feminino. Observa-se uma tendência decrescente nos casos novos ao longo dos anos, com uma queda em 2016 e 2017. No entanto, os casos de abandono do tratamento em ambos os sexos mantiveram uma tendência similar. Durante o ano de 2019, a proporção de pacientes que abandonaram o tratamento foi maior para ambos os sexos. Por outro lado, os anos 2010 e 2011 apresentaram proporções menores de abandono (Figura 2).
> 
> ![Figura 3. Número de casos novos e de abandono do tratamento estratificado por sexo e ano no período de 2009 a 2019 no Brasil. F:feminino, M:masculino](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_sexo.png)
> 
> *Figura 3. Número de casos novos e de abandono do tratamento estratificado por sexo e ano no período de 2009 a 2019 no Brasil. F:feminino, M:masculino*
> 
## Análise espacial de casos novos por unidade federativa e ano
> As bases foram unidas por sigla do estado (UF) e por ano (NU_ANO), dessa forma, foi obtido uma tabela com quatro colunas (UF, NU_ANO, IDH, N_CASOS) e a partir disso foi possível analisar a correlação entre o IDH e a quantidade de casos em cada estado.
> 
> Geograficamente, todas as unidades federativas relataram novos casos de hanseníase no período de 2009 a 2019. Os estados com o maior número de casos novos foram o Maranhão (MA, n=36.401), o Pará (PA, n=30.764) e o Mato Grosso (MT, n=30.068). Por outro lado, Roraima (RR, n=1.034) e Rio Grande do Sul (RS, n=1.184) apresentaram a menor número de casos (Figura 3).
> 
> ![Figura 4. Número de casos novos por unidade federativa por ano no Brasil, no período de 2009 a 2019](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos.gif)
> 
> *Figura 4. Número de casos novos por unidade federativa por ano no Brasil, no período de 2009 a 2019*
> 
## Análise espacial de casos de abandono do tratamento por unidade federativa e ano
> Do total de casos novos diagnosticados no período de 2009 a 2019 (n=309.555), 6.023% abandonaram o esquema de tratamento (n=18.644). No entanto, a proporção de abandono variou entre as unidades federativas ao longo dos anos. Por exemplo, os estados do Amapá (AP), Pará (PA), Roraima (RR), Mato Grosso (MT), Mato Grosso do Sul (MS), Amazonas (AM) e Pernambuco (PE), apresentaram maiores proporções de abandono em algum momento do período analisado (Figura 4). A proporção de casos de hanseníase em abandono de tratamento entre os casos novos diagnosticados por ano é uma forma de avaliar a qualidade dos serviços da doença em cada unidade federativa. As diferenças observadas podem indicar uma má qualidade dos serviços médicos prestados, bem como a persistência de fontes de infecção da doença nessas áreas. 
> 
> ![Figura 5. Proporção de casos que abandonaram o tratamento de hanseníase em relação ao número de casos novos estratificados por unidade federativa e ano no período de 2009 a 2019 no Brasil](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_uf.gif)
> 
> *Figura 5. Proporção de casos que abandonaram o tratamento de hanseníase em relação ao número de casos novos estratificados por unidade federativa e ano no período de 2009 a 2019 no Brasil*

## Análise da correlação entre o IDH dos estados 
> Sendo o IDH uma medida de referência em saúde, educação  e renda, foi feita sua correlação com a contagem de casos e porcentagem de abandono nos anos de 2009 a 2019 em cada estado e o valor do IDH do respectivo estado. Resultando numa correlação de -0.28 para a quantidade de casos e 0.0091 para o abandono, o que não indica uma relação muito forte para essa influência.
> 
> ![Figura 6. Número de casos novos em um estado versus o IDH do respectivo estado no período de 2009 a 2019 no Brasil, colorização por estado.](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_caso_idh_uf_hue.png)
> 
> *Figura 6. Número de casos novos em um estado versus o IDH do respectivo estado no período de 2009 a 2019 no Brasil, colorização por estado.*
> 
> ![Figura 7. Porcentagem de abandono em um estado versus o IDH do respectivo estado no período de 2009 a 2019 no Brasil, colorização por estado.](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_idh_uf_hue.png)
> 
> *Figura 7. Porcentagem de abandono em um estado versus o IDH do respectivo estado no período de 2009 a 2019 no Brasil, colorização por estado.*

## Análise estatísitca de tempo de cura e correlação entre variáveis da base de dados sobre hanseníase 
>Com o intuito de pensar na pergunta sobre o planejamento financeira de hospitais para o tratamento de hanseníase, fizemos uma distribuição normal do tempo de cura a partir da nova coluna "DURACAO_TRAT" criada a partir da data de saída e data de diagnóstico. A análise indicou uma média de 360.23 dias com um desvio padrão de 192.40 dias. Isso condiz com a análise médica que diz que o tratamento dura de 6 a 18 meses. 

>Já a respeito da correlação do tempo de cura com as demais variáveis, as maiores correlações, apesar de baixas, foram 

>| Parâmetros                                                                   | Correlação |
>|------------------------------------------------------------------------------|------------|
>| Duração Tratamento (DURACAO_TRAT) X Classificação Operacional (CLASSOPERA)   | 0.4614     |
>| Duração Tratamento (DURACAO_TRAT) X Forma Clínica da Doença (FORMACLINI)     | 0.3662     |
>| Duração do Tratamento (DURACAO_TRAT) X Número de Lesões (NU_LESOES)          | 0.2109     |

## Análises de ML para predição do desfecho

> Foi feito um comparativo com alguns algoritmos considerando as váriaveis disponíveis para predizer o tipo de alta do paciente. Para isso, foram utilizados os modelos de regressão logística, random forest, xgboost e lightgbm.
>
> Visando obter a melhor perfomance de cada modelo, foi utilizada uma otimização de hiperparâmetros de modo a automatizar e simplificar o processo de ajuste de hiperparâmetros. Para tal, foi utilizado uma abordagem de busca em espaço com base em algoritmos de otimização sequencial para encontrar a combinação ideal de hiperparâmetros que maximize a métrica de desempenho f1-score.
>
> Foi escolhido o f1-score devido ao desequilíbrio significativo entre as classes (cura e abandono). Ele combina a precisão (precision) e o recall, fornecendo uma medida única que considera tanto os verdadeiros positivos quanto os falsos positivos e falsos negativos. Dessa forma, se torna uma ótima métrica de otimização para o problema abordado. 
>
> O treinamento dos modelos foi feito utilizando pipelines com o objetivo de manter a organização, reprodutibilidade, eficiência, escalabilidade e prevenção de vazamento de dados. A estrutura adotada foi:

~~~python
num_transformer = FeatureUnion(    
    [
        ('num_pipe', Pipeline(
            [
                ('norm', StandardScaler()),
                ('nan_input', SimpleImputer())
            ]
        )),
        ('nan_flag', MissingIndicator(error_on_new=False))
    ]
)

feat_transformer = ColumnTransformer(
    [
        ('num_trans', num_transformer, num_feats),
        ('cat_trans', OneHotEncoder(handle_unknown='ignore'), cat_feats)    
    ],
    remainder='passthrough', sparse_threshold=0
)
~~~
~~~python
xgb_pipe = Pipeline(
[
    ('feat_trans', feat_transformer),
    ('over', SMOTE()),
    ('xgb', xgb.XGBClassifier())
]
)
~~~

> É possível perceber um pipeline de transformação de features numéricas e categóricas. Para as numéricas, foi realizada a normalização das variáveis usando o StandardScaler() que padroniza os valores das variáveis para terem média zero e desvio padrão igual a um. Além disso, usando o SimpleImputer(), os valores ausentes foram substituídos pela média ou mediana dos valores existentes.
>
> Para as categóricas, foi utilizado o OneHotEncoder, que utiliza a ColumnTransformer para aplicar transformações específicas a colunas específicas do conjunto de dados.
>
> Além disso, no pipeline de definição do modelo, foi utilizado o Smote como uma técnica para lidar com o desbalaceamento da base.

# Ferramentas
> O projeto será realizado em Python e serão utilizadas a seguintes ferramentas e bibliotecas:
>
> |Ferramenta/Biblioteca | Descrição|
> |--|--|
> |[Pandas](https://pandas.pydata.org/) |Biblioteca para manipulação e análise de dados| 
> |[Numpy](https://numpy.org/) |Biblioteca para cálculos matemáticos e estatísticos| 
> |[Scikit-learn](https://scikit-learn.org/stable/) |Biblioteca para modelagem preditiva e aprendizado de máquina| 
> |[Matplotlib](https://matplotlib.org/) e [Seaborn](https://seaborn.pydata.org/) |Bibliotecas para visualização de dados| 
> |[Pandas Profiling](https://pypi.org/project/pandas-profiling/) |Biblioteca para geração de relatório descritivo de um conjunto de dados| 
> |[Geopandas](https://geopandas.org/en/stable/) |Biblioteca de visualização para plotar dados geoespaciais em mapas| 
> |[Folium](https://pypi.org/project/folium/) |Biblioteca para visualização de dados geográficos interativos| 
> |[Imageio](https://pypi.org/project/imageio/) |Biblioteca Python para ler e escrever uma ampla gama de formatos de imagem, vídeo e áudio|
> |[Jupyter Notebook](https://jupyter.org/) |Ferramenta para desenvolvimento e apresentação de notebooks interativos| 
> |[Hyperopt](http://hyperopt.github.io/hyperopt/) |Bibilioteca para otimização dos hiperparâmetros de modelos de ML| 


# Resultados
## Evolução da quantidade de casos por estado
> Foi analisado um gráfico para entender a evolução dos casos de hanseníase ao longo dos anos. Os dados foram normalizados para a quantidade de habitantes em cada estado.
>
> ![Figura 8. Quantidade de casos a cada 100 mil habitantes por estado ao longo dos anos](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_por_100k.gif)
> 
> *Figura 8.Quantidade de casos a cada 100 mil habitantes por estado ao longo dos anos.*
>
## Análise de casos de abandono por estado
> Foi analisada a proporção de casos que abandonaram o tratamento de hanseníase em relação ao número de casos novos estratificados por município e ano no período de 2009 a 2019 no Brasil.
>
> ![Figura 9. Porcentagem de casos de abandono em relação ao número de diagnósticos por estado ao longo dos anos](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_uf.gif)
> 
> *Figura 9. Porcentagem de casos de abandono em relação ao número de diagnósticos por estado ao longo dos anos.*
> 
## Modelagem de ML
>A tabela abaixo contém o resultado comparativo entre os modelos de regressão logística, random forest, xgboost e lightgbm para a predição do desfecho da doença: cura ou abandono.
>
>Tabela 1 - Resultados para classificação em cura (classe 1) e abandono (classe 0) utilizando modelos de aprendizado de máquina
>| Modelo               | Acurácia | Precisão <br> da classe 0 | Precisão <br> da classe 1 | Revocação <br> da classe 0 | Revocação <br> da classe 1 | F1 score <br> da classe 0 | F1 score <br> da classe 1 |
>|----------------------|----------|----------|----------|----------|----------|----------|----------|
>| Logistic Regression  | 0.92     | 0.42     | 0.98     | 0.82     | 0.93     | 0.56     | 0.96     |
>| Random Forest        | 0.95     | 0.63     | 0.97     | 0.54     | 0.98     | 0.58     | 0.97     |
>| XGBoost              | 0.96     | 0.68     | 0.98     | 0.65     | 0.98     | 0.66     | 0.98     |
>| LightGBM             | 0.96     | 0.71     | 0.98     | 0.62     | 0.98     | 0.66     | 0.98     |
>
>A combinação de hiperparâmetros que resultou nesses valores para o XGBoost estão na Tabela 2:
>
>Tabela 2 - Hiperparâmetros do modelo escolhido 
>| Hiperparâmetro       | Valor               |
>|----------------------|---------------------|
>| colsample_bytree     | 0.9664002609854957  |
>| gamma                | 5.30286290577693    |
>| max_depth            | 7                   |
>| min_child_weight     | 1.0                 |
>| n_estimators         | 180                 |
>| reg_alpha            | 80.0                |
>| reg_lambda           | 0.4117635792177079  |

# Discussão
> Com base na análise dos resultados da Tabela 1, considerando todas as métricas avaliadas, podemos concluir que os modelos Random Forest, XGBoost e LightGBM apresentam desempenhos semelhantes e superiores à Logistic Regression. Esses modelos têm valores mais altos de precisão, revocação e F1 Score para a classe 0, o que indica que são capazes de lidar melhor com a identificação correta das instâncias negativas. 
>
> Além disso, eles têm resultados consistentemente mais altos para a classe 1 em todas as métricas. Isso se deve ao fato do banco de dados ser desbalanceado, possuindo uma representação majoritária da classe 1 (cura) em comparação com a classe 0 (abandono). Esse desequilíbrio pode levar o modelo a ter uma tendência a favorecer a classe majoritária, resultando em um viés na classificação. Foram adotadas algumas técnicas como *oversampling*, *undersampling* e *smote* para corrigir o desbalanceamento, que melhoraram o desempenho, mas não foram suficientes para remover totalmente o viés dos dados. 
>
> Portanto, com base nos resultados apresentados, o modelo escolhido foi o XGBoost que mostrou uma precisão de 0.68 para a classe 0, o que significa que 68% dos desfechos classificados como abandono foram corretamente identificados. A revocação de 0.65 indica que 65% dos pacientes que realmente abandonaram o tratamento foram corretamente identificados. O f1-score, que combina precisão e revocação, foi de 0.66, e a acurácia geral foi de 0.96. Apesar de terem sido obtidas métricas similares ao LightGBM, o XGBoost manteve uma maior constância entre revocação e precisão. 

# Conclusão
> Esse trabalho apresentou a aplicabilidade da Inteligência Artificial para auxiliar no planejamento financeiro da saúde pública, sendo capaz de classificar o tipo de desfecho do caso do paciente em cua ou abandono. Sendo capaz de fazer esse tipo de predição, é possível estimar um maior investimento destinado ao paciente que abandona o tratamento, pois eventualmente ele irá retornar em um nível mais avançado da doença.
>
> A metodologia apresentou a utilização de várias técnicas para a análise dos dados, buscando relação entre as variáveis e o tipo de desfecho. Utilizou também quatro modelos distintos para comparar desempenho e escolher o que tivesse melhor desempenho, utilizando para todos o método k-fold cross validation e otimização de hiperparâmetros.
>
> As análises realizadas mostraram que não é possível afirmar uma relação entre as variáveis clínicas e epidemiológicas  com o tempo de cura dos pacientes com hanseníase, uma vez que a duração do tratamento é padronizada de acordo com o grau da doença. Além disso, também não se pode concluir que há uma relação entre o índice de desenvolvimento humano com a incidência (número de casos novos) e os casos de abandono do tratamento da doença, pois embora tenha se obtido uma correlação negativa (indicando que quanto menor o IDH, maior a incidência da doença), esse valor foi de 0,28.
>
> O classificador XGBoost obteve os melhores resultados com acurácia de 96%, revocação da classe 0 (abandono) de 65%, revocação da classe 1 (cura) de 98%, precisão da classe 0 de 68%, precisão da classe 1 de 98%, f1 score da classe 0 de 66%, e f1 score da classe 1 de 98%. Tendo em vista que o ideal para classificar o problema, deve possuir um equilíbrio entre as quatro métricas avaliadas (acurácia, revocação, precisão e f1-score), pode-se considerar que o trabalho apresentou resultados promissores.

# Trabalhos Futuros
>Alguns aspectos que não foram concluídos ou inclusos nesse trabalho podem ser aprimorados no futuro. O primeiro é extender a análise para o corte temporal após a pandemia de covid-19 (a partir de 2020). Segundo, utilizar outras variáveis para análises, como formas clínicas e regiões geográficas. 

# Cronograma
> |Etapas | Sem 1 | Sem 2| Sem 3| Sem 4| Sem 5| Sem 6| Sem 7| Sem 8| Sem 9| Sem 10|
> |--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
> | Definição do escopo do projeto e planejamento da metodologia  | X |  |  |  |  |  |  |  |  |  |
> | Pré-processamento dos dados  |  | X |  |  |  |  |  |  |  |  |
> | Análise exploratória|  |  | X | X |  |  |  |  |  |  |
> | Entrega 2  |  |  |  | X |  |  |  |  |  |  |
> | Modelagem preditiva e avaliação dos modelos  |  |  |  |  | X | X | X |  |  |  |
> | Avaliação do modelo  |  |  |  |  |  |  |  | X |  |  |
> | Elaboração do relatório  |  |  |  |  |  |  |  |  | X |  |
> | Entrega final e apresentação  |  |  |  |  |  |  |  |  |  | X |

# Referências Bibliográficas
> 1. de Andrade KVF, Nery SJ, Pescarini MJ, Ramond A, Teles Santos dS CA, Ichihara MY, et al. (2019). Geographic and socioeconomic factors associated with leprosy treatment default: An analysis from the 100 Million Brazilian Cohort. PLOS Neglected Tropical Diseases, 13(9): e0007714. https://doi.org/10.1371/journal. pntd.0007714.
>    
> 2. Girão, R. J. S., N. L. R. Soares, J. V. Pinheiro, G. da P. Oliveira, S. M. F. de Carvalho, L. C. de Abreu, V. E. Valenti, and F. L. A. Fonseca. 2013. Leprosy treatment dropout: a systematic review. International Archives of Medicine 6: 34.
>
> 3. Kerr-Pontes LR, Barreto M L, Evangelista CM, Rodrigues LC, Heukelbach, and Feldmeier H. (2006). Socioeconomic, environmental, and behavioural risk factors for leprosy in North-east Brazil: Results of a case–control study. International Journal of Epidemiology, 35(4): 994–1000. https://doi.org/10.1093/ije/dyl072.
>
> 4. Lima, L. V. de, G. Pavinati, I. G. P. Silva, D. R. de O. Moura, N. L. de M. Gil, and G. T. Magnabosco. 2022. Tendência temporal, distribuição e autocorrelação espacial da hanseníase no Brasil: estudo ecológico, 2011 a 2021. Revista Brasileira de Epidemiologia 25: e220040.
> 
> 5. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Articulação Estratégica de Vigilância em Saúde. 2022. Guia de Vigilância em Saúde. Brasília, DF. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/guia_vigilancia_saude_5ed_rev_atual.pdf Acesso em Maio 2023.
>
> 6. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Vigilância das Doenças Transmissíveis. 2017. Guia prático sobre a hanseníase. Brasília, DF. Disponível em: https://www.gov.br/aids/pt-br/centrais-de-conteudo/publicacoes/2021/guia-pratico-sobre-a-hanseniase/view Acesso em: Maio 2023.
>
> 7. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Vigilância das Doenças Transmissíveis. 2016. Diretrizes para vigilância, atenção e eliminação da Hanseníase como problema de saúde pública: manual técnico operacional.  Brasília, DF. Disponível em: http://portal.saude.pe.gov.br/sites/portal.saude.pe.gov.br/files/diretrizes_para_._eliminacao_hanseniase_-_manual_-_3fev16_isbn_nucom_final_2.pdf Acesso em: Maio 2023. 
>
> 8. Nery, J. S., A. Ramond, J. M. Pescarini, A. Alves, A. Strina, M. Y. Ichihara, M. L. Fernandes Penna, et al. 2019. Socioeconomic determinants of leprosy new case detection in the 100 Million Brazilian Cohort: a population-based linkage study. The Lancet. Global Health 7: e1226–e1236.
> 
> 9. Ploemacher T, Faber WR, Menke H, Rutten V, and Pieters T. (2020). Reservoirs and transmission routes of leprosy; A systematic review. PLOS Neglected Tropical Diseases, 14(4): e0008276. https://doi.org/10.1371/journal.pntd.0008276.
>
> 10. World Health Organization. Leprosy. https://www.who.int/news-room/fact-sheets/detail/leprosy. Update January 27, 2023. Acesso em: Maio 2023.
