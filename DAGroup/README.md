# Projeto `Associação de comportamentos de saúde e doenças crônicas não transmissíveis com depressão no Brasil`

### Project `Association of health behavior and chronic noncommunicable diseases with depression in Brazil`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp.

|Nome  | RA | Especialização|
|--|--|--|
| Beatriz Silva Nunes  | 167428  | Saúde - [Conta GitHub](https://github.com/beatrizsnunes)|
| Arthur Rezende Salles   | 166003  | Computação - Líder Github - [Conta GitHub](https://github.com/Arthur-Salles)|
| Anderson Nogueira Cotrim  | 163993  | Computação - [Conta GitHub](https://github.com/AndersonCotrim)|
| Guilherme Magalhães Soares  | 217241  | Elétrica - [Conta GitHub](https://github.com/gsoso01)|

## Slides da Apresentação Final

[Link para slides da apresentação final do projeto](https://www.canva.com/design/DAFmwXEC7yY/icnFkTJZTTm-u82yPKs00A/edit?utm_content=DAFmwXEC7yY)

## Apresentação inicial do projeto

[Link para vídeo de apresentação da proposta do projeto](https://drive.google.com/file/d/1uQ0wQsbig9BBA0OvvMyG8jLpcLTL104L/view?usp=share_link)

# Introdução e Referenciais Teóricos

> Contextualização do projeto
> Caracterização do problema
> Motivação
> Relevância
> Trabalhos relacionados
> Indicação (bastante resumida) da análise proposta
> Indicação (bastante resumida) dos resultados alcançados

As doenças crônicas não transmissíveis (DCNT) são um problema de saúde pública global [1]. DCNT estão associadas a diversos fatores de risco ou comportamentos de saúde inadequados, dentre eles o uso de tabaco, inatividade física, consumo excessivo de álcool e dietas não saudáveis [1]. Entre as doenças crônicas temos a desordem depressiva ou depressão que é uma doença mental comum, caracterizada como uma persistência da tristeza e baixo interesse ou prazer em atividades anteriormente colocadas como comuns ou agradáveis [2, 3].

A depressão afeta cerca de 5% da população adulta mundial [2]. O tratamento da depressão é complexo e infelizmente ineficaz, reduz somente cerca de um terço da carga da desordem depressiva [4]. Com isso, a prevenção é a melhor forma de combater a depressão, similarmente a situação de outras doenças crônicas não transmissíveis como a obesidade.

Estudos prévios têm demonstrado associações entre depressão e comportamentos de saúde inadequados na população brasileira, com variações de acordo com características sociodemográficas, como sexo e renda [5, 6]. Além disso, fatores de risco têm sido associados ao diagnóstico de depressão, assim como a presença de outras doenças crônicas não transmissíveis, como diabetes e artrite. Essa associação não se deve apenas à reação depressiva decorrente da presença de uma doença, mas também ao compartilhamento de fatores de risco e mecanismos fisiopatológicos comuns entre a depressão e outras doenças crônicas não transmissíveis [7, 8]. No entanto, existem poucos estudos que investigam essa relação em países de baixa e média renda [7].

Compreender a relação entre as doenças crônicas não transmissíveis e a depressão, considerando os fatores de risco associados à doença, bem como as particularidades sociodemográficas da população brasileira, é de extrema importância para o desenvolvimento de políticas públicas eficazes no combate ao avanço da depressão no país.

A utilização de inquéritos de saúde nacionais se torna extremamente pertinente para a compreensão da prevalência das doenças e dos fatores associados, visto que são produzidos com amostragens representativas da população brasileira, com o propósito de orientar diretrizes e políticas públicas de Saúde no país [9].

A partir desse cenário, o objetivo do estudo é buscar comportamentos de saúde inadequados e doenças crônicas não transmissíveis mais determinantes para o diagnóstico da depressão em um inquérito de saúde nacional possibilitando auxiliar na prevenção do desenvolvimento da depressão no Brasil.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/assets/DAG.jpg)

Neste trabalho, utilizamos técnicas de análise estatística, como o teste qui-quadrado, para avaliar a associação de variáveis de comportamentos de saúde, doenças crônicas não transmissíveis e características sociodemograficas com depressão. Além disso, treinamos modelos de classificação binária para prever se uma pessoa é potencialmente diagnósticada com depressão (utilizando o questionário PHQ-9) a partir de variáveis de elecandas acima.

O modelo de regressão logística apresentou o melhor desempenho preditivo, com uma precisão de 18,49%, recall (revocação) de 66,39% e AUC (área sob a curva) de 71,57%. Embora a eficácia tenha sido baixa, esse modelo nos permite analisar a influência desses variáveis na depressão.

# Perguntas de Pesquisa e Objetivos

> Perguntas de pesquisa (revisadas e atualizadas) que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.
> Se a análise exploratória contribuiu para as perguntas de pesquisa, apresente aqui elementos de análise exploratória que ajudem a responder a questão.
> Objetivos principais e específicos

Algumas perguntas de pesquisa foram pensadas visando uma compreensão aprofundada dos determinantes associados à depressão.

 - Quais hábitos de vida estão associados à depressão? 
 - É possível quantificar o grau de impacto de cada hábito, considerando tanto as influências positivas quanto negativas? 
 - A influência desses fatores varia ao longo do curso da vida e de variaveis sociodemográficas?
 - Será que os comportamentos de saúde e/ou doenças crônicas não transmissíveis são determinantes para o diagnóstico de depressão? 

Através dos experimentos exploratórios, análise de correlação e gráficos de distribuição, foram confirmados a associação entre a depressão (utilizando χ2 de Pearson) com os comportamentos de saúde inadequados e as doenças crônicas não transmissíveis elecandas no estudo, variaveis que estão em consonância com a literatura existente. Essas descobertas já contribuem para responder a primeira questão de pesquisa.

Para abordar a segunda questão, utilizamos a análise de regressão logística. Essa abordagem permitiu avaliar de forma mais precisa o grau de impacto de cada hábito, considerando tanto as influências positivas quanto as negativas, relacionadas à depressão.

Em relação à terceira questão, observou-se uma diferença na distribuição do potencial de depressão em relação à idade e renda. Os fatores que influenciam essa diferença foram confrontados e explorados por meio da análise de regressão logística, possibilitando uma compreensão mais aprofundada.

Para a quarta questão, realizamos uma comparação das eficácias dos modelos de regressão logística utilizando cada grupo de variáveis separadamente. Por meio desses experimentos, pudemos observar uma forte associação entre doenças crônicas e depressão, as quais demonstraram uma eficácia maior na classificação, em comparação às variáveis de hábitos, e praticamente igual em relação às variáveis sociodemográficas. 

_Objetivo geral:_

 - Compreender os comportamentos de saúde e doenças crônicas
   não transmissíveis mais determinantes para o diagnóstico da depressão
   em um inquérito de saúde nacional a fim de orientar ações de prevenção para à depressão.

_Objetivos específicos:_

 - Analisar quais comportamentos de saúde inadequados estão associados com o diagnóstico de depressão;
 - Analisar quais doenças crônicas não transmissiveis estão associadas com o diagnóstico de depressão;
 - Analisar quais varíaveis sociodemográficas estão associadas com o diagnóstico de depressão;
 - Determinar a importância dos comportamentos de saúde e das doenças crônicas não transmissíveis e das variáveis sociodemográficas para o diagnóstico de depressão;
 - Determinar quais variaveis são determinantes para o diagnóstico de depressão.

# Metodologia

> Abordagem adotada pelo projeto na busca pela resposta às perguntas de pesquisa.
> Justificar teoricamente, sempre que possível, a metodologia adotada.

A metodologia do estudo foi baseada em quatro principais estratégias:

- Realização de um estudo bibliográfico, que permitiu entender os padrões esperados para cada pergunta de pesquisa.
- Análise exploratória, incluindo seleção e pré-processamento dos dados. 
- Realização de uma análise estatística, utilizando técnicas de estatística descritiva e visualização, como gráficos de dispersão, caixa, e barras, a fim de extrair conhecimento dos dados.
- Aplicação de técnicas de aprendizado de máquina (regressão), que nos permitiu uma análise aprofundada e a quantificação da relevância de cada característica para variável de interesse (depressão).


## Bases de Dados e Evolução

### Bases Estudadas mas Não Adotadas

Base de Dados  | Descrição | Anos
----- | ----- |  -----
[Pesquisa Nacional de Saúde do Escolar (PeNSE)](https://www.ibge.gov.br/en/statistics/social/population/16837-national-survey-of-school-health-editions.html?=&t=downloads) | O Instituto Brasileiro de Geografia e Estatística - IBGE - realiza a Pesquisa Nacional de Saúde do Escolar (PeNSE), em diversas cidades do Brasil, em parceria com o Ministério da Saúde e com o apoio do Ministério da Educação. Os objetivos da pesquisa são: conhecer e medir fatores de risco e de proteção relacionados à saúde dos adolescentes; apoiar o monitoramento da saúde dos estudantes brasileiros; oferecer orientação às iniciativas de saúde voltadas para esse grupo populacional, fornecendo informações confiáveis sobre o assunto. | 2019 (último)

Esta base de dados possui um total de 159245 alunos, com 306 características cada. Os dados estão estruturados e contam com dicionário. Inicialmente, tentamos utilizá-la para especificar mais o escopo da proposta de análise da depressão em adolescentes. Exploramos essa base por meio dos arquivos Jupyter Notebook, [pense_preprocessing.ipynb](notebooks/pense_preprocessing.ipynb) e [pense_hello_world.ipynb](notebooks/pense_hello_world.ipynb). No entanto, apesar do grande número de características, percebemos que essa base aborda pouco sobre doenças crônicas e apresenta algumas limitações relacionadas à saúde mental. Infelizmente, não encontramos nenhum indicador de depressão como o [PHQ9](https://www.mdcalc.com/calc/1725/phq9-patient-health-questionnaire9) que possa ser utilizado como na PNS (Pesquisa Nacional de Saúde).

Base de Dados  | Descrição | Anos
----- | ----- |  -----
[Sistema de Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico (Vigitel)](https://svs.aids.gov.br/download/Vigitel/) | O Vigitel é parte integrante do sistema de Vigilância de Fatores de Risco para doenças crônicas não transmissíveis (DCNT) do Ministério da Saúde, juntamente com outros inquéritos, como os domiciliares e os direcionados à população escolar. Conhecer a situação de saúde da população é o primeiro passo para planejar ações e programas que possam reduzir a ocorrência e a gravidade dessas doenças, melhorando assim a saúde da população. A pesquisa Vigitel é realizada anualmente pela Secretaria de Vigilância em Saúde (SVS) do Ministério da Saúde e as entrevistas telefônicas são conduzidas com amostras da população adulta (18 anos ou mais) residente em domicílios com linha de telefone fixo. A partir de 2022, as entrevistas também passaram a ser realizadas em telefones celulares. | 2006-2021

Não tivemos a oportunidade de explorar a fundo essa base de dados, mas, à primeira vista, ela parece apresentar um número mais limitado de características (~300) em comparação com o PNS (~1000) que aborda de forma mais abrangente os fatores de estilo de vida que propomos analisar. Além disso, essa base de dados possui informações verificáveis se o diagnóstico de depressão já foi feito, mas não oferece parâmetros para avaliar o estado atual da saúde mental do entrevistado no momento da coleta dos dados.

### Bases Estudadas e Adotadas

Base de Dados  | Descrição | Anos
----- | ----- |  -----
[Pesquisa Nacional de Saúde (PNS)](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html?=&t=downloads) | Realizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) em parceria com o Ministério da Saúde, tem como objetivo coletar informações sobre o desempenho do sistema nacional de saúde em relação ao acesso e uso dos serviços disponíveis, bem como garantir a continuidade dos cuidados necessários. Além disso, a pesquisa visa avaliar as condições de saúde da população, monitorar doenças crônicas não transmissíveis e identificar os principais fatores de risco associados a elas. |  2019 (último)

O presente estudo utilizou como fonte de dados a [Pesquisa Nacional de Saúde de 2019](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html?=&t=downloads), a qual possui uma amostra da população brasileira residente em domicílios particulares de todo o território brasileiro e detalhes sobre o processo de amostragem dessa pesquisa foram publicados[6].

O dicionário disponibilizado pela PNS pode ser encontrado [aqui](data/raw/PNS_2019/dicionario.xlsx). O dicionário dispõe das perguntas feitas aos indivíduos e as possíveis respostas. Nota-se a grande variedade de perguntas relacionadas a doenças crônicas e aos hábitos do domicílio. 

Foi necessáro filtrar de forma arbitrária as variáveis relevantes para responder às questões de pesquisa escolhidas anteriormente. Originou um banco de dados para a análise do estudo com perguntas para caracterização da amostra como sexo, cor ou raça, nível de escolaridade, renda média, características do domicílio, para verificação de comportamentos de saúde como consumo de álcool, tabaco, hábitos alimentares e atividade física, e para avaliar as doenças crônicas como peso, altura e diagnóstico de alguma doença crônica não transmissível (doenças cardíacas, artrite, diabetes, entre outras) por algum médico especialista. 

Ao final desse processamento obtivemos 90846 linhas e 380 colunas de dados relevantes para as perguntas de pesquisa.


### Integração entre Bases e Análise Exploratória

> Descreva etapas de integração de fontes de dados e apresente a seguir uma análise exploratória que envolva ambas.
>
> Resultados de Análise Exploratória
> * use estatística descritiva e gráficos;
> * inclua gráficos de sobre a distribuição dos dados (e.g., histogramas e boxplots);
> * analise correlação e use gráficos de dispersão;
> * descreva os resultados/gráficos, os analise e contextualize com o tema definido.

Primeiramente realizamos a análise exploratória do banco de dados, buscando uma caracterização da amostra. Em seguida, categorizamos as variáveis de interesse de acordo com os parâmetros utilizados na literatura, conforme apresentado a seguir:

#### Variável dependente:

A prevalência de depressão na população estudada foi avaliada através da aplicação do indicador PHQ9, que indica a severidade da doença em cinco intervalos: nenhum ou mínimo, leve, moderada, moderadamente grave e grave. Para as análises, as pessoas com pontuação igual ou superior a 10 pontos do indicador foram classificadas com depressão.

Apenas pessoas com idade entre 18 e 59 anos podem ser avaliadas neste índice. Portanto, o estudo foi restrito a essa faixa etária e as mulheres grávidas foram excluídas da análise devido a questões metodológicas específicas (n = 736), resultando em uma amostra final de 64.664 indivíduos.	

#### Variáveis independentes:

*Variáveis relacionadas às doenças crônicas não transmissíveis*:

 - **Presença de artrite, AVC, doenças cardiovasculares, hipertensão, hipercolesterolemia, diabetes**: sim ou não;
 - **Presença de obesidade**: calculamos o IMC dos indivíduos (peso/altura²) e classificamos com obesidade, os indivíduos com IMC superior ou igual a 30 (sim/não).

*Variáveis relacionadas aos comportamentos de saúde*:

- **Alimentação**: aplicamos um score de consumo de produtos ultraprocessados de 0 a 10 pontos, o qual é baseado na resposta positiva de consumo no dia anterior dos seguintes alimentos [10]. Quanto maior a pontuação do score, maior o consumo de ultraprocessados, ou seja, menos saudável é a dieta. Os alimentos considerados na pontuação incluem:
  - Refrigerante; 
  - Suco de fruta em caixinha ou lata ou refresco em pó;
  - Bebida achocolatada ou iogurte com sabor; 
  - Salgadinho de pacote ou biscoito/bolacha salgado; 
  - Biscoito/bolacha doce ou recheado ou bolo de pacote; 
  - Sorvete, chocolate, gelatina, flan ou outra sobremesa industrializada; 
  - Salsicha, linguiça, mortadela ou presunto; 
  - Pão de forma, de cachorro-quente ou de hambúrguer;
  - Margarina, maionese, ketchup ou outros molhos ultraprocessados; 
  - Macarrão instantâneo, sopa de pacote, lasanha congelada ou outro prato congelado comprado pronto industrializado. 
- **Exercício físico** [5]: prática de exercício físico nos últimos 3 meses (sim/não).
- **Consumo de álcool** [11]: consumo de bebidas alcoólica uma vez ou mais por mês (sim/não) 
- **Tabagismo** [5]: faz uso de algum tipo de tabaco (sim/não)

*Variáveis relacionadas ao perfil sociodemográfico:*

- **Escolaridade**: Sem instrução e fundamental incompleto (1), fundamental completo e médio incompleto (2), médio completo e superior incompleto (3), superior completo (4);
- **Sexo**: feminino (0) ou masculino (1);
- **Estado Civil**: vive sozinho (0) ou com conjugue (1);
- **Idade** [10]: 18 a 29 anos (1), 30 a 39 anos (2), 40 a 49 anos (3), 50 a 59 anos (4);
- **Renda per capita** [5]: recebe menos de 1 salário mínimo (0) ou recebe mais de 1 salário mínimo (1);
- **Localidade**: região geográfica dos indivíduos (Norte, Nordeste, Centro, Sul, Sudeste);


Abaixo temos um resumo do workflow dos experimentos realizados com esta base:

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/assets/e2_workflow.png)

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/assets/e2_specific_workflow.png" alt="drawing" width="583"/>

#### Análise Exploratória

Os gráficos abaixo descrevem a proporção em relação a sexo, cor ou raça das amostras da população. Onde podemos observar um balanceamento em gênero e a predominância parda na categoria cor ou raça.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_sexo_cor.png" alt="drawing" width="583"/>

Abaixo podemos observar curvas de distribuição dos indivíduos da base em relação à idade e peso, podemos notar que estas curvas estão num intervalo de valores a primeira vista aceitável indicando que, aparentemente, grande parte dos dados em relação a este atributo estão confiáveis. Mais abaixo temos a distribuição destas mesmas características, porém limitados à amostragem aplicável ao PHQ9 (pessoas de 18 a 59 anos).

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_idade_peso.png" alt="drawing" width="700"/>

Por fim nos gráficos de barras abaixo temos a proporção do nível escolar e da renda per capita da população geral:

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_escolaridade_renda.png" alt="drawing" width="700"/>

Em relação à distribuição do valor PHQ9 (inteiro de 0 à 27), esta apresenta um comportamento similar ao de uma exponencial negativa, conforme podemos observar na figura abaixo:

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_phq9_total_dist.png" alt="drawing" width="700"/>

Nas figuras abaixo podemos comparar as distribuições do score PHQ-9 confrontadas com algumas variáveis de interesse. Foi possível notar que há uma maior prevalência de pessoas do sexo feminino com depressão ao longo de todo o score de PHQ-9, o mesmo ocorre com pessoas com idade superior aos 40 anos. Evidenciando que independente do grau de gravidade da doença, a diferença entre as categorias se mantêm. 


<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_analysis/01_pns_compare_dist_phq9_startos1.png" alt="drawing" width="700"/>

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_analysis/01_pns_compare_dist_phq9_startos3.png" alt="drawing" width="700"/>

Abaixo temos gráficos de depressão com tratamento e atendimento no SUS.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_depression_stats.png" alt="drawing" width="700"/>

Abaixo temos o gráfico da porcentagem de pessoas que já disseram diagnosticadas por depressão por estado brasileiro.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_brazil_depression.png" alt="drawing" width="450"/>

Curiosamente, notou-se uma alta correlação entre o IDH médio de cada estado com a porcentagem de depressão.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_depression_idh_correlation.png" alt="drawing" width="600"/>

O grupo suspeita que essa observação está relacionada ao fato de que o diagnóstico de depressão ou sua ausência está fortemente ligado à disponibilidade e facilidade de acesso aos serviços de saúde, o que tende a ser mais comum em regiões com um Índice de Desenvolvimento Humano (IDH) mais elevado. 

Avaliando o PHQ9 >= 10 questionário aplicado durante à entrevista obtivemos o gráfico de correlação abaixo, reforçando a suspeita observada acima.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_phq9_idh_correlation.png" alt="drawing" width="450"/>

Abaixo temos o gráfico da porcentagem de pessoas com o PHQ9 >= 10 por estado brasileiro.

<img src="https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_brazil_phq9.png" alt="drawing" width="450"/>

# Análises Realizadas

> Descrição detalhada das análises realizadas.
>
>Relate aqui também a evolução do projeto: possíveis problemas enfrentados e possíveis mudanças de trajetória. Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.
>
> Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
>
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.
> 

Iniciamos as análises buscando a associação das variáveis de interesse com o diagnóstico de depressão por meio do teste χ2 de Pearson, devido ao fato das nossas variáveis serem qualitativas.

Nessa etapa houve a preocupação de averiguar os dados faltantes de cada variável de interesse, gerando necessidade de algumas alterações na seleção dessas variáveis, pois primeiramente havíamos desenvolvido indicadores com base nos apresentados pela [PNS](https://www.pns.icict.fiocruz.br/painel-de-indicadores-mobile-desktop/). No entanto, percebeu-se uma grande quantidade de informações faltantes nas variáveis que compunham esses indicadores, como em indicadores de prática de exercício físico e consumo de bebida alcoólica.

O indicador de consumo de bebida alcoólica utilizado pela PNS foi elaborado baseado em definições da OMS, a qual considera uma pessoa ativa com base na relação entre o tempo gasto e tipo de atividade física (leve, moderada e vigorosas), porém as variáveis necessárias para construir esse indicador apresentaram uma ausência de cerca de 58% dos dados. Devido a esse problema, modificou-se o critério de classificação de exercício físico, baseando-se em artigos que também avaliaram dados da PNS, considerando praticante de exercício físico aqueles que realizaram algum tipo de exercício físico nos últimos três meses [11] e para essa variável não encontramos dados faltantes para a população alvo. No que diz respeito ao indicador de consumo de álcool, com base na frequência semanal de consumo de bebidas alcoólicas como o elencando o site da PNS, constatou-se que cerca de 69% dos dados estavam faltando, com isso houve a necessidade de modificar o indicador averiguando a frequência mensal de consumo de bebida alcoólica, visto que essa variável é utilizada pela literatura e não apresenta dados faltantes [5].

Além disso, em relação às doenças crônicas, foi notado uma baixa quantidade de dados faltantes (10%). Visando não alterar a distribuição dos dados e manter a característica binária das perguntas (se houve ou não diagnóstico da doença por um especialista), optamos por não realizar nenhum procedimento de imputação. Com isso, os indivíduos que não responderam à estas questões foram removidas da análise.

No desenvolvimento do modelo, deparamo-nos com outro problema relacionado ao grande desbalanceio na quantidade de pessoas diagnosticadas com depressão ou não. Dos 64.664 indivíduos no total, apenas 6.848 (10,6%) foram classificados como depressivos (PHQ-9 maior ou igual a 10). Portanto, primeiramente aplicou-se o algoritmo SMOTE no conjunto de treinamento para gerar dados sintéticos na classe menos representada. No entanto, ao utilizar a curva ROC-AUC como parâmetro, constatou-se que a regressão logística com penalização para a classe majoritária apresentou uma abordagem mais eficaz.


Para realizar nossa análise e responder às questões de pesquisa, procedemos da seguinte maneira: inicialmente, dividimos os dados em conjuntos de treinamento (70%) e teste (30%). Após essa divisão, tivemos 45.264 amostras para treinamento e 19.400 amostras para teste. Vale ressaltar que ambos os conjuntos apresentaram aproximadamente 23% de linhas com pelo menos um dado faltante.

Para avaliar os modelos, utilizamos o F1-score como métrica principal devido à sua confiabilidade em conjuntos não balanceados. Realizamos testes removendo as linhas com dados nulos e também empregamos técnicas de imputação para encontrar o melhor modelo.

A maioria das variáveis no conjunto de dados possui valores binários. No entanto, as variáveis restantes foram normalizadas para uma escala de 0 a 1, a fim de possibilitar uma comparação justa dos coeficientes de regressão.

Para investigar a importância dos determinantes e sua influência no diagnóstico de depressão, construímos vários modelos modificando as variáveis independentes. No primeiro modelo, selecionamos apenas as variáveis relacionadas a comportamentos de saúde. No segundo modelo, selecionamos apenas as variáveis relacionadas a doenças crônicas não transmissíveis. No terceiro modelo, incluímos tanto as variáveis de comportamentos de saúde quanto as de doenças crônicas não transmissíveis. No quarto modelo, utilizamos apenas as variáveis sociodemográficas. Essa abordagem nos permitiu comparar e analisar separadamente a influência de cada grupo de fatores no diagnóstico de depressão.

Por fim, criamos um último modelo que incluiu todas as variáveis e conduzimos análises estratificadas sociodemográficas para, por exemplo, investigar variações dos fatores ao longo da vida, com o objetivo de avaliar os coeficientes mais distintos.

Além da regressão logística, também realizamos testes com árvores de decisão e floresta randômica. Para todos os algoritmos utilizados, aplicamos uma busca em grade para otimizar os hiperparâmetros dos modelos, conforme os snippets abaixo:

~~~python
param_grid = {
    'reg__C': [0.1, 1.0, 10.0],
    'reg__solver': ['liblinear', 'saga'],
    'reg__max_iter': [100, 500, 1000]
}

model = Pipeline([
    ('reg', LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42))
])

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1', n_jobs=-1)
grid_search.fit(X, y)
~~~

~~~python
param_grid = {
    'class__criterion': ['gini', 'entropy'],
    'class__max_depth': [None, 5, 10],
    'class__min_samples_split': np.arange(0, 0.05, 0.01),
    'class__min_samples_leaf': np.arange(0.01, 0.05, 0.01)
}

model = Pipeline([
    ('trans', RoundTransformer()),
    ('class', DecisionTreeClassifier(class_weight='balanced', random_state=43, 
                                     min_samples_split=0.05, min_samples_leaf=0.01))
])

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1', n_jobs=-1)
~~~

~~~python
param_grid = {
    'class__criterion': ['gini', 'entropy'],
    'class__max_depth': [None, 5, 10],
    'class__min_samples_split': np.arange(0, 0.05, 0.01),
    'class__min_samples_leaf': np.arange(0.01, 0.05, 0.01)
}

model = Pipeline([
    ('trans', RoundTransformer()),
    ('class', RandomForestClassifier(class_weight='balanced', random_state=43, 
                                     min_samples_split=0.05, min_samples_leaf=0.01))
])

grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1', n_jobs=-1)
~~~

Essas abordagens metodológicas foram adotadas com o intuito de realizar uma análise abrangente e fornecer respostas às questões de pesquisa propostas.



# Ferramentas

Ferramenta | Descrição
----- | -----
Python 3 | Linguagem de programação a ser utilizada para o desenvolvimento das soluções propostas.
Jupyter Notebook | Código principal e solução reprodutível em arquivos de Jupyter Notebook, ajuda também na visualização de dados.
Pandas | Ferramenta para manipulação e análise de dados tabulares.
NumPy | Biblioteca utilizada para manipulação de vetores multidimensionais.
Scipy | Biblioteca com algoritmos/cálculos estatísticos gerais.
Matplotlib/Plotly/Seaborn | Bibliotecas para visualização dos dados.
Scikit-learn | Biblioteca com grande variedade de algoritmos de aprendizagem de máquina.
ChatGPT | Ferramenta imprescindível, quase outro integrante do grupo, também conhecido como o evangelista da programação.



# Resultados e Discussão


> Descrição dos resultados mais importantes obtidos.
>
> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de Análises Realizadas (o que for mais pertinente).
> Discussão dos resultados. Relacionar os resultados com as perguntas de pesquisa ou hipóteses avaliadas.
> A discussão dos resultados também pode ser feita opcionalmente na seção de Resultados, na medida em que os resultados são apresentados. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?



### Testes de associação

Ao analisar as associações entre as variáveis sociodemográficas dentre as pessoas diagnósticas com depressão segundo o PHQ9, encontramos que escolaridade, sexo, estado civil, renda per capita e idade possui associação (p < 0,05) com alto potencial de depressão. Além disso, encontramos associação entre depressão e a maior parte das regiões brasileiras, exceto na região Centro-Oeste.

Assim como apresentado na literatura, encontramos que quanto menor a escolaridade maior é a proporção de pessoas com depressão, ocorreu o mesmo ao comparamos depressão com renda per capita. Em relação a variável sexo, encontramos uma prevalência de depressão muito super em mulheres comparada aos homens. Isto é atribuído a diversos fatores, por exemplo as mulheres apresentam e relatam mais sobre os sintomas clássicos para o diagnóstico da depressão em relação aos homens que relatam com menor frequência e apresentam como sintomas mais comum o abuso de álcool e drogas (https://linkinghub.elsevier.com/retrieve/pii/S0165032704003738) (https://www.sciencedirect.com/science/article/abs/pii/S0010440X07001666?via%3Dihub). Além dessas variáveis, encontramos que ao avançar da idade há uma maior prevalência de depressão dentre a amostra estudada. 



| **Variáveis sociodemográficas** 	|                                         	| **População 2019** 	| **Sem depressão** 	| **Com depressão** 	| **X²** * 	| **p** * 	|
|---------------------------------	|-----------------------------------------	|--------------------	|-------------------	|-------------------	|----------	|---------	|
|                                 	|                                         	| n = 64.664         	| n = 57.816        	| n = 6.848         	|          	|         	|
| **Escolaridade**                	| Superior completo                       	| 4,8%               	| 5,56%             	| 5,17%             	| 36,93    	| 0,0000  	|
|                                 	| Médio completo e superior incompleto    	| 15,08%             	| 17,29%            	| 16,75%            	| ---      	| ---     	|
|                                 	| Fundamental completo e médio incompleto 	| 35,7%              	| 41,09%            	| 38,09%            	| ---      	| ---     	|
|                                 	| Sem instrução e fundamental incompleto  	| 31,94%             	| 36,06%            	| 40%               	| ---      	| ---     	|
| **Sexo**                        	| Masculino                               	| 48,29%             	| 50,92%            	| 26,10%            	| 1510,69  	| 0,0000  	|
|                                 	| Feminino                                	| 51,71%             	| 49,08%            	| 73,91%            	| ---      	| ---     	|
| **Estado civil**                	| Mora com parceiro                       	| 59,89%             	| 39,01%            	| 49,40%            	| 275,03   	| 0,0000  	|
|                                 	| Não mora com parceiro                   	| 40,11%             	| 60,99%           	 | 50,60%            	| ---      	| ---     	|
| **Renda per capita**            	| Recebe mais de 1 salário mínimo         	| 42,28%             	| 43,08%            	| 35,57%            	| 141,31   	| 0,0000  	|
|                                 	| Recebe menos de 1 salário mínimo        	| 56,92%             	| 56,92%            	| 64,43             	| ---      	| ---     	|
|**Idade**                         | 18 a 29 anos (1)                         | 23,04%              | 23,29%             | 20,95%             | 76,40     | 0,0000   |
|                                  | 30 a 39 anos (2)                         | 27,46%              | 27,78%             | 24,71%             |           |          |
|                                  | 40 a 49 anos (3)                         | 25,25%              | 25,25%             | 27,06%             |           |          |
|                                  | 50 a 59 anos (4)                         | 24,06%              | 23,68%             | 27,29%             |           |          |
| **Localidade**                  	| Norte                                   	| 20,42%             	| 20,77%            	| 17,46%            	| 41,14    	| 0,0000  	|
|                                 	| Nordeste                                	| 34,90%             	| 34,73%            	| 36,40%            	| 7,60     	| 0,0058  	|
|                                 	| Sudeste                                 	| 20,70%             	| 20,48%            	| 22,49%            	| 14,99    	| 0,0001  	|
|                                 	| Sul                                     	| 12,12%             	| 12,22%            	| 11,30%            	| 4,85     	| 0,0276  	|
|                                 	| Centro Oeste                            	| 11,86%             	| 11,80%            	| 12,34%            	| 1,71     	| 0,1913  	|

\* Teste X² de variáveis sociodemográficas confrontadas com pessoas com depressão (PHQ9 score >= 10)


Em seguida, buscamos associação de comportamentos de saúde com diagnostico de depressão, onde encontramos que há associação entre todos os comportamentos de saúde elencados e o desfecho do estudo (p ≤ 0,05). Esses achados estão em consonância com a literatura, a qual mostra associação desses comportamentos de saúde inadequados com o diagnóstico de depressão. 

Ao observarmos o score de consumo de produtos ultraprocessados encontramos que as pessoas com depressão possuem um ligeiro maior consumo de ultraprocessados em relação as pessoas sem o diagnóstico de depressão. Diversos estudos mostram uma associação positiva entre maior consumo de produtos ultraprocessados como refrigerantes e doces com depressão, independente de renda e sexo. 

No que se refere a prática de exercício físico foi observado uma maior proporção de pessoas com depressão que não praticam exercício físico, assim como mostrado na literatura [5]. Diversos estudos, dentre eles algumas metanálises, apresentam evidências de que qualquer nível de atividade física atenua o risco de depressão e independentemente da idade o exercício físico é um fator protetor para o desenvolvimento da depressão (https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2018.17111194) (https://bjsm.bmj.com/content/55/16/926).


Em relação ao consumo de tabaco, encontramos uma maior prevalência de tabagismo em pessoas diagnosticadas com depressão. Já a respeito ao consumo de bebida alcoólica há uma menor prevalência de pessoas que consomem bebidas alcóolicas dentre o público alvo do trabalho, estudos vêm mostrando que o alto consumo de bebida alcoólica pode ser colocado como um fator de risco para depressão, porém o consumo leve a moderado é considerado um fator protetor, visto que o consumo moderado está correlacionado com fatores sociais e culturais, fatores importantes para a saúde mental da população. (https://www.scielo.br/j/rbp/a/gC5yf6KyWB7F4wBc7ChbcKv/?lang=en) (https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-019-6730-4). Contudo, deve-se lembrar que a depressão é o transtorno mental mais comum dentre as pessoas com problemas de consumo de álcool. (https://jamanetwork.com/journals/jamapsychiatry/fullarticle/206176).



| **Comportamentos de saúde**                         |                | **População 2019** | **Sem depressão** | **Com Depressão** | **X²** *| **p** * |
|-----------------------------------------------------|----------------|--------------------|-------------------|-------------------|---------|--------|
|                                                     |                | n = 64.664         | n = 57.816        | n = 6.848         |         |        |
| **Score de Consumo de Ultraprocessado**             | 0, 1           | 36,53%             | 36,68%            | 35,27%            | 24,9    | 0,0056 |
|                                                     | 2, 3           | 37,78%             | 37,81%            | 37,46%            | ---     | ---    |
|                                                     | 4, 5           | 18,77%             | 18,70%            | 19,32%            | ---     | ---    |
|                                                     | 6, 7           | 5,35%              | 5,28%             | 5,99%             | ---     | ---    |
|                                                     | 8, 9, 10       | 1,57%              | 1,53%             | 1,97%             | ---     | ---    |
| **Prática de exercício físico nos últimos 3 meses** | Sim            | 56,78%             | 44,20%            | 35,00%            | 210,9   | 0,0000 |
|                                                     | Não            | 43,22%             | 55,80%            | 65,00%            | ---     | ---    |
| **Consumo de bebida alcoólica no último mês**       | Sim            | 44,88%             | 45,45%            | 40,07%            | 71,7    | 0,0000 |
|                                                     | Não            | 55,12%             | 54,55%            | 59,93%            | ---     | ---    |
| **Consumo de tabaco**                               | Sim            | 13,14%             | 12,61%            | 17,58%            | 132,6   | 0,0000 |
|                                                     | Não            | 86,86%             | 87,39%            | 82,42%            | ---     | ---    |

\* Teste X² de variáveis de comportamento de saúde confrontadas com pessoas com depressão (PHQ9 score >= 10)



Por fim, analisamos as doenças crônicas não transmissíveis com depressão e verificamos que diagnóstico de artrite ou reumatismo, AVC, doenças cardiovasculares, hipercolesterolemia, diabetes, hipertensão, câncer, diabetes e obesidade estão associados com o diagnóstico de depressão. Tais associações também são encontradas por outros estudos, os quais mostram uma bidirecionalidade entre histórico de doenças crônicas não transmissiveis sendo fator de risco para depressão e depressão sendo elencada como fator de risco para o desenvolvimento de DCNT. Essa complexidade é atribuída a diversos fatores como genética, biológica e comportamental que são comuns entre elas (https://www.scielo.br/j/rbepid/a/gYrgkcRnGTgWTjVTNSD9MNS/?lang=pt)


| **Variáveis de DCNT**        	|                      	| **População 2019** 	| **Sem depressão** 	| **Com depressão** 	| **X²** * 	| **p** * 	|
|------------------------------	|----------------------	|--------------------	|-------------------	|-------------------	|----------	|---------	|
|                              	|                      	| n = 64.664         	| n = 57.816        	| n = 6.848         	|          	|         	|
| **Artrite**                  	| Teve diagnóstico     	| 4,87%              	| 3,94%             	| 12,72%            	| 1017,191 	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 95,13%             	| 96,06%            	| 87,28%            	| ---      	| ---     	|
| **AVC**                      	| Teve diagnóstico     	| 1,08%              	| 0,82%             	| 3,23%             	| 332,787  	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 98,92%             	| 99,18%            	| 96,77%            	| ---      	| ---     	|
| **Doenças cardiovasculares** 	| Teve diagnóstico     	| 3,06%              	| 2,47%             	| 7,96%             	| 621,4531 	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 96,94%             	| 97,53%            	| 92,04%            	| ---      	| ---     	|
| **Hipertensão**              	| Teve diagnóstico     	| 17,77%             	| 16,44%            	| 28,86%            	| 639,0247 	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 82,23%             	| 83,56%            	| 71,14%            	| ---      	| ---     	|
| **Hipercolesterolemia**      	| Teve diagnóstico     	| 12,78%             	| 11,65%            	| 21,89%            	| 535,933  	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 87,22%             	| 88,35%            	| 78,11%            	| ---      	| ---     	|
| **Diabetes**                 	| Teve diagnóstico     	| 5,06%              	| 4,54%             	| 9,33%             	| 276,6615 	| 0,0000  	|
|                              	| Não teve diagnóstico 	| 94,94%             	| 95,46%            	| 90,67%             	| ---      	| ---     	|
| **Obesidade**                	| Sim                  	| 20,93%             	| 20,23%            	| 26,82%            	| 158,9776 	| 0,0001  	|
|                              	| Não                  	| 79,07%             	| 79,77%            	| 73,18%            	| ---      	| ---     	|

\* Teste X² de variáveis de DCNT confrontadas com pessoas com depressão (PHQ9 score >= 10)

A partir dessas análises, levamos para o modelo final (regressão) todas as variáveis de hábitos de vida e doenças crônicas não transmissíveis que possuem associação com o alto potencial de depressão.

### Modelos preditivos para classificação

A primeira tabela abaixo os resultados de diferentes combinações de variáveis no modelo de regressão. Cada linha representa uma combinação específica de variáveis e os valores nas colunas "Acc. Treino" e "Acc. Teste" indicam a acurácia alcançada pelo modelo nos conjuntos de treino e teste, respectivamente. Além disso, a tabela também fornece métricas adicionais como precisão (P), recall (R), pontuação F1 (F1) e área sob a curva (AUC) para cada conjunto de treino e teste.

| Váriaveis selecionadas             | Acc. Treino   | Acc. Teste   | P. Treino   | P. Teste   | R. Treino   | R. Teste   | F1 Treino   | F1 Teste       | AUC Treino   | AUC Teste      |
|:-----------------------------------|:--------------|:-------------|:------------|:-----------|:------------|:-----------|:------------|:---------------|:-------------|:---------------|
| Apenas hábitos                     | 55.95%        | 55.68%       | 12.95%      | 12.94%     | 54.70%      | 55.10%     | 20.94%      | 20.96% ± 0.65% | 55.40%       | 55.42% ± 0.97% |
| Apenas doenças crônicas            | 72.84%        | 71.83%       | 18.99%      | 18.62%     | 44.33%      | 45.37%     | 26.59%      | 26.36% ± 0.45% | 60.36%       | 60.26% ± 0.37% |
| Apenas hábitos e doenças crônicas  | 69.49%        | 69.74%       | 18.43%      | 18.58%     | 51.04%      | 51.02%     | 27.08%      | 27.23% ± 0.34% | 61.42%       | 61.55% ± 0.38% |
| Apenas variáveis sociodemográficos | 57.05%        | 56.56%       | 15.81%      | 15.70%     | 69.71%      | 70.06%     | 25.77%      | 25.65% ± 0.30% | 62.62%       | 62.50% ± 0.46% |
| Todas as varáveis                  | 65.80%        | 65.90%       | 19.29%      | 19.28%     | 64.79%      | 64.46%     | 29.73%      | 29.68% ± 1.09% | 65.36%       | 65.27% ± 1.35% |

A métrica de acurácia não é adequada para este problema devido ao desbalanceamento das classes. Se tivéssemos um modelo que classificasse todas as instâncias como não-depressão, teríamos uma acurácia próxima a 90%. Por essa razão, é necessário avaliar outras métricas, como precisão, revocação, F1-score e AUC, para realizar comparações. No caso desse problema, optaremos pelo F1-score como métrica padrão, pois ele oferece um equilíbrio entre precisão e revocação, sendo adequado para situações em que as classes estão desbalanceadas.

Ao analisar a tabela, podemos observar que o modelo "Apenas doenças crônicas" apresenta um F1-score superior em comparação com os modelos "Apenas hábitos" e "Apenas variáveis sociodemográficas". Isso indica que o grupo de variáveis relacionadas a doenças crônicas é mais relevante para o modelo do que os outros grupos. Esse resultado está em consonância com o nosso modelo teórico, o qual elenca os comportamentos de saúde inadequados como fatores comuns para as doenças crônicas não transmissíveis e a depressão. 

Em seguida podemos ver a tabela de coeficientes encontrados pela regressão logistica.

| Variáveis                  |   Apenas hábitos |   Apenas doenças crônicas |   Apenas hábitos e doenças crônicas |   Apenas variáveis sociodemográficos |   Todas as varáveis      |
|:---------------------------|-----------------:|--------------------------:|------------------------------------:|-------------------------------------:|-------------------------:|
| Intercepto                 |             0.09 |                     -0.36 |                               -0.37 |                                 0.50 |                     0.30 |
| Ultraprocessados           |             0.33 |                           |                                0.51 |                                      |                     0.49 |
| Exercício Físico           |            -0.31 |                           |                               -0.27 |                                      |                    -0.23 |
| Tabagismo                  |             0.43 |                           |                                0.50 |                                      |                     0.57 |
| Consumo Álcool             |            -0.26 |                           |                               -0.17 |                                      |                    -0.02 |
| Câncer                     |                  |                      0.60 |                                0.61 |                                      |                     0.51 |
| Hipertensão                |                  |                      0.33 |                                0.32 |                                      |                     0.35 |
| Diabetes                   |                  |                      0.44 |                                0.43 |                                      |                     0.50 |
| Cardiovascular             |                  |                      0.82 |                                0.79 |                                      |                     0.88 |
| Hipercolesterolemia        |                  |                      0.42 |                                0.45 |                                      |                     0.46 |
| AVC                        |                  |                      0.83 |                                0.75 |                                      |                     0.73 |
| Artrite                    |                  |                      0.97 |                                0.97 |                                      |                     0.89 |
| Obesidade                  |                  |                      0.17 |                                0.18 |                                      |                     0.19 |
| Sexo                       |                  |                           |                                     |                                -1.05 |                    -0.96 |
| Estado Civil               |                  |                           |                                     |                                -0.39 |                    -0.38 |
| Classificação Escolaridade |                  |                           |                                     |                                -0.17 |                     0.11 |
| Classificação Idade        |                  |                           |                                     |                                 0.48 |                    -0.24 |
| Classificação Renda        |                  |                           |                                     |                                -0.26 |                    -0.27 |

Observa-se que os coeficientes mantiveram-se praticamente inalterados quando todos os atributos foram combinados em um único modelo.

A próxima tabela apresenta os resultados de diferentes abordagens experimentadas no modelo. Cada linha representa uma abordagem específica, como remoção de linhas nulas, substituição de valores faltantes pela média, substituição de valores faltantes pela mediana, uso de SMOTE (técnica de oversampling) e melhores resultados obtidos através de um 'Grid Search', executado pelo codigo abaixo:

| Abordagens experimentadas    | F1 Treino   | F1 Teste       | AUC Treino   | AUC Teste      |
|:-----------------------------|:------------|:---------------|:-------------|:---------------|
| Removendo Linhas Nulas       | 29.73%      | 29.68% ± 1.09% | 65.36%       | 65.27% ± 1.35% |
| Substituindo NA pela média   | 28.67%      | 28.75% ± 0.75% | 65.39%       | 65.45% ± 0.96% |
| Substituindo NA pela mediana | 28.80%      | 28.84% ± 0.72% | 65.53%       | 65.54% ± 0.93% |
| SMOTE                        | 29.43%      | 29.18% ± 0.81% | 65.37%       | 65.10% ± 1.06% |
| Melhor resultado Grid Search | 29.67%      | 29.70% ± 1.05% | 65.29%       | 65.32% ± 1.30% |
| Floresta Randomica           | 28.54%      | 28.38% ± 0.65% | 64.47%       | 64.15% ± 0.90% |
| Árvore de Decisão            | 28.39%      | 28.16% ± 0.58% | 64.86%       | 64.44% ± 0.83% |

Os resultados de testes de estratificação realizados com base em diferentes características, como renda, sexo, idade e região, são apresentados na tabela abaixo. Cada linha representa um teste específico e as colunas fornecem as pontuações F1 e AUC para cada teste, tanto para o conjunto de treino quanto para o conjunto de teste.

| Testes de estratificação	 | F1 Treino   | F1 Teste       | AUC Treino   | AUC Teste      |
|:--------------------------|:------------|:---------------|:-------------|:---------------|
| Renda Baixa               | 32.55%      | 32.45% ± 0.85% | 65.31%       | 65.15% ± 1.00% |
| Renda Alta                | 24.36%      | 24.07% ± 0.71% | 63.69%       | 63.26% ± 1.02% |
| Sexo Mulher               | 33.69%      | 33.25% ± 0.83% | 61.58%       | 61.16% ± 0.76% |
| Sexo Homem                | 18.55%      | 18.25% ± 0.78% | 64.15%       | 63.67% ± 1.12% |
| Idade < 40                | 25.45%      | 25.38% ± 0.77% | 63.30%       | 63.20% ± 1.10% |
| Idade >= 40               | 32.86%      | 32.77% ± 0.37% | 66.40%       | 66.29% ± 0.48% |
| Idade [20, 29]            | 25.31%      | 24.93% ± 0.73% | 63.07%       | 62.54% ± 1.26% |
| Idade [30, 39]            | 26.22%      | 26.19% ± 1.70% | 64.24%       | 64.34% ± 2.47% |
| Idade [40, 49]            | 31.94%      | 31.62% ± 1.25% | 66.13%       | 65.71% ± 1.45% |
| Idade [50, 59]            | 34.98%      | 34.57% ± 1.23% | 67.87%       | 67.40% ± 1.28% |
| Região Norte              | 27.10%      | 26.86% ± 1.86% | 65.43%       | 65.07% ± 2.37% |
| Região Nordeste           | 30.55%      | 30.28% ± 1.05% | 64.51%       | 64.27% ± 1.25% |
| Região Sudeste            | 31.60%      | 31.02% ± 0.64% | 66.38%       | 65.71% ± 0.82% |
| Região Sul                | 28.50%      | 27.97% ± 2.24% | 65.61%       | 64.87% ± 2.78% |
| Região Centro Oeste       | 30.47%      | 29.33% ± 2.57% | 66.34%       | 64.83% ± 3.20% |

As próximas tabelas, comparam as diferenças entre cada coeficiente encontrado na regressão por meio da estratificação em diversas variáveis.

Na proxima, temos a comparação dos coeficientes da regressão estratificados por Renda Baixa e Renda Alta:

| Variáveis                  |   Renda Baixa |   Renda Alta |   Diferença |
|:---------------------------|--------------:|-------------:|------------:|
| Intercepto                 |         -0.05 |         0.54 |    **0.59** |
| Ultraprocessados           |          0.47 |         0.49 |        0.03 |
| Exercício Físico           |         -0.15 |        -0.34 |       -0.19 |
| Tabagismo                  |          0.60 |         0.53 |       -0.06 |
| Consumo Álcool             |         -0.06 |         0.04 |        0.11 |
| Câncer                     |          0.58 |         0.48 |       -0.10 |
| Hipertensão                |          0.32 |         0.39 |        0.06 |
| Diabetes                   |          0.50 |         0.51 |        0.01 |
| Cardiovascular             |          0.94 |         0.79 |       -0.15 |
| Hipercolesterolemia        |          0.46 |         0.47 |        0.01 |
| AVC                        |          0.81 |         0.59 |       -0.21 |
| Artrite                    |          0.86 |         0.93 |        0.06 |
| Obesidade                  |          0.21 |         0.16 |       -0.05 |
| Sexo                       |         -1.00 |        -0.91 |        0.09 |
| Estado Civil               |         -0.41 |        -0.30 |        0.11 |
| Classificação Escolaridade |          0.27 |         0.02 |       -0.25 |
| Classificação Idade        |          0.00 |        -0.62 |   **-0.62** |

Observa-se que existem duas grandes diferenças, principalmente nos atributos de idade e intercepto. Nota-se que indivíduos com renda alta (superior a um salário mínimo) apresentam uma tendência maior em relação à depressão. Além disso, o fator idade possui um efeito mais significativo no grupo de alta renda, onde quanto maior a idade, menor é o efeito depressivo. No entanto, no estrato de baixa renda, essa variável não demonstra ter um efeito significativo.

A seguir, a comparação dos coeficientes da regressão estratificados por Sexo Mulher e Sexo Homem.

| Váriaveis                  |   Sexo Mulher |   Sexo Homem |   Diferença |
|:---------------------------|--------------:|-------------:|------------:|
| Intercepto                 |         -0.04 |        -0.10 |       -0.06 |
| Ultraprocessados           |          0.37 |         0.68 |        0.31 |
| Exercício Físico           |         -0.22 |        -0.22 |        0.00 |
| Tabagismo                  |          0.57 |         0.61 |        0.04 |
| Consumo Álcool             |          0.08 |        -0.18 |       -0.27 |
| Câncer                     |          0.58 |         0.31 |       -0.27 |
| Hipertensão                |          0.27 |         0.47 |        0.19 |
| Diabetes                   |          0.46 |         0.60 |        0.14 |
| Cardiovascular             |          0.81 |         0.96 |        0.16 |
| Hipercolesterolemia        |          0.43 |         0.53 |        0.11 |
| AVC                        |          0.63 |         0.85 |        0.22 |
| Artrite                    |          0.83 |         1.19 |        0.36 |
| Obesidade                  |          0.16 |         0.26 |        0.10 |
| Estado Civil               |         -0.24 |        -0.69 |   **-0.45** |
| Classificação Escolaridade |         -0.01 |         0.39 |        0.41 |
| Classificação Idade        |         -0.27 |        -0.05 |        0.22 |
| Classificação Renda        |         -0.31 |        -0.28 |        0.03 |

Aqui podemos observar uma diferença relevante na variável estado civil. Viver com um cônjuge apresenta um efeito não depressivo, mas parece ter uma maior relevância no sexo masculino.

A seguir, a comparação dos coeficientes da regressão estratificados por Idade < 40 e Idade >= 40.

| Váriaveis                  |   Idade < 40 |   Idade >= 40 |   Diferença |
|:---------------------------|-------------:|--------------:|------------:|
| Intercepto                 |         0.18 |          0.13 |       -0.05 |
| Ultraprocessados           |         0.58 |          0.48 |       -0.10 |
| Exercício Físico           |        -0.07 |         -0.35 |       -0.27 |
| Tabagismo                  |         0.67 |          0.48 |       -0.19 |
| Consumo Álcool             |         0.11 |         -0.14 |       -0.25 |
| Câncer                     |         0.43 |          0.53 |        0.11 |
| Hipertensão                |         0.58 |          0.24 |       -0.34 |
| Diabetes                   |         0.26 |          0.52 |        0.26 |
| Cardiovascular             |         1.17 |          0.77 |   **-0.40** |
| Hipercolesterolemia        |         0.52 |          0.42 |       -0.10 |
| AVC                        |         1.12 |          0.62 |   **-0.50** |
| Artrite                    |         1.03 |          0.85 |       -0.18 |
| Obesidade                  |         0.25 |          0.14 |       -0.11 |
| Sexo                       |        -1.11 |         -0.87 |        0.25 |
| Estado Civil               |        -0.38 |         -0.37 |        0.01 |
| Classificação Escolaridade |        -0.05 |          0.27 |        0.31 |
| Classificação Renda        |        -0.14 |         -0.40 |       -0.26 |

Aqui podemos notar uma diferença significativa nos atributos relacionados a doenças cardiovasculares e AVC.

A seguir, a comparação dos coeficientes da regressão estratificados por grupos de Idade: 20 à 29, 30 à 39, 40 à 49 e 50 à 59

| Váriáveis                  |   Idade [20, 29] |   Idade [30, 39] |   Idade [40, 49] |   Idade [50, 59] |
|:---------------------------|-----------------:|-----------------:|-----------------:|-----------------:|
| Intercepto                 |             0.19 |             0.16 |             0.23 |             0.03 |
| Ultraprocessados           |             0.58 |             0.55 |             0.56 |             0.24 |
| Exercício Físico           |             0.04 |            -0.16 |            -0.22 |            -0.52 |
| Tabagismo                  |             0.66 |             0.67 |             0.48 |             0.52 |
| Consumo Álcool             |             0.14 |             0.10 |            -0.09 |            -0.24 |
| Câncer                     |             0.46 |             0.43 |             0.55 |             0.56 |
| Hipertensão                |             0.73 |             0.54 |             0.32 |             0.22 |
| Diabetes                   |             0.52 |             0.21 |             0.71 |             0.47 |
| Cardiovascular             |             1.58 |             0.99 |             0.68 |             0.85 |
| Hipercolesterolemia        |             0.48 |             0.56 |             0.39 |             0.49 |
| AVC                        |             1.02 |             1.15 |             0.65 |             0.61 |
| Artrite                    |             0.82 |             1.12 |             0.91 |             0.88 |
| Obesidade                  |             0.34 |             0.20 |             0.18 |             0.10 |
| Sexo                       |            -1.19 |            -1.05 |            -0.94 |            -0.78 |
| Estado Civil               |            -0.30 |            -0.43 |            -0.56 |            -0.21 |
| Classificação Escolaridade |            -0.33 |             0.18 |             0.32 |             0.16 |
| Classificação Renda        |             0.02 |            -0.25 |            -0.38 |            -0.35 |

Ao analisar esta tabela, podemos observar a variação da importância de alguns fatores ao longo do tempo. Por exemplo, os exercícios físicos parecem ter um efeito maior em idades mais avançadas.

Na proxima tabela, são comparados os coeficientes da regressão logística para diferentes variáveis, estratificados por Região geográfica: Norte, Nordeste, Sudeste, Sul e Centro-Oeste. A tabela mostra as diferenças nos valores dos coeficientes entre as diferentes regiões, permitindo uma análise das influências regionais nas relações entre as variáveis estudadas.


| Variáveis                  |   Região Norte |   Região Nordeste |   Região Sudeste |   Região Sul |   Região Centro Oeste |
|:---------------------------|---------------:|------------------:|-----------------:|-------------:|----------------------:|
| Intercepto                 |          -0.08 |              0.28 |             0.23 |         0.42 |                  1.00 |
| Ultraprocessados           |           0.81 |              0.61 |             0.28 |         0.54 |                  0.11 |
| Exercício Físico           |          -0.03 |             -0.21 |            -0.30 |        -0.25 |                 -0.43 |
| Tabagismo                  |           0.43 |              0.60 |             0.57 |         0.58 |                  0.64 |
| Consumo Álcool             |           0.23 |             -0.14 |             0.01 |        -0.13 |                 -0.02 |
| Câncer                     |           0.62 |              0.52 |             0.50 |         0.81 |                 -0.00 |
| Hipertensão                |           0.37 |              0.40 |             0.21 |         0.44 |                  0.32 |
| Diabetes                   |           0.66 |              0.43 |             0.42 |         0.51 |                  0.51 |
| Cardiovascular             |           0.99 |              0.95 |             1.01 |         0.40 |                  0.76 |
| Hipercolesterolemia        |           0.38 |              0.47 |             0.52 |         0.50 |                  0.39 |
| AVC                        |           0.37 |              0.74 |             0.60 |         0.92 |                  1.35 |
| Artrite                    |           0.93 |              0.98 |             1.00 |         0.56 |                  0.89 |
| Obesidade                  |           0.35 |              0.05 |             0.42 |         0.13 |                  0.03 |
| Sexo                       |          -1.07 |             -0.88 |            -0.93 |        -0.87 |                 -1.23 |
| Estado Civil               |          -0.41 |             -0.36 |            -0.43 |        -0.29 |                 -0.36 |
| Classificação Escolaridade |           0.40 |              0.05 |             0.09 |         0.27 |                 -0.22 |
| Classificação Idade        |          -0.11 |             -0.29 |            -0.07 |        -0.30 |                 -0.62 |
| Classificação Renda        |          -0.42 |             -0.16 |            -0.26 |        -0.49 |                 -0.18 |

O algoritmo de árvore de decisão, assim como a regressão, logística também tem a vantagem de ser interpretável. A figura abaixo ilustra uma árvore de decisão construída a partir dos dados fornecidos. Essa representação visual demonstra como o algoritmo divide os dados em diferentes ramos, com base em atributos relevantes, até chegar a uma decisão final. Cada nó da árvore representa uma condição que é testada, e as ramificações indicam os possíveis resultados dessa condição.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/decistion_tree_p.svg)

Ao analisar o gráfico da árvore de decisão, é possível observar que o atributo mais eficaz na separação das classes (depressão ou não) é o sexo. Quando uma pessoa é do sexo masculino e não possui hipertensão, o algoritmo classifica como não-depressiva, uma vez que 70,1% das amostras nessa categoria não apresentam depressão, representando 38,7% de todos os dados. Por outro lado, o algoritmo identifica a depressão em 78,5% dos casos em que a pessoa é do sexo feminino e tem artrite, embora esse cenário seja pouco representativo, abrangendo apenas 4,1% das amostras.

A tabela abaixo compara os coeficientes da regressão logística com os níveis de importância de cada variável de entrada da floresta randômica e a árvore de decisão.

| Variáveis                  | Regressão Logistica | Árvore de Decisão | Floresta Randomica |
|:---------------------------|--------------------:|------------------:|-------------------:|
| Intercepto                 |                0.30 |                   |                    |
| Ultraprocessados           |                0.48 |              0.00 |               0.00 |
| Exercício Físico           |               -0.23 |              0.03 |               0.02 |
| Tabagismo                  |                0.56 |              0.04 |               0.07 |
| Consumo Álcool             |               -0.02 |              0.01 |               0.01 |
| Câncer                     |                0.48 |              0.00 |               0.00 |
| Hipertensão                |                0.35 |              0.11 |           **0.12** |
| Diabetes                   |                0.49 |              0.02 |               0.00 |
| Cardiovascular             |            **0.85** |              0.03 |               0.00 |
| Hipercolesterolemia        |                0.46 |              0.08 |               0.06 |
| AVC                        |                0.68 |              0.00 |               0.00 |
| Artrite                    |            **0.88** |              0.09 |           **0.10** |
| Obesidade                  |                0.19 |              0.02 |               0.01 |
| Sexo                       |           **-0.95** |              0.46 |           **0.51** |
| Estado Civil               |               -0.38 |              0.07 |               0.06 |
| Classificação Escolaridade |                0.11 |              0.00 |               0.00 |
| Classificação Idade        |               -0.23 |              0.01 |               0.01 |
| Classificação Renda        |               -0.27 |              0.04 |               0.04 |

Observa-se que tanto a Floresta Randomica quanto as Árvores de Decisão apresentam importâncias relativamente semelhantes, uma vez que são métodos de classificação semelhantes. Ao comparar a Regressão Logística e a Floresta Randomica, ambos elegem o atributo "Sexo" como o mais importante para a classificação. O segundo atributo mais importante na Regressão Logística, "Artrite", é o terceiro mais importante na Floresta Randomica. No entanto, o atributo "Cardiovascular", que é o terceiro mais importante na Regressão Logística, tem importância praticamente zero na Floresta Randomica.

### Resultados testes

Por fim, a tabala abaixo compara os diferentes tipos de algoritmos experimentados no conjunto de teste final: Regressão Logística, Árvore de Decisão e Floresta Randomica.

|                  | Logistic Regression   | Decision Tree   | Random Forest   |
|:-----------------|:----------------------|:----------------|:----------------|
| Acurácia Treino  | 65.74%                | 62.64%          | 59.81%          |
| Acurácia Teste   | **65.30%**            | 62.32%          | 59.17%          |
| Precisão Treino  | 19.25%                | 18.15%          | 17.72%          |
| Precisão Teste   | **18.49%**            | 17.29%          | 16.90%          |
| Revocação Treino | 64.72%                | 66.82%          | 71.36%          |
| Revocação Teste  | 66.39%                | 67.21%          | **72.45%**      |
| F1 Treino        | 29.67%                | 28.54%          | 28.39%          |
| F1 Teste         | **28.93%**            | 27.51%          | 27.40%          |
| AUC Treino       | 71.40%                | 69.95%          | 70.95%          |
| AUC Teste        | **71.57%**            | 69.56%          | 70.55%          |

Abaixo podemos ver a curva ROC entre estes 3 modelos.
![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/roc.png)

Tanto a curva ROC quanto a tabela concordam em eleger a Regressão Logística como o melhor algoritmo para o problema em questão. Podemos observar na curva ROC que o modelo de Regressão Logística (curva azul) está acima das outras duas curvas em praticamente todos os pontos de tradeoff, o que é consistente com seu maior AUC e maior pontuação F1. No entanto, é importante notar que na métrica de revocação, a Floresta Randomica mostra um desempenho superior aos demais. A Floresta Randomica utiliza uma abordagem de conjunto (ensemble) em que cada Árvore de Decisão é treinada com uma amostra aleatória dos dados de treinamento e, em seguida, suas classificações são agregadas para obter uma previsão final, a vantagem da Floresta Randomica em relação à Regressão Logística é sua capacidade de capturar interações complexas e não lineares entre as variáveis de entrada.

Abaixo está a matriz de confusão para o melhor modelo, que utiliza regressão logística no conjunto de teste. Ao analisar a matriz, podemos observar que há um grande número de falsos positivos, o que resulta na precisão baixa previamente relatada. No entanto, em relação aos casos de depressão, o modelo apresenta um número menor de falsos negativos, resultando em uma taxa de revocação de aproximadamente 66%.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/cm.png)



# Conclusão
> Destacar as principais conclusões obtidas no desenvolvimento do projeto.
>
> Destacar os principais desafios enfrentados.
>
> Principais lições aprendidas.
>

Neste trabalho, o objetivo foi identificar os fatores relacionados à depressão com base na literatura existente. As questões de pesquisa abordaram diversos aspectos.

Investigamos quais hábitos de vida estão associados à depressão por meio da análise dos coeficientes da regressão logística. Constatamos que o tabagismo e o alto consumo de alimentos ultraprocessados possuem uma associação positiva com a depressão, enquanto o exercício físico apresenta uma associação inversa, ou seja, negativa. Isto indica prevalência de depressão em pessoas que não praticam exercício físico regularmente, conforme descrito pela literatura.

Além disso, procuramos quantificar o grau de impacto de cada hábito, considerando tanto as influências positivas quanto negativas. Utilizando a regressão logística, pudemos identificar a influência de certos hábitos. Por exemplo, observamos que o tabagismo parece ter um impacto maior do que o consumo de alimentos ultraprocessados.

Durante a análise dos coeficientes da regressão, notamos que a influência desses fatores varia ao longo do curso da vida e de variáveis sociodemográficas. Um exemplo é a influência crescente da prática de exercícios físicos à medida que a idade avança. Esta questão pode estar relacionada à deterioração da condição física do indivíduo ao passar dos anos, aumentando a dependência de terceiros e impactando a saúde mental.

Descobrimos que os comportamentos de saúde e/ou doenças crônicas não transmissíveis também desempenham um papel determinante no diagnóstico da depressão. Grande parte do peso dos coeficientes recai sobre as doenças crônicas, perdendo apenas para a variável sociodemográfica do sexo.

Durante o desenvolvimento do projeto, enfrentamos desafios significativos. Um deles foi lidar com a quantidade de dados faltantes e variáveis ausentes nos indicadores iniciais baseados na PNS. Especificamente, a falta de informações sobre o consumo de álcool e a prática de atividade física representou um obstáculo importante. 

Além disso, deparamos com o desafio do desbalanceamento dos dados na classificação dos casos de depressão. A proporção entre indivíduos classificados como depressivos e não depressivos era desigual, sendo que apenas 10,6% dos participantes foram identificados como depressivos. Inicialmente, utilizamos o algoritmo SMOTE para gerar dados sintéticos na classe minoritária, porém posteriormente optamos por ponderar a classe majoritária durante o treinamento dos modelos de classificação, o que resultou em melhores resultados.

Esses desafios evidenciaram a importância de abordar estrategicamente os dados faltantes e encontrar soluções adequadas para lidar com os desequilíbrios nas classes. Foi essencial buscar abordagens alternativas, como a modificação dos critérios de classificação e o ajuste das estratégias de modelagem, a fim de obter resultados mais precisos e confiáveis.

# Trabalhos Futuros

No âmbito dos trabalhos futuros, sugerimos explorar a utilização de técnicas de aprendizado não supervisionado para a seleção de features no problema em questão. Essa abordagem oferece a oportunidade de descobrir relações ainda não descritas na literatura, por meio da exploração dos dados, identificando padrões ocultos e estruturas subjacentes relevantes para a compreensão do problema. A aplicação dessas técnicas pode fornecer insights adicionais e aprofundar a compreensão dos fatores associados à doença em estudo.

Adicionalmente, consideramos relevante explorar a disponibilidade de outras bases de dados brasileiras, como Vigitel e PeNSE, para realizar testes e validações do modelo desenvolvido em diferentes segmentos da população. Essas bases de dados representam amostras representativas de diversas regiões e grupos demográficos, permitindo a generalização e a avaliação da robustez do modelo. Essa abordagem ampliada pode proporcionar uma visão mais abrangente sobre a relação entre os fatores estudados e a doença, contribuindo para embasar a tomada de decisões e a formulação de políticas públicas mais efetivas e direcionadas.

# Cronograma

Semanas | Tarefas                                           | Conclusão
----- |---------------------------------------------------| -----
Semana 01 (16/04 - 22/04) | Definir escopo do projeto e revisão bibliográfica | :heavy_check_mark:
Semana 02 (23/04 - 29/04) | Compreensão do dados                              | :heavy_check_mark:
Semana 03 (30/04 - 06/05) | Processamento dos dados                           | :heavy_check_mark:
Semana 04 (07/05 - 13/05) | Processamento dos dados                           | :heavy_check_mark:
Semana 05 (14/05 - 20/05) | Análise exploratória e Entrega 2                  | :heavy_check_mark:
Semana 06 (21/05 - 27/05) | Modelagem da solução                              | :heavy_check_mark:
Semana 07 (28/05 - 03/06) | Modelagem da solução                              | :heavy_check_mark:
Semana 08 (04/06 - 10/06) | Análise e discussão dos resultados                | :heavy_check_mark:
Semana 09 (11/06 - 17/06) | Relatório                                         | :heavy_check_mark:
Semana 10 (18/06 - 24/06) | Apresentação e Entrega Final                      | :heavy_check_mark:


# Referências Bibliográficas

1. 	Hunter DJ, Reddy KS. Noncommunicable Diseases. N Engl J Med [Internet]. 2013 [cited 2023 Apr 14];369(14):1336–43. Available from: https://www.who.int/health-topics/noncommunicable-diseases#tab=tab_1

2. 	World Health Organisation. Mental health in emergencies [Internet]. 2019 [cited 2023 Apr 14]. p. 1–70. Available from: https://www.who.int/news-room/fact-sheets/detail/mental-health-in-emergencies

3. 	Soares B, Kanevsky G, Teng CT, Pérez-Esparza R, Bonetto GG, Lacerda ALT, et al. Prevalence and Impact of Treatment-Resistant Depression in Latin America: a Prospective, Observational Study. Psychiatr Q [Internet]. 2021 Dec 1 [cited 2023 Apr 14];92(4):1797–815. Available from: /pmc/articles/PMC8531108/
 	
4. 	Chisholm D, Sanderson K, Ayuso-Mateos JL, Saxena S. Reducing the global burden of depression: Population-level analysis of intervention cost-effectiveness in 14 world regions. Br J Psychiatry [Internet]. 2004 May [cited 2023 Apr 14];184(MAY):393–403. Available from: https://pubmed.ncbi.nlm.nih.gov/15123502/
 	
5. 	Barros MB de A, Medina L de PB, Lima MG, de Azevedo RCS, Sousa NF da S, Malta DC. Association between health behaviors and depression: findings from the 2019 Brazilian National Health Survey. Rev Bras Epidemiol [Internet]. 2021 Dec 10 [cited 2023 Jun 21];24:e210010. Available from: https://doi.org/10.1590/1980-549720210010.supl.2
 	
6. 	Theme Filha MM, Souza Junior PRB de, Damacena GN, Szwarcwald CL. Prevalence of chronic non-communicable diseases and association with self-rated health: National Health Survey, 2013. Rev Bras Epidemiol [Internet]. 2015 Dec 1 [cited 2023 Jun 23];18 Suppl 2:83–96. Available from: https://pubmed.ncbi.nlm.nih.gov/27008605/
 	
7. 	Lotfaliany M, Bowe SJ, Kowal P, Orellana L, Berk M, Mohebbi M. Depression and chronic diseases: Co-occurrence and communality of risk factors. J Affect Disord. 2018 Dec 1;241:461–8.
 	
8. 	Sousa NF da S, Barros MB de A, Medina L de PB, Malta DC, Szwarcwald CL. Association of major depressive disorder with chronic diseases and multimorbidity in Brazilian adults, stratified by gender: 2019 National Health Survey. Rev Bras Epidemiol. 2021;24.
 	
9. 	Stopa SR, Szwarcwald CL, Oliveira MM de, Gouvea E de CDP, Vieira MLFP, Freitas MPS de, et al. Pesquisa Nacional de Saúde 2019: histórico, métodos e perspectivas. Epidemiol e Serv saude  Rev do Sist Unico Saude do Bras [Internet]. 2020 [cited 2023 Apr 14];29(5):e2020315. Available from: http://scielo.iec.gov.br/scielo.php?script=sci_arttext&pid=S1679-49742020000500035&lng=pt&nrm=iso&tlng=pt
 	
10. dos Santos Costa C, Steele EM, de Faria FR, Monteiro CA. Score of ultra-processed food consumption and its association with sociodemographic factors in the Brazilian National Health Survey, 2019. Cad Saude Publica [Internet]. 2022 May 6 [cited 2023 Jun 21];38:e00119421. Available from: https://www.scielo.br/j/csp/a/QP4GrYT7cS6YCLrrTKtPvjp/?lang=en
 	
11. de Sousa KT, Marques ES, Levy RB, Azeredo CM. Food consumption and depression among Brazilian adults: results from the Brazilian National Health Survey, 2013. Cad Saude Publica [Internet]. 2019 Dec 20 [cited 2023 Jun 21];36(1):e00245818. Available from: https://www.scielo.br/j/csp/a/75WMGWKGMvLZXR9CbJWd7sP/?lang=en

 
### Estudo Bibliográfico

[Barros MBA, Lima MG, Azevedo RCS, Medina LBP, Lopes CS, Menezes PR, Malta DC. Depression and health behaviors in Brazilian adults - PNS 2013. Rev Saude Publica. 2017 Jun 1;51(suppl 1):8s. doi: 10.1590/S1518-8787.2017051000084. PMID: 28591352; PMCID: PMC5676399.](https://pubmed.ncbi.nlm.nih.gov/28591352/)

[Godos J, Bonaccio M, Al-Qahtani WH, Marx W, Lane MM, Leggio GM, Grosso G. Ultra-Processed Food Consumption and Depressive Symptoms in a Mediterranean Cohort. Nutrients. 2023 Jan 18;15(3):504. doi: 10.3390/nu15030504. PMID: 36771211; PMCID: PMC9919031.](https://pubmed.ncbi.nlm.nih.gov/36771211/)

[Tian YR, Deng CY, Xie HC, Long QJ, Yao Y, Deng Y, Zhao H, Li Y, Liu H, Xiao L. Ultra-processed food intake and risk of depression: a systematic review. Nutr Hosp. 2023 Feb 15;40(1):160-176. English. doi: 10.20960/nh.03723. PMID: 36537321.](https://pubmed.ncbi.nlm.nih.gov/36537321/)

[Melo, A. P. S., Bonadiman, C. S. C., Andrade, F. M. de ., Pinheiro, P. C., & Malta, D. C.. (2023). Depression Screening in a population-based study: Brazilian National Health Survey 2019. Ciência & Saúde Coletiva, 28(4), 1163–1174. https://doi.org/10.1590/1413-81232023284.14912022](https://www.scielo.br/j/csc/a/wWKFtv8ZVZZTwVDM94Q3gFt/)

[Elizabeth L, Machado P, Zinöcker M, Baker P, Lawrence M. Ultra-Processed Foods and Health Outcomes: A Narrative Review. Nutrients. 2020 Jun 30;12(7):1955. doi: 10.3390/nu12071955. PMID: 32630022; PMCID: PMC7399967.](https://pubmed.ncbi.nlm.nih.gov/32630022/)

[Antunes JT, Dumont-Pena Érica, Silva AG da, Moutinho C dos S, Vieira MLFP, Malta DC. A saúde mental dos adolescentes brasileiros: Pesquisa Nacional de Saúde do Escolar de 2019. REME Rev Min Enferm.](https://periodicos.ufmg.br/index.php/reme/article/view/38984)

[Lane MM, Gamage E, Travica N, Dissanayaka T, Ashtree DN, Gauci S, Lotfaliany M, O'Neil A, Jacka FN, Marx W. Ultra-Processed Food Consumption and Mental Health: A Systematic Review and Meta-Analysis of Observational Studies. Nutrients. 2022 Jun 21;14(13):2568. doi: 10.3390/nu14132568. PMID: 35807749; PMCID: PMC9268228.](https://pubmed.ncbi.nlm.nih.gov/35807749/)

[Hecht EM, Rabil A, Martinez Steele E, Abrams GA, Ware D, Landy DC, Hennekens CH. Cross-sectional examination of ultra-processed food consumption and adverse mental health symptoms. Public Health Nutr. 2022 Nov;25(11):3225-3234. doi: 10.1017/S1368980022001586. Epub 2022 Jul 28. PMID: 35899785; PMCID: PMC9991859.](https://pubmed.ncbi.nlm.nih.gov/35899785/)
