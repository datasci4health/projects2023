# Projeto `Associação de fatores de estilo de vida e doenças crônicas não transmissíveis com depressão no Brasil`

### Project `Association of lifestyle factors and chronic non-communicable diseases with depression in Brazil`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp.

|Nome  | RA | Especialização|
|--|--|--|
| Beatriz Silva Nunes  | 167428  | Saúde - [Conta GitHub](https://github.com/beatrizsnunes)|
| Arthur Rezende Salles   | 166003  | Computação - Líder Github - [Conta GitHub](https://github.com/Arthur-Salles)|
| Anderson Nogueira Cotrim  | 163993  | Computação - [Conta GitHub](https://github.com/AndersonCotrim)|
| Guilherme Magalhães Soares  | 217241  | Elétrica - [Conta GitHub](https://github.com/gsoso01)|


# Introdução e Referenciais Teóricos

> Contextualização do projeto
> Caracterização do problema
> Motivação
> Relevância
> Trabalhos relacionados
> Indicação (bastante resumida) da análise proposta
> Indicação (bastante resumida) dos resultados alcançados


As doenças crônicas não transmissíveis (DCNT) são um problema de saúde pública global(1). DCNT estão associadas a diversos fatores de risco ou comportamentos de saúde inadequados, dentre eles o uso de tabaco, inatividade física, consumo excessivo de álcool e dietas não saudáveis(1). Entre as doenças crônicas temos a desordem depressiva ou depressão que é uma doença mental comum, caracterizada como uma persistência da tristeza e baixo interesse ou prazer em atividades anteriormente colocadas como comuns ou agradáveis(2)(3).

A depressão afeta cerca de 5% da população adulta mundial(2). O tratamento da depressão é complexo e infelizmente ineficaz, reduz somente cerca de um terço da carga da desordem depressiva(4). Com isso, a prevenção é a melhor forma de combater a depressão, similarmente a situação de outras doenças crônicas não transmissíveis como a obesidade.

Estudos prévios têm demonstrado associações entre depressão e comportamentos de saúde inadequados na população brasileira, com variações de acordo com características sociodemográficas, como sexo e renda(5,6). Além disso, fatores de risco têm sido associados ao diagnóstico de depressão, assim como a presença de outras doenças crônicas não transmissíveis, como diabetes e artrite. Essa associação não se deve apenas à reação depressiva decorrente da presença de uma doença, mas também ao compartilhamento de fatores de risco e mecanismos fisiopatológicos comuns entre a depressão e outras doenças crônicas não transmissíveis(7)(8). No entanto, existem poucos estudos que investigam essa relação em países de baixa e média renda(7).

Compreender a relação entre as doenças crônicas não transmissíveis e a depressão, considerando os fatores de risco associados à doença, bem como as particularidades sociodemográficas da população brasileira, é de extrema importância para o desenvolvimento de políticas públicas eficazes no combate ao avanço da depressão no país.

A utilização de inquéritos de saúde nacionais se torna extremamente pertinente para a compreensão da prevalência das doenças e dos fatores associados, visto que são produzidos com amostragens representativas da população brasileira, com o propósito de orientar diretrizes e políticas públicas de Saúde no país(9).

A partir desse cenário, o objetivo do estudo é buscar comportamentos de saúde inadequados e doenças crônicas não transmissíveis mais determinantes para o diagnóstico da depressão em um inquérito de saúde nacional possibilitando auxiliar na prevenção do desenvolvimento da depressão no Brasil.

*precisar adiconar o DAG QUE NÃO CONSEGUI



#### Apresentação inicial do projeto

[Link para vídeo de apresentação da proposta do projeto](https://drive.google.com/file/d/1uQ0wQsbig9BBA0OvvMyG8jLpcLTL104L/view?usp=share_link)




# Perguntas de Pesquisa e Objetivos

> Perguntas de pesquisa (revisadas e atualizadas) que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.
> Se a análise exploratória contribuiu para as perguntas de pesquisa, apresente aqui elementos de análise exploratória que ajudem a responder a questão.
> Objetivos principais e específicos

Algumas perguntas de pesquisa foram pensadas visando uma compreensão aprofundada da prevalência e fatores de risco associados à depressão no Brasil.

> a minha sugestão é não respondermos as questões aqui e sim nos resultados, aqui deixar apenas as questões;

 - Quais hábitos de vida estão associados à depressão? 
 - É possível quantificar o grau de impacto de cada hábito, considerando tanto as influências positivas quanto negativas? 
 - A influência desses fatores varia ao longo do curso da vida e de variaveis sociodemográficas?
- Será que os comportamentos de saúde e/ou doenças crônicas não transmissíveis são determinantes para o diagnóstico de depressão? 

Através dos experimentos exploratórios, análise de correlação e gráficos de distribuição, foram confirmados a associação entre a depressão (utilizando χ2 de Pearson) com os comportamentos de saúde inadequados e as doenças crônicas não transmissíveis elecandas no estudo, variaveis que estão em consonância com a literatura existente. Essas descobertas já contribuem para responder a primeira questão de pesquisa.

Para abordar a segunda questão, pretende-se utilizar a análise de regressão logística. Essa abordagem permitirá avaliar de forma mais precisa o grau de impacto de cada hábito, considerando tanto as influências positivas quanto as negativas, relacionadas à depressão.

Em relação à terceira questão, observou-se uma diferença na distribuição do potencial de depressão em relação à idade e renda. No entanto, os fatores que influenciam essa diferença serão confrontados e explorados por meio da análise de regressão logística, possibilitando uma compreensão mais aprofundada.

O objetivo geral do estudo é compreender os comportamentos de saúde inadequados e doenças crônicas não transmissíveis mais determinantes para o diagnóstico da depressão em um inquérito de saúde nacional.
Os objetivos específicos são:
1- Analisar quais comportamentos de saúde inadequados estão associados com o diagnóstico de depressão;
2- Analisar quais doenças crônicas não transmissiveis estão associadas com o diagnóstico de depressão;
3- Analisar quais varíaveis sociodemográficas estão associadas com o diagnóstico de depressão;
4- Determinar a importância dos comportamentos de saúde inadequados e das doenças crônicas não transmissíveis e das variáveis sociodemográficas para o diagnóstico de depressão;
5- Determinar quais variaveis são determinantes para o diagnóstico de depressão;

# Metodologia

> Abordagem adotada pelo projeto na busca pela resposta às perguntas de pesquisa.
> Justificar teoricamente, sempre que possível, a metodologia adotada.

Este trabalho de forma geral procura avaliar e descobrir os fatores de risco para a depressão no Brasil. Para este fim, abordaremos uma metodologia baseada quatro estratégias principais:

- Realização de um estudo bibliográfico, que permitirá entender os padrões esperados para cada pergunta de pesquisa.
- Análise exploratória, incluindo seleção e pré-processamento dos dados. 
- Realização de uma análise estatística, utilizando técnicas de estatística descritiva e visualização, como gráficos de dispersão, caixa, e barras, a fim de extrair conhecimento dos dados.
- Aplicação de técnicas de aprendizado de máquina (regressão), que nos permita uma análise aprofundada e a quantificação da relevância de cada característica para variável de interesse (depressão). 


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

Para conduzir as análises deste estudo, categorizamos as variáveis de interesse de acordo com os parâmetros utilizados na literatura, conforme apresentado a seguir:

*Variável dependente:*

A prevalência de depressão na população estudada foi avaliada através da aplicação do indicador PHQ9, que indica a severidade da doença em cinco intervalos: nenhum ou mínimo, leve, moderada, moderadamente grave e grave. Para as análises, as pessoas com pontuação igual ou superior a 10 pontos do indicador foram classificadas com depressão.

Apenas pessoas com idade entre 18 e 59 anos podem ser avaliadas neste índice. Portanto, o estudo foi restrito a essa faixa etária e as mulheres grávidas foram excluídas da análise devido a questões metodológicas específicas (n = 736), resultando em uma amostra final de 64.664 indivíduos.	

_Variáveis independentes de doenças crônicas não transmissíveis, comportamentos de saúde e sociodemográficas:_

Variáveis relacionadas às doenças crônicas não transmissíveis:

Presença de artrite, AVC, doenças cardiovasculares, hipertensão, hipercolesterolemia, diabetes: sim ou não;

Presença de obesidade: calculamos o IMC dos indivíduos (peso/altura²) e classificamos com obesidade, os indivíduos com IMC superior ou igual a 30 (sim/não).

_Variáveis independentes de doenças crônicas não transmissíveis, comportamentos de saúde e sociodemográficas:_

Variáveis relacionadas aos comportamentos de saúde:

Alimentação: aplicamos um score de consumo de produtos ultraprocessados de 0 a 10 pontos, o qual é baseado na resposta positiva de consumo no dia anterior dos seguintes alimentos[10]: 
1- Refrigerante; 
2- Suco de fruta em caixinha ou lata ou refresco em pó;
3- Bebida achocolatada ou iogurte com sabor; 
4- Salgadinho de pacote ou biscoito/bolacha salgado; 
5- Biscoito/bolacha doce ou recheado ou bolo de pacote; 
6- Sorvete, chocolate, gelatina, flan ou outra sobremesa industrializada; 7- Salsicha, linguiça, mortadela ou presunto; 
8- Pão de forma, de cachorro-quente ou de hambúrguer;
9- Margarina, maionese, ketchup ou outros molhos ultraprocessados; 10- Macarrão instantâneo, sopa de pacote, lasanha congelada ou outro prato congelado comprado pronto industrializado. 
Sendo que quanto maior a pontuação do score, maior o consumo de ultraprocessados, ou seja, menos saudável é a dieta. 

Exercício físico[5]: prática de exercício físico nos últimos 3 meses (sim/não).

Consumo de álcool[11]: consumo de bebidas alcoólica uma vez ou mais por mês (sim/não) 

Tabagismo[5]: faz uso de algum tipo de tabaco (sim/não)

Variáveis relacionadas ao perfil sociodemográfico:

Escolaridade: Sem instrução e fundamental incompleto, fundamental completo e médio incompleto, médio completo e superior incompleto, superior completo.

Sexo: feminino ou masculino

Idade [10]: 

Renda [5]:

Localidade: região geográfica dos indivíduos (Norte, Nordeste, Centro, Sul, Sudeste);


Nesta seção, apresentamos algumas características identificadas na base de dados selecionada, juntamente com os resultados da análise exploratória.

Abaixo temos um resumo do workflow dos experimentos realizados com esta base:

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/assets/e2_workflow.png)


** Arrumar workflow **
![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/assets/e2_specific_workflow.png)

Nas proximas seções decrevemos uma análise exploratoria inicial e mais detalhes desta base.

#### Características descritivas da população

Os gráficos abaixo descrevem a proporção em relação a sexo, cor ou raça das amostras da população. Onde podemos observar um balanceamento em gênero e a predominância parda na categoria cor ou raça.

![Sexo e cor/raça da população](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_sexo_cor.png)

Abaixo podemos observar curvas de distribuição dos indivíduos da base em relação à idade e peso, podemos notar que estas curvas estão num intervalo de valores a primeira vista aceitável indicando que, aparentemente, grande parte dos dados em relação a este atributo estão confiáveis. Mais abaixo temos a distribuição destas mesmas características, porém limitados à amostragem aplicável ao PHQ9 (pessoas de 18 a 59 anos).

![Idade e peso da população](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_idade_peso.png)

Por fim nos gráficos de barras abaixo temos a proporção do nível escolar e da renda per capita da população estudada:

![Nível escolar e renda per capita da população](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_escolaridade_renda.png)

Em relação à distribuição do valor PHQ9 (inteiro de 0 à 27) num comportamento similar ao uma exponencial negativa, conforme podemos observar na figura abaixo:

![PHQ9_dist](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_phq9_total_dist.png)

Nas figuras abaixo podemos comparar as distribuições do score PHQ-9 confrontadas com algumas variáveis de interesse.

![Correlacoes de interesse com depressao](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_analysis/01_pns_compare_dist_phq9_startos1.png)

![Correlacoes de interesse com depressao](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_analysis/01_pns_compare_dist_phq9_startos3.png)

Abaixo temos o gráfico da porcentagem de pessoas que já disseram diagnosticadas por depressão por estado brasileiro.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_brazil_depression.png)

Curiosamente, notou-se uma alta correlação entre o IDH médio de cada estado com a porcentagem de depressão.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_depression_idh_correlation.png)

O grupo suspeita que essa observação está relacionada ao fato de que o diagnóstico de depressão ou sua ausência está fortemente ligado à disponibilidade e facilidade de acesso aos serviços de saúde, o que tende a ser mais comum em regiões com um Índice de Desenvolvimento Humano (IDH) mais elevado. 

Avaliando o PHQ9 (indicativo acima de moderado) questionário aplicado durante à entrevista obtivemos o gráfico de correlação abaixo, reforçando a suspeita observada acima.

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_description/00_pns_phq9_idh_correlation.png)


# Análises Realizadas

> Descrição detalhada das análises realizadas.
>
>Relate aqui também a evolução do projeto: possíveis problemas enfrentados e possíveis mudanças de trajetória. Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.
>
> Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
>
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.
> 

_


_Análises estatísticas:_

Realizamos uma análise descritiva da amostra do estudo e averiguamos as correlações entre a variável dependente e as variáveis independentes. Em seguida, a fim de verificar a importância dos determinantes e a influência deles no diagnóstico de depressão construímos 3 modelos modificando as variáveis determinantes, sendo que no primeiro modelo selecionamos apenas as variáveis de comportamentos de saúde, no segundo modelo selecionamos apenas as variáveis de doenças crônicas não transmissíveis e no último modelo selecionamos tanto as variáveis de comportamentos de saúde, quanto às doenças crônicas não transmissíveis, todos os modelos foram ajustados pelas variáveis sociodemográficas. 











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



# Resultados



#### Testes de associação

Devido ao fato das nossas variáveis de interesse serem qualitativas, utilizamos o teste χ2 de Pearson para buscar associação.
Primeiramente, buscamos associações entre as variáveis que possam nos auxiliar na discussão dos achados, por exemplo, percepção de saúde e nível de escolaridade e percepção de saúde e raça-cor, e minimizar as variáveis de caracterização da amostra, como associação entre nível de escolaridade e renda per capita. 

| Variáveis confrontadas                                 |        χ2 |   p-value |
|:-------------------------------------------------------|----------:|----------:|
| Nível de escolaridade e renda per capita               |  23047.00 |         0 |
| Percepção de saúde e nível de escolaridade             |   6137.04 |         0 |
| Percepção de saúde segundo OMS e nível de escolaridade |   4083.09 |         0 |
| Percepção de saúde e raça-cor                          |   1020.99 |         0 |
| Percepção de saúde segundo OMS e raça-cor              |    695.94 |         0 |

Em seguida, realizamos associações entre variáveis de caracterização dos indivíduos com alto potencial de depressão baseado no score PHQ9. Obtivemos que sexo, cor, idade, escolaridade, percepção da própria saúde, percepção da saúde segundo OMS, renda per capita possui associação (p< 0,05) com alto potencial de depressão.

| Variáveis confrontadas com alto potencial de depressão (PHQ9 score > 20) |        χ2 |    p_value |
|:-------------------------------------------------------------------------|----------:|-----------:|
| Sexo                                                                     |    650.12 |          0 |
| Cor                                                                      |     27.46 |    0.00005 |
| Categoria idade                                                          |     23.64 |          0 |
| Escolaridade                                                             |      9.63 |    0.02198 |
| Percepção da própria saúde                                               |   3007.41 |          0 |
| Percepção da saúde segundo a OMS                                         |   4762.96 |          0 |
| Possui animal de estimação?                                              |      2.64 |   0.10445* |
| Renda per capita                                                         |    263.28 |          0 |
| Frequência bebida alcoólica                                              |      2.61 |   0.27098* |
| Fuma tabaco                                                              |    101.61 |          0 |
| Atividade física nos últimos 3 meses                                     |    105.78 |          0 |
| Teve diagnostico artrite ou reumatismo                                   |    183.69 |          0 |
| Teve diagnostico AVC                                                     |     50.22 |          0 |
| Teve diagnostico doenças cardiovasculares                                |    150.73 |          0 |
| Teve diagnostico hipercolesterolemia                                     |    130.91 |          0 |
| Teve diagnostico diabetes                                                |     13.57 |    0.00023 |
| Teve diagnostico pressão alta                                            |     35.73 |          0 |
| Teve diagnostico câncer                                                  |      5.25 |    0.02193 |
| Teve diagnostico depressão                                               |   4597.09 |          0 |

Em relação aos hábitos de vida, encontramos associação entre fumar tabaco e atividade física nos últimos 3 meses (p< 0,05), porém não encontramos associação entre consumo de bebida alcoólica e depressão (p=0,27). Neste bloco, pretendemos realizar análises sobre consumo alimentar, porém é necessário criar um índice a partir das informações presentes no inquérito, visto que são perguntas baseadas em um grupo de alimento ou alimento, por esse motivo, iremos buscar a associação de padrão alimentar saudável e não saudável com alto potencial de depressão para a próximo entrega. 
Por fim, analisamos as doenças crônicas não transmissíveis com depressão e verificamos que diagnóstico de artrite ou reumatismo, AVC, doenças cardiovasculares, hipercolesterolemia, diabetes, hipertensão e câncer estão associados com alto potencial de depressão. Como na análise de hábitos de vida, pretendemos incluir para próxima etapa a análise de associação de obesidade com alto potencial para depressão.
A partir dessas análises, pretendemos levar para o modelo final todas as variáveis de hábitos de vida e doenças crônicas não transmissíveis que possuem associação com o alto potencial de depressão.


#### Regressão


> Descrição dos resultados mais importantes obtidos.
>
> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de Análises Realizadas (o que for mais pertinente).

|                                    | Acc. Treino | Acc. Teste | P. Treino | P. Teste | R. Treino | R. Teste | F1 Treino | F1 Teste       | AUC Treino | AUC Teste      |
| ---------------------------------- | ----------- | ---------- | --------- | -------- | --------- | -------- | --------- | -------------- | ---------- | -------------- |
| Apenas hábitos                     | 55,95%      | 55,68%     | 12,95%    | 12,94%   | 54,70%    | 55,10%   | 20,94%    | 20,96% ± 0,65% | 55,40%     | 55,42% ± 0,97% |
| Apenas doenças crônicas            | 72,84%      | 71,83%     | 18,99%    | 18,62%   | 44,33%    | 45,37%   | 26,59%    | 26,36% ± 0,45% | 60,36%     | 60,26% ± 0,37% |
| Apenas hábitos e doenças crônicas  | 69,49%      | 69,74%     | 18,43%    | 18,57%   | 51,04%    | 51,00%   | 27,08%    | 27,22% ± 0,33% | 61,42%     | 61,54% ± 0,37% |
| Apenas variáveis sociodemográficos | 57,05%      | 56,56%     | 15,81%    | 15,70%   | 69,71%    | 70,06%   | 25,77%    | 25,65% ± 0,30% | 62,62%     | 62,50% ± 0,46% |
| Todas as varáveis 		               | 65,80%      | 65,90%     | 19,29%    | 19,28%   | 64,82%    | 64,46%   | 29,74%    | 29,68% ± 1,09% | 65,37%     | 65,27% ± 1,36% |



| Abordagens experimentadas    | F1 Treino  | F1 Teste               | AUC Treino | AUC Teste              |
| ---------------------------- | ---------- | ---------------------- | ---------- | ---------------------- |
| Removendo Linhas Nulas       | 29,74%     | 29,68% ± 1,09%         | 65,37%     | 65,27% ± 1,36%         |
| Substituindo NA pela média   | 28,68%     | 28,75% ± 0,75%         | 65,40%     | 65,45% ± 0,97%         |
| Substituindo NA pela mediana | 28,80%     | 28,85% ± 0,72%         | 65,53%     | 65,55% ± 0,93%         |
| SMOTE                        | 28,84%     | 28,64% ± 0,78%         | 64,95%     | 64,74% ± 1,10%         |
| Melhor resultado Grid Search | **29,68%** | **29,74%** ± **1,05%** | **65,31%** | **65,36%** ± **1,30%** |
| Árvore de Decisão            | 28,56%     | 28,26% ± 0,77%         | 64,48%     | 63,81% ± 1,06%         |
| Floresta Randomica           | 28,66%     | 28,39% ± 0,63%         | 65,17%     | 64,75% ± 0,81%         |




| Testes de estratificação | F1 Treino | F1 Teste       | AUC Treino | AUC Teste              | 
| ------------------------ | --------- | -------------- | ---------- | ---------------------- | 
| Renda Baixa              | 32,55%    | 32,45% ± 0,85% | 65,31%     | 65,15% ± 1,00%         |
| Renda Alta               | 24,36%    | 24,07% ± 0,71% | 63,69%     | 63,26% ± 1,01%         |
| Sexo Mulher              | 33,69%    | 33,25% ± 0,83% | 61,58%     | 61,16% ± 0,76%         |
| Sexo Homen               | 18,55%    | 18,25% ± 0,78% | 64,15%     | 63,67% ± 1,12%         |
| Idade < 40               | 25,45%    | 25,38% ± 0,77% | 63,30%     | 63,20% ± 1,10%         |
| Idade > 40               | 32,86%    | 32,77% ± 0,37% | 66,40%     | 66,29% ± 0,48%         |
| Idade 20-29              | 25,35%    | 24,93% ± 0,73% | 63,11%     | 62,54% ± 1,26%         |
| Idade 30-39              | 26,22%    | 26,19% ± 1,70% | 64,24%     | 64,34% ± 2,47%         |
| Idade 40-49              | 31,94%    | 31,62% ± 1,25% | 66,13%     | 65,71% ± 1,45%         |
| Idade 50-59              | 34,98%    | 34,57% ± 1,23% | 67,87%     | 67,40% ± 1,28%         |
| Região Norte             | 27,09%    | 26,86% ± 1,86% | 65,43%     | 65,07% ± 2,37%         |
| Região Nordeste          | 30,58%    | 30,27% ± 1,03% | 64,54%     | 64,26% ± 1,23%         |
| Região Sudeste           | 31,61%    | 31,02% ± 0,64% | 66,39%     | 65,71% ± 0,82%         |
| Região Sul               | 28,52%    | 28,00% ± 2,28% | 65,63%     | 64,89% ± 2,81%         |
| Região Centro Oeste      | 30,47%    | 29,33% ± 2,57% | 66,34%     | 64,83% ± 3,20%         |





| name                | log_apenas_habitos | log_apenas_dcnt | log_apenas_habitos_dcnt | log_apenas_sociodemo | Todas Váriaveis |
| ------------------- | ------------------ | --------------- | ----------------------- | -------------------- | --------------- |
| intercept           | 0,088              | \-0,360         | \-0,375                 | 0,501                | 0,295           |
| upf                 | 0,033              |                 | 0,051                   |                      | 0,049           |
| exerc_fisico        | \-0,311            |                 | \-0,269                 |                      | \-0,227         |
| tabagismo           | 0,427              |                 | 0,497                   |                      | 0,565           |
| cons_alcool         | \-0,257            |                 | \-0,169                 |                      | \-0,024         |
| cancer              |                    | 0,599           | 0,611                   |                      | 0,485           |
| hipertensao         |                    | 0,333           | 0,320                   |                      | 0,347           |
| diabetes            |                    | 0,443           | 0,428                   |                      | 0,487           |
| cardiovascular      |                    | 0,817           | 0,794                   |                      | 0,853           |
| hipercolesterolemia |                    | 0,416           | 0,448                   |                      | 0,463           |
| avc                 |                    | 0,827           | 0,748                   |                      | 0,679           |
| artrite             |                    | 0,971           | 0,967                   |                      | 0,876           |
| obesidade           |                    | 0,172           | 0,184                   |                      | 0,194           |
| sexo                |                    |                 |                         | \-1,053              | \-0,954         |
| estado_civil        |                    |                 |                         | \-0,394              | \-0,375         |
| escolaridade        |                    |                 |                         | \-0,043              | 0,028           |
| class_idade         |                    |                 |                         | 0,120                | \-0,058         |
| class_renda         |                    |                 |                         | \-0,262              | \-0,274         |


| Variáveis                  | Renda Baixa | Renda Alta | Diferença (abs) |
| -------------------------- | ----------- | ---------- | --------------- |
| **Intercepto**             | **\-0,054** | **0,540**  | **0,594**       |
| Ultraprocessados           | 0,047       | 0,050      | 0,003           |
| Exercício Físico           | \-0,150     | \-0,339    | 0,189           |
| Tabagismo                  | 0,597       | 0,534      | 0,063           |
| Consumo Álcool             | \-0,063     | 0,042      | 0,106           |
| Câncer                     | 0,581       | 0,481      | 0,100           |
| Hipertensão                | 0,321       | 0,385      | 0,065           |
| Diabetes                   | 0,497       | 0,507      | 0,010           |
| Cardiovascular             | 0,944       | 0,791      | 0,153           |
| Hipercolesterolemia        | 0,463       | 0,468      | 0,005           |
| **AVC**                    | **0,806**   | **0,592**  | **0,214**       |
| Artrite                    | 0,864       | 0,927      | 0,063           |
| Obesidade                  | 0,207       | 0,158      | 0,049           |
| Sexo (1=Masculino)         | \-1,003     | \-0,912    | 0,091           |
| Estado_Civil (1=Casado)    | \-0,410     | \-0,304    | 0,105           |
| Classificação Escolaridade | 0,069       | 0,005      | 0,063           |
| Classificação Idade        | 0,001       | \-0,154    | 0,155           |
| Classificação Renda        |             |            | 0,000           |




| Variáveis                   | Sexo Mulher | Sexo Homem  | Diferença (abs) |
| --------------------------- | ----------- | ----------- | --------------- |
| Intercepto                  | \-0,035     | \-0,098     | 0,063           |
| Ultraprocessados            | 0,037       | 0,068       | 0,031           |
| Exercício Físico            | \-0,223     | \-0,223     | 0,000           |
| Tabagismo                   | 0,570       | 0,606       | 0,036           |
| Consumo Álcool              | 0,083       | \-0,185     | 0,268           |
| Câncer                      | 0,577       | 0,308       | 0,269           |
| Hipertensão                 | 0,274       | 0,468       | 0,194           |
| Diabetes                    | 0,457       | 0,598       | 0,141           |
| Cardiovascular              | 0,806       | 0,964       | 0,157           |
| Hipercolesterolemia         | 0,428       | 0,534       | 0,105           |
| AVC                         | 0,630       | 0,854       | 0,224           |
| **Artrite**                 | **0,828**   | **1,191**   | **0,363**       |
| Obesidade                   | 0,164       | 0,265       | 0,101           |
| Sexo (1=Masculino)          |             |             | 0,000           |
| **Estado_Civil (1=Casado)** | **\-0,238** | **\-0,685** | **0,447**       |
| Classificação Escolaridade  | \-0,004     | 0,098       | 0,102           |
| Classificação Idade         | \-0,068     | \-0,012     | 0,056           |
| Classificação Renda         | \-0,314     | \-0,280     | 0,034           |



| Variáveis                  | Idade < 40 | Idade => 40 | Diferença (abs) |
| -------------------------- | ---------- | ----------- | --------------- |
| Intercepto                 | 0,179      | 0,130       | 0,049           |
| Ultraprocessados           | 0,058      | 0,048       | 0,010           |
| Exercício Físico           | \-0,074    | \-0,347     | 0,273           |
| Tabagismo                  | 0,671      | 0,484       | 0,187           |
| Consumo Álcool             | 0,114      | \-0,140     | 0,254           |
| Câncer                     | 0,428      | 0,535       | 0,106           |
| Hipertensão                | 0,578      | 0,239       | 0,339           |
| Diabetes                   | 0,261      | 0,523       | 0,263           |
| **Cardiovascular**         | **1,172**  | **0,774**   | **0,397**       |
| Hipercolesterolemia        | 0,524      | 0,424       | 0,100           |
| **AVC**                    | **1,123**  | **0,622**   | **0,502**       |
| Artrite                    | 1,029      | 0,851       | 0,179           |
| Obesidade                  | 0,250      | 0,141       | 0,108           |
| Sexo (1=Masculino)         | \-1,115    | \-0,870     | 0,245           |
| Estado_Civil (1=Casado)    | \-0,383    | \-0,375     | 0,009           |
| Classificação Escolaridade | \-0,011    | 0,067       | 0,078           |
| Classificação Idade        |            |             | 0,000           |
| Classificação Renda        | \-0,140    | \-0,397     | 0,256           |



| Variáveis                  | Idade 20-29 | Idade 30-39 | Idade 40-49 | Idade 50-59 |
| -------------------------- | ----------- | ----------- | ----------- | ----------- |
| Intercepto                 | 0,194       | 0,161       | 0,230       | 0,032       |
| Ultraprocessados           | 0,058       | 0,055       | 0,056       | 0,024       |
| Exercício Físico           | 0,038       | \-0,161     | \-0,223     | \-0,523     |
| Tabagismo                  | 0,663       | 0,674       | 0,480       | 0,517       |
| Consumo Álcool             | 0,136       | 0,097       | \-0,085     | \-0,238     |
| Câncer                     | 0,462       | 0,426       | 0,549       | 0,556       |
| Hipertensão                | 0,725       | 0,536       | 0,322       | 0,224       |
| Diabetes                   | 0,521       | 0,213       | 0,706       | 0,472       |
| Cardiovascular             | 1,577       | 0,989       | 0,684       | 0,845       |
| Hipercolesterolemia        | 0,477       | 0,562       | 0,391       | 0,489       |
| AVC                        | 1,021       | 1,146       | 0,652       | 0,609       |
| Artrite                    | 0,818       | 1,115       | 0,906       | 0,884       |
| Obesidade                  | 0,345       | 0,203       | 0,180       | 0,097       |
| Sexo (1=Masculino)         | \-1,195     | \-1,051     | \-0,944     | \-0,784     |
| Estado_Civil (1=Casado)    | \-0,301     | \-0,433     | \-0,555     | \-0,214     |
| Classificação Escolaridade | \-0,084     | 0,044       | 0,080       | 0,040       |
| Classificação Idade        |             |             |             |             |
| Classificação Renda        | 0,023       | \-0,249     | \-0,379     | \-0,354     |



| Variáveis                  | Região Norte | Região Nordeste | Região Sudeste | Região Sul | Região Centro Oeste |
| -------------------------- | ------------ | --------------- | -------------- | ---------- | ------------------- |
| Intercepto                 | \-0,080      | 0,277           | 0,232          | 0,422      | 0,999               |
| Ultraprocessados           | 0,081        | 0,061           | 0,028          | 0,054      | 0,011               |
| Exercício Físico           | \-0,030      | \-0,206         | \-0,301        | \-0,247    | \-0,434             |
| Tabagismo                  | 0,434        | 0,599           | 0,573          | 0,576      | 0,643               |
| Consumo Álcool             | 0,234        | \-0,137         | 0,006          | \-0,133    | \-0,023             |
| Câncer                     | 0,620        | 0,524           | 0,501          | 0,809      | \-0,002             |
| Hipertensão                | 0,368        | 0,399           | 0,213          | 0,442      | 0,324               |
| Diabetes                   | 0,656        | 0,431           | 0,420          | 0,509      | 0,515               |
| Cardiovascular             | 0,987        | 0,951           | 1,011          | 0,396      | 0,763               |
| Hipercolesterolemia        | 0,377        | 0,475           | 0,515          | 0,499      | 0,388               |
| AVC                        | 0,367        | 0,739           | 0,602          | 0,925      | 1,348               |
| Artrite                    | 0,925        | 0,979           | 0,996          | 0,561      | 0,894               |
| Obesidade                  | 0,354        | 0,046           | 0,418          | 0,129      | 0,031               |
| Sexo (1=Masculino)         | \-1,066      | \-0,878         | \-0,926        | \-0,871    | \-1,234             |
| Estado_Civil (1=Casado)    | \-0,407      | \-0,358         | \-0,430        | \-0,287    | \-0,363             |
| Classificação Escolaridade | 0,101        | 0,013           | 0,023          | 0,068      | \-0,055             |
| Classificação Idade        | \-0,027      | \-0,073         | \-0,018        | \-0,075    | \-0,156             |
| Classificação Renda        | \-0,418      | \-0,164         | \-0,257        | \-0,495    | \-0,179             |




![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/decistion_tree_p.svg)


### Resultados testes

| **exp**             | **accuracy_train** | **precision_train** | **recall_train** | **f1_train** | **auc_train** | **accuracy_test** | **precision_test** | **recall_test** | **f1_test** | **auc_test** |
| ------------------- | ------------------ | ------------------- | ---------------- | ------------ | ------------- | ----------------- | ------------------ | --------------- | ----------- | ------------ |
| Logistic Regression | 65,76%             | 19,26%              | 64,72%           | 29,68%       | 71,40%        | 65,33%            | 18,49%             | 66,27%          | 28,91%      | 71,57%       |
| Decision Tree       | 62,67%             | 18,16%              | 66,82%           | 28,56%       | 70,11%        | 61,99%            | 16,91%             | 65,76%          | 26,90%      | 69,33%       |
| Random Forest       | 60,28%             | 17,92%              | 71,46%           | 28,66%       | 71,21%        | 59,48%            | 16,90%             | 71,75%          | 27,36%      | 70,67%       |

![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/roc.png)


![](https://raw.githubusercontent.com/Arthur-Salles/DAGroup/e3/DAGroup/notebooks/generated_data/pns_data_models/cm.png)


# Discussão
> Discussão dos resultados. Relacionar os resultados com as perguntas de pesquisa ou hipóteses avaliadas.
>
> A discussão dos resultados também pode ser feita opcionalmente na seção de Resultados, na medida em que os resultados são apresentados. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?

# Conclusão
> Destacar as principais conclusões obtidas no desenvolvimento do projeto.
>
> Destacar os principais desafios enfrentados.
>
> Principais lições aprendidas.

# Trabalhos Futuros
> O que poderia ser melhorado se houvesse mais tempo?

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

1. Hunter DJ, Reddy KS. Noncommunicable Diseases. N Engl J Med [Internet]. 2013 [cited 2023 Apr 14];369(14):1336–43. Available from: https://www.who.int/health-topics/noncommunicable-diseases#tab=tab_1

2. World Health Organisation. Mental health in emergencies [Internet]. 2019 [cited 2023 Apr 14]. p. 1–70. Available from: https://www.who.int/news-room/fact-sheets/detail/mental-health-in-emergencies

3. Soares B, Kanevsky G, Teng CT, Pérez-Esparza R, Bonetto GG, Lacerda ALT, et al. Prevalence and Impact of Treatment-Resistant Depression in Latin America: a Prospective, Observational Study. Psychiatr Q [Internet]. 2021 Dec 1 [cited 2023 Apr 14];92(4):1797–815. Available from: /pmc/articles/PMC8531108/

4. Chisholm D, Sanderson K, Ayuso-Mateos JL, Saxena S. Reducing the global burden of depression: Population-level analysis of intervention cost-effectiveness in 14 world regions. Br J Psychiatry [Internet]. 2004 May [cited 2023 Apr 14];184(MAY):393–403. Available from: https://pubmed.ncbi.nlm.nih.gov/15123502/

5. Lotfaliany, M. _et al._ (2018) ‘Depression and chronic diseases: Co-occurrence and communality of risk factors’, _Journal of Affective Disorders_, 241, pp. 461–468. doi:10.1016/j.jad.2018.08.011. Available from: https://www.sciencedirect.com/science/article/pii/S016503271830805X?via%3Dihub

6. Stopa SR, Szwarcwald CL, Oliveira MM de, Gouvea E de CDP, Vieira MLFP, Freitas MPS de, et al. Pesquisa Nacional de Saúde 2019: histórico, métodos e perspectivas. Epidemiol e Serv saude Rev do Sist Unico Saude do Bras [Internet]. 2020 [cited 2023 Apr 14];29(5):e2020315. Available from: http://scielo.iec.gov.br/scielo.php?script=sci_arttext&pid=S1679-49742020000500035&lng=pt&nrm=iso&tlng=pt

7. 	dos Santos Costa C, Steele EM, de Faria FR, Monteiro CA. Score of ultra-processed food consumption and its association with sociodemographic factors in the Brazilian National Health Survey, 2019. Cad Saude Publica [Internet]. 2022 May 6 [cited 2023 Jun 21];38:e00119421. Available from: https://www.scielo.br/j/csp/a/QP4GrYT7cS6YCLrrTKtPvjp/?lang=en
   
8. 	Berti De Azevedo Barros M, De L, Medina PB, Lima G, Soares De Azevedo RC, Ferreira N, et al. Associação entre comportamentos de saúde e depressão: resultados da Pesquisa Nacional de Saúde de 2019. Rev Bras Epidemiol [Internet]. 2021 Dec 10 [cited 2023 Jun 21];24:e210010. Available from: https://doi.org/10.1590/1980-549720210010.supl.2
   	
9. 	de Sousa KT, Marques ES, Levy RB, Azeredo CM. Food consumption and depression among Brazilian adults: results from the Brazilian National Health Survey, 2013. Cad Saude Publica [Internet]. 2019 Dec 20 [cited 2023 Jun 21];36(1):e00245818. Available from: https://www.scielo.br/j/csp/a/75WMGWKGMvLZXR9CbJWd7sP/?lang=en
 
### Estudo Bibliográfico

[Barros MBA, Lima MG, Azevedo RCS, Medina LBP, Lopes CS, Menezes PR, Malta DC. Depression and health behaviors in Brazilian adults - PNS 2013. Rev Saude Publica. 2017 Jun 1;51(suppl 1):8s. doi: 10.1590/S1518-8787.2017051000084. PMID: 28591352; PMCID: PMC5676399.](https://pubmed.ncbi.nlm.nih.gov/28591352/)

[Godos J, Bonaccio M, Al-Qahtani WH, Marx W, Lane MM, Leggio GM, Grosso G. Ultra-Processed Food Consumption and Depressive Symptoms in a Mediterranean Cohort. Nutrients. 2023 Jan 18;15(3):504. doi: 10.3390/nu15030504. PMID: 36771211; PMCID: PMC9919031.](https://pubmed.ncbi.nlm.nih.gov/36771211/)

[Tian YR, Deng CY, Xie HC, Long QJ, Yao Y, Deng Y, Zhao H, Li Y, Liu H, Xiao L. Ultra-processed food intake and risk of depression: a systematic review. Nutr Hosp. 2023 Feb 15;40(1):160-176. English. doi: 10.20960/nh.03723. PMID: 36537321.](https://pubmed.ncbi.nlm.nih.gov/36537321/)

[Melo, A. P. S., Bonadiman, C. S. C., Andrade, F. M. de ., Pinheiro, P. C., & Malta, D. C.. (2023). Depression Screening in a population-based study: Brazilian National Health Survey 2019. Ciência & Saúde Coletiva, 28(4), 1163–1174. https://doi.org/10.1590/1413-81232023284.14912022](https://www.scielo.br/j/csc/a/wWKFtv8ZVZZTwVDM94Q3gFt/)

[Elizabeth L, Machado P, Zinöcker M, Baker P, Lawrence M. Ultra-Processed Foods and Health Outcomes: A Narrative Review. Nutrients. 2020 Jun 30;12(7):1955. doi: 10.3390/nu12071955. PMID: 32630022; PMCID: PMC7399967.](https://pubmed.ncbi.nlm.nih.gov/32630022/)

[Antunes JT, Dumont-Pena Érica, Silva AG da, Moutinho C dos S, Vieira MLFP, Malta DC. A saúde mental dos adolescentes brasileiros: Pesquisa Nacional de Saúde do Escolar de 2019. REME Rev Min Enferm.](https://periodicos.ufmg.br/index.php/reme/article/view/38984)

[Lane MM, Gamage E, Travica N, Dissanayaka T, Ashtree DN, Gauci S, Lotfaliany M, O'Neil A, Jacka FN, Marx W. Ultra-Processed Food Consumption and Mental Health: A Systematic Review and Meta-Analysis of Observational Studies. Nutrients. 2022 Jun 21;14(13):2568. doi: 10.3390/nu14132568. PMID: 35807749; PMCID: PMC9268228.](https://pubmed.ncbi.nlm.nih.gov/35807749/)

[Hecht EM, Rabil A, Martinez Steele E, Abrams GA, Ware D, Landy DC, Hennekens CH. Cross-sectional examination of ultra-processed food consumption and adverse mental health symptoms. Public Health Nutr. 2022 Nov;25(11):3225-3234. doi: 10.1017/S1368980022001586. Epub 2022 Jul 28. PMID: 35899785; PMCID: PMC9991859.](https://pubmed.ncbi.nlm.nih.gov/35899785/)
