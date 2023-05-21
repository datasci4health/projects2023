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


# Descrição Resumida do Projeto
> A hanseníase é uma doença infecciosa crônica e transmissível que afeta principalmente a pele e o sistema nervoso periférico. Os agentes causantes da enfermidade são as bactérias Mycobacterium leprae e Mycobacterium lepromatosis. A doença pode afetar pessoas de qualquer sexo ou faixa etária, sua evolução é de forma lenta e progressiva, e se não for tratada na fase inicial, pode levar a incapacidades físicas. A infecção está inserida no grupo de doenças tropicais negligenciadas e continua sendo um problema de saúde pública em muitos países, incluindo o Brasil. Embora a tendência de novos casos tenha diminuído ao longo do tempo devido ao tratamento com terapia multidrogas, o Brasil ocupa atualmente o segundo lugar em termos de prevalência no mundo.
> 
> O esquema de tratamento (número de doses e tempo) é padronizado e depende da classificação operacional da doença baseada no número de lesões cutâneas. Os casos são classificados como paucibacilares (PB, até cinco lesões) ou multibacilares (MB, seis ou mais lesões de pele), com uma duração de tratamento de 6 a 12 meses, respectivamente. Se o tratamento é realizado de forma completa e correta a transmissão da doença é interrompida, impede que outras pessoas sejam infectadas e o paciente é curado. Apesar dos avanços no tratamento para a cura da doença, o abandono da terapia multidrogas ainda representa um dos obstáculos para o controle efetivo e a eliminação da hanseníase. Por exemplo, os casos de abandono podem resultar em curas incompletas, levando a uma maior progressão da doença, o que pode prolongar o tempo de tratamento e aumentar os custos para o sistema de saúde, além de manter fontes persistentes de infecção na área geográfica.
> 
> Evidências sugerem que existem fatores associados ao risco de abandono do tratamento da hanseníase. A interrupção do tratamento pode ser influenciada por características pessoais, socioeconômicas e fatores clínicos ou médicos. Nesse contexto, este projeto tem como objetivo analisar os casos novos de hanseníase no período de 2009 a 2019, a fim de determinar padrões ou relações entre as características dos pacientes e da doença com os casos de cura e abandono do tratamento. Além disso, pretende-se identificar diferentes padrões espaciais de ocorrência e abandono, levando em consideração o índice de desenvolvimento humano. Para isso, serão utilizadas técnicas de machine learning para identificar as variáveis mais relevantes e sua relação com os casos de cura e abandono do tratamento.
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
> Qual é o desempenho dos modelos de machine learning na previsão do tempo de cura dos pacientes com hanseníase?

# Metodologia
> Seleção e tratamento dos dados
> Os dados foram obtidos do Sistema de Informação de Agravos de Notificação (SINAN) no período de 2009 a 2019. Os dados foram pré-processados considerando apenas os casos novos notificados a cada ano. Um caso novo é a pessoa que nunca recebeu qualquer tratamento específico para a doença. Verificou-se que os casos novos eram residentes do Brasil no momento da notificação e não houve duplicatas. 
Considerando as características da doença e a variação das variáveis fornecidas no banco de dados, foi realizada uma análise exploratória para identificar e selecionar features que mostram relação com a cura e o abandono do tratamento (ver report). 
> A alta por cura implica que o tratamento foi concluído (6 ou doze meses de acordo com a classificação operacional), juntamente com a avaliação médica, o que resulta na saída do paciente do registro ativo no SINAN. Os casos de abandono do tratamento são aqueles em que os pacientes não conseguem completar o tratamento dentro do prazo máximo permitido (mais de três ou seis meses consecutivos, se forem paucibacilares e multibacilares, respectivamente), apesar de repetidas tentativas de retorno e acompanhamento do tratamento.
>
> Análise descriptivos
> A partir desse subconjunto de dados, foi realizada um análise descriptiva dos casos novos, dos casos de cura e dos casos de abandono de tratamento, estratificada por sexo, faixa etária, classificação operacional e outras variáveis clínicas dos pacientes. Além disso, determinou-se a correlação das variáveis com os desfechos da doença.
>
> Análise espacial
> Para identificar padrões espaciais de ocorrência e abandono, determinou-se a proporção de casos de hanseníase em abandono de tratamento entre os casos novos diagnosticados nos anos das cortes como um indicador para avaliar a qualidade da atenção e do acompanhamento dos casos novos diagnosticados até a conclusão do tratamento. Para o cálculo desse indicador, utilizaram-se os casos novos de hanseníase diagnosticados nos anos das coortes que abandonaram o tratamento até 31/12 do ano de avaliação, dividido pelo total de casos novos diagnosticados nos anos das coortes, multiplicado por 100. O qualidade de atenção pode ser classificada como Boa quando o indicador é inferior a 10%, Regular quando está entre 10% e 24,9% e Precária quando é igual ou superior a 25%. Para esse indicador foi utilizado o município e a unidade federativa de residência atual dos casos notificados, excluindo aqueles com a classificação de "erro de diagnóstico” no banco de dados. Com base nos parâmetros obtidos, foram criados mapas temáticos para cada ano.

## Bases de Dados e Evolução
> Bases de dados estudadas e/ou utilizadas no projeto.

### Bases Estudadas e Adotadas

> Para cada base, coloque uma mini-tabela no modelo a seguir e depois detalhamento sobre como ela foi analisada/usada, conforme exemplo a seguir.

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Sistema de Informação de Agravos de Notificação (SINAN) | http://portalsinan.saude.gov.br/hanseniase | Banco de dados nacional alimentado pela notificação e investigação de casos de doenças e agravos gerados pelo Sistema de Vigilância Epidemiológica a nível municipal, estadual e nacional.

> * Qual o esquema/dicionário desse banco (o formato é livre)?
> 
> Sim, [link](https://github.com/alexbjr/hans_project/blob/main/hans_project/data/raw/dicionario_dados.xlsx) para o dicionário de dados.
> 
> * O que descobriu sobre esse banco?
> 
> * Quais as transformações e tratamentos (e.g., dados faltantes e limpeza) feitos?
> 
> Foram feitos filtros na base para remoção de duplicadas, para selecionar apenas casos do Brasil, apenas novos casos registrados no sistema (exclui reincidente) e apenas os casos com desfecho: cura, óbito ou abandono. Em seguida, foi realizada a mudança do tipo de algumas colunas que estavam caracterizadas como numéricas, mas representavam uma categoria. Depois, foram removidas todas as features com baixa variação de dados e alta cardinalidade. Outras colunas foram removidas sob o critério de não serem relevantes para o problema estudado. Por fim, foi feito um corte temporal para analisar apenas os casos de 2009 a 2019.
> 
> * Apresente aqui uma Análise Exploratória (inicial) sobre esta base.
> 
> Para Análise Exploratória dessa base foram analisados a quantidade de casos registrados em cada estado ao longo dos anos com o objetivo de entender se existia alguma região em que a doença predominou e se essa proporção foi reduzindo ou aumentando com o passar de uma década. Além disso, foi analisada a gravidade desses casos registrados, para entender onde há a presença de casos mais graves. Em seguida foram analisadas duas variaáveis (tempo de cura e tipo de saída do tratamento), para cada uma foi calculada a correlação com outras variáveis a fim de entender como se comportavam com outras variáveis. Por fim, foi iniciado testes de ML para analisar a acurácia do modelo em prever se o paciente abandonará o tratamento ou seguirá até o fim.


Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Atlas Brasil | http://www.atlasbrasil.org.br/consulta/planilha | O Atlas Brasil é um projeto que reúne informações socioeconômicas e demográficas sobre o Brasil. Ele oferece uma ampla gama de indicadores e dados estatísticos que abrangem diversos aspectos do país, permitindo análises e comparações em diferentes níveis geográficos.

> * Qual o esquema/dicionário desse banco (o formato é livre)?
> 
> Sim, é um site de consulta em que você seleciona quais indicadores (educação, desenvolvimento humano, renda, etc) e quais territorialidade deseja acessar. Nessse caso, foi selecionado apenas o IDH por estado ao longo dos anos.
> 
> * O que descobriu sobre esse banco?
> 
> Ele oferece uma ampla gama de indicadores e dados estatísticos que abrangem diversos aspectos do país, permitindo análises e comparações em diferentes níveis geográficos.
> 
> * Quais as transformações e tratamentos (e.g., dados faltantes e limpeza) feitos?
> 
> Não foi encontrado dados para o IDH de 2009 e 2011 e portanto, para estes anos, foram considerados os mesmos valores de 2010. Foi necessário remover o texto 'IDHM' das colunas, restando apenas o ano ao qual aqueles valores se referem. Foi removido os dados sobre o IDH do país, deixando apenas os dos estados. Além disso, foi substituído o nome dos estados por suas siglas. Por fim, foi adaptado o formato da tabela para conter apenas três colunas (UF, NU_ANO, IDH).
> 
> * Apresente aqui uma Análise Exploratória (inicial) sobre esta base.
> 
> Foi feita uma análise de correlação do IDH com a quantidade de casos novos nos estados em cada ano, indicando uma correlação negativa, mas muito baixa (0.28)

### Integração entre Bases e Análise Exploratória

> As bases foram unidas por sigla do estado (UF) e por ano (NU_ANO), dessa forma, foi obtido uma tabela com quatro colunas (UF, NU_ANO, IDH, N_CASOS) e a partir disso foi possível analisar a correlação entre o IDH e a quantidade de casos em cada estado.
> 
> Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> Utilize gráficos que descrevam os aspectos principais da base que são relevantes para as perguntas de pesquisa consideradas.
> 
> O maior número de casos novos diagnosticados esteve concentrado em pacientes com idades entre 40 e 69 anos, sendo maior na faixa etária de 40 a 49 anos. Por outro lado, a maior  proporção de pacientes que abandonaram o tratamento ocorreu entre os 20 e 49 anos de idade, destacando-se aqueles com idades entre 20 a 29 anos.(Figura 1).
>  
> ![Figura 1. Número de casos novos diagnosticados e abandonos do tratamento por faixa etária a cada 10 anos no período de 2009 a 2019 no Brasil.] (https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_idade.png)
> 
> Em todo o periódo analisado, o sexo masculino apresenta o maior número de casos novos diagnosticados e de abandono do tratamento em comparação com o sexo feminino. Observa-se uma tendência decrescente nos casos novos ao longo dos anos, com uma queda em 2016 e 2017. No entanto, os casos de abandono do tratamento em ambos os sexos mantiveram uma tendência similar. Durante o ano de 2019, a proporção de pacientes que abandonaram o tratamento foi maior para ambos os sexos. Por outro lado, os anos 2010 e 2011 apresentaram proporções menores de abandono (Figura 2).
> 
> ![Figura 2. Número de casos novos e de abandono do tratamento estratificado por sexo e ano no período de 2009 a 2019 no Brasil. F:feminino, M:masculino.](https://github.com/alexbjr/hans_project/blob/main/hans_project/assets/graficos/graficos_ab_sexo.png)
> 
> 


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

# Dicionário / Roteiro
> 
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
> Formas clínicas: Classificação segundo Madri 1953.
> Hanseníase indeterminada (HI) -- PB
> H. tuberculóide (HT) -- PB
> H. dimorfa (HD) -- MB
> H. virchowiana (HV) -- MB
> 
> Classificação operacional baseado no número de lesões cutâneas (OMS).
> Paucibacilar (PB)
> Multibacilar (MB)
> 
> Tratamento - esquemas terapêuticos
> Série de medicamentos diários e mensais dependendo da classificação operacional padronizada pela Organização Mundial da Saúde(OMS). O tratamento é com poliquimioterapia (PQT).
> 
> Casos novos em faixa etária menor de 15 anos: A ocorrência de casos novos nesta faixa etária indica focos de transmissão ativa, importante sinalizador para o monitoramento da doença.
> 
> Grau de Incapacidade Física (GIF): Indica a perda da sensibilidade protetora e/ou deformidade visível em consequência de lesão neural e/ou cegueira. 
Casos notificados com GIF=2 (de maior avanço) evidenciam diagnóstico tardio, devido ao maior grau de comprometimento físico ocasionado pela hanseníase.
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


# Referências
> 1. de Andrade KVF, Nery SJ, Pescarini MJ, Ramond A, Teles Santos dS CA, Ichihara MY, et al. (2019). Geographic and socioeconomic factors associated with leprosy treatment default: An analysis from the 100 Million Brazilian Cohort. PLOS Neglected Tropical Diseases, 13(9): e0007714. https://doi.org/10.1371/journal. pntd.0007714.
>
> 2. Kerr-Pontes LR, Barreto M L, Evangelista CM, Rodrigues LC, Heukelbach, and Feldmeier H. (2006). Socioeconomic, environmental, and behavioural risk factors for leprosy in North-east Brazil: Results of a case–control study. International Journal of Epidemiology, 35(4): 994–1000. https://doi.org/10.1093/ije/dyl072.
>
> 3. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Articulação Estratégica de Vigilância em Saúde. 2022. Guia de Vigilância em Saúde. Brasília, DF. Disponível em: https://bvsms.saude.gov.br/bvs/publicacoes/guia_vigilancia_saude_5ed_rev_atual.pdf Acesso em Maio 2023.
>
> 4. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Vigilância das Doenças Transmissíveis. 2017. Guia prático sobre a hanseníase. Brasília, DF. Disponível em: https://www.gov.br/aids/pt-br/centrais-de-conteudo/publicacoes/2021/guia-pratico-sobre-a-hanseniase/view Acesso em: Maio 2023.
>
> 5. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Vigilância das Doenças Transmissíveis. 2016. Diretrizes para vigilância, atenção e eliminação da Hanseníase como problema de saúde pública: manual técnico operacional.  Brasília, DF. Disponível em: http://portal.saude.pe.gov.br/sites/portal.saude.pe.gov.br/files/diretrizes_para_._eliminacao_hanseniase_-_manual_-_3fev16_isbn_nucom_final_2.pdf Acesso em: Maio 2023. 
> 
> 6. Ploemacher T, Faber WR, Menke H, Rutten V, and Pieters T. (2020). Reservoirs and transmission routes of leprosy; A systematic review. PLOS Neglected Tropical Diseases, 14(4): e0008276. https://doi.org/10.1371/journal.pntd.0008276.
>
> 7. World Health Organization. Leprosy. https://www.who.int/news-room/fact-sheets/detail/leprosy. Update January 27, 2023. Acesso em: Maio 2023.
