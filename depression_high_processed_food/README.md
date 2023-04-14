# Projeto `Depressão e ultraprocessados no Brasil, uma abordagem guiada por dados`
# Project `Depression and ultra-processed foods in Brazil: a data-driven approach`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp.

|Nome  | RA | Especialização|
|--|--|--|
| Beatriz Silva Nunes  | 167428  | Saúde - [Conta GitHub](https://github.com/beatrizsnunes)|
| Arthur Rezende Salles   | 166003  | Computação - Líder Github - Conta <incluir login conta github>|
| Anderson Nogueira Cotrim  | 163993  | Computação - [Conta GitHub](https://github.com/AndersonCotrim)|
| Guilherme Magalhães Soares  | 217241  | Elétrica - [Conta GitHub](https://github.com/gsoso01)|


# Descrição Resumida do Projeto
> Descrição do tema do projeto, incluindo motivação e contexto gerador.
> 

Este projeto visa estudar os fatores de risco relacionados aos hábitos de vida, alimentação e saúde mental que contribuem para a prevalência de doenças não crônicas no Brasil. A ideia é analisar dados de diferentes fontes, como pesquisas nacionais de saúde e dados de hospitais, para identificar os principais fatores de risco e padrões de doenças em diferentes regiões do país.

Doenças relacionadas aos hábitos de vida, alimentação e saúde mental são um grande problema de saúde pública no Brasil e em todo o mundo. Estas doenças incluem, por exemplo, doenças cardiovasculares, diabetes, obesidade, depressão e ansiedade. Essas doenças podem ter causas multifatoriais, incluindo estilo de vida, dieta, fatores ambientais e genéticos.

Compreender os fatores de risco relacionados a essas doenças é fundamental para desenvolver estratégias eficazes de prevenção e tratamento. Por exemplo, estudos mostram que a adoção de um estilo de vida saudável, incluindo uma dieta balanceada, atividade física regular e a prática de técnicas de relaxamento e gestão do estresse, pode reduzir o risco de desenvolver doenças crônicas.

Em resumo, este projeto visa identificar os principais fatores de risco relacionados aos hábitos de vida, alimentação e saúde mental que contribuem para a prevalência de doenças não crônicas no Brasil, com base na análise de dados de diferentes fontes. Espera-se que os resultados obtidos possam informar políticas de saúde pública e melhorar a qualidade de vida da população.


[Link para vídeo de apresentação da proposta do projeto](https://dummy.com.br)

# Perguntas de Pesquisa
> Perguntas de pesquisa que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.


Algumas perguntas de pesquisa foram pensadas visando uma compreensão aprofundada da prevalência e fatores de risco associados à depressão no Brasil.

 - Quais hábitos de vida estão associados à depressão? 
 - É possível quantificar o grau de impacto de cada hábito, considerando tanto as influências positivas quanto negativas? 
 - A influência desses fatores varia ao longo do curso da vida?
 - Será que o consumo de ultraprocessados está associado ao desenvolvimento da depressão?
 - Será que as pessoas que possuem depressão também possuem outras doenças crônicas que estão associadas com alto consumo de ultraprocessados como obesidade?

# Bases de Dados
> Elencar bases de dados candidatas a serem utilizadas no projeto.

Base de Dados  | Descrição | Anos
----- | ----- |  -----
[Pesquisa Nacional de Saúde (PNS)](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html?=&t=downloads) | Realizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) em parceria com o Ministério da Saúde, tem como objetivo coletar informações sobre o desempenho do sistema nacional de saúde em relação ao acesso e uso dos serviços disponíveis, bem como garantir a continuidade dos cuidados necessários. Além disso, a pesquisa visa avaliar as condições de saúde da população, monitorar doenças crônicas não transmissíveis e identificar os principais fatores de risco associados a elas. |  2019 (último)
[Sistema de Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico (Vigitel)](https://svs.aids.gov.br/download/Vigitel/) | O Vigitel é parte integrante do sistema de Vigilância de Fatores de Risco para doenças crônicas não transmissíveis (DCNT) do Ministério da Saúde, juntamente com outros inquéritos, como os domiciliares e os direcionados à população escolar. Conhecer a situação de saúde da população é o primeiro passo para planejar ações e programas que possam reduzir a ocorrência e a gravidade dessas doenças, melhorando assim a saúde da população. A pesquisa Vigitel é realizada anualmente pela Secretaria de Vigilância em Saúde (SVS) do Ministério da Saúde e as entrevistas telefônicas são conduzidas com amostras da população adulta (18 anos ou mais) residente em domicílios com linha de telefone fixo. A partir de 2022, as entrevistas também passaram a ser realizadas em telefones celulares. | 2006-2021
[Pesquisa Nacional de Saúde do Escolar (PeNSE)](https://www.ibge.gov.br/en/statistics/social/population/16837-national-survey-of-school-health-editions.html?=&t=downloads) | O Instituto Brasileiro de Geografia e Estatística - IBGE - realiza a Pesquisa Nacional de Saúde do Escolar (PeNSE), em diversas cidades do Brasil, em parceria com o Ministério da Saúde e com o apoio do Ministério da Educação. Os objetivos da pesquisa são: conhecer e medir fatores de risco e de proteção relacionados à saúde dos adolescentes; apoiar o monitoramento da saúde dos estudantes brasileiros; oferecer orientação às iniciativas de saúde voltadas para esse grupo populacional, fornecendo informações confiáveis sobre o assunto. | 2019 (último)


# Metodologia
> Esta seção será evoluída ao longo do projeto. Nesta primeira entrega informe técnicas que pretende-se explorar
> tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas. Para a primeira entrega, descreva de maneira mais genérica que tipo de abordagem seu grupo pretende realizar.

Este trabalho de forma geral procura avaliar e descobrir os fatores de risco para a depressão no Brasil. Para este fim, abordaremos uma metodologia baseada quatro estratégias principais:

- Realização de um estudo bibliográfico, que permitirá entender os padrões esperados para cada pergunta de pesquisa.
- Análise exploratória, incluindo seleção e pré-processamento dos dados. Mostrar o que os dados de forma macro contam diretamente. Exemplos: como é a distribuição da depressão pelas regiões do Brasil? Há correlação com IDH regional? Como essa doença se evoluiu ao longo dos anos no Brasil e em cada Estado? 
- Realização de uma análise estatística, utilizando técnicas de estatística descritiva e visualização, como gráficos de dispersão, caixa, e barras, a fim de extrair conhecimento dos dados.
- Aplicação de técnicas de aprendizado de máquina (regressão), que nos permita uma análise aprofundada e a quantificação da relevância de cada característica para variável de interesse (depressão). 


# Estudo bibliográfico

[Godos J, Bonaccio M, Al-Qahtani WH, Marx W, Lane MM, Leggio GM, Grosso G. Ultra-Processed Food Consumption and Depressive Symptoms in a Mediterranean Cohort. Nutrients. 2023 Jan 18;15(3):504. doi: 10.3390/nu15030504. PMID: 36771211; PMCID: PMC9919031.](https://pubmed.ncbi.nlm.nih.gov/36771211/)

[Tian YR, Deng CY, Xie HC, Long QJ, Yao Y, Deng Y, Zhao H, Li Y, Liu H, Xiao L. Ultra-processed food intake and risk of depression: a systematic review. Nutr Hosp. 2023 Feb 15;40(1):160-176. English. doi: 10.20960/nh.03723. PMID: 36537321.](https://pubmed.ncbi.nlm.nih.gov/36537321/)

[Elizabeth L, Machado P, Zinöcker M, Baker P, Lawrence M. Ultra-Processed Foods and Health Outcomes: A Narrative Review. Nutrients. 2020 Jun 30;12(7):1955. doi: 10.3390/nu12071955. PMID: 32630022; PMCID: PMC7399967.](https://pubmed.ncbi.nlm.nih.gov/32630022/)

[Lane MM, Gamage E, Travica N, Dissanayaka T, Ashtree DN, Gauci S, Lotfaliany M, O'Neil A, Jacka FN, Marx W. Ultra-Processed Food Consumption and Mental Health: A Systematic Review and Meta-Analysis of Observational Studies. Nutrients. 2022 Jun 21;14(13):2568. doi: 10.3390/nu14132568. PMID: 35807749; PMCID: PMC9268228.](https://pubmed.ncbi.nlm.nih.gov/35807749/)

[Hecht EM, Rabil A, Martinez Steele E, Abrams GA, Ware D, Landy DC, Hennekens CH. Cross-sectional examination of ultra-processed food consumption and adverse mental health symptoms. Public Health Nutr. 2022 Nov;25(11):3225-3234. doi: 10.1017/S1368980022001586. Epub 2022 Jul 28. PMID: 35899785; PMCID: PMC9991859.](https://pubmed.ncbi.nlm.nih.gov/35899785/)


# Ferramentas
> Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

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


# Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.

Semanas | Tarefas
----- | -----
Semana 01 (16/04 - 22/04) | Definir escopo do projeto e revisão bibliográfica
Semana 02 (23/04 - 29/04) | Compreensão do dados
Semana 03 (30/04 - 06/05) | Processamento dos dados 
Semana 04 (07/05 - 13/05) | Análise exploratória e Entrega 2
Semana 05 (14/05 - 20/05) | Modelagem da solução
Semana 06 (21/05 - 27/05) | Modelagem da solução
Semana 07 (28/05 - 03/06) | Modelagem da solução
Semana 08 (04/06 - 10/06) | Análise e discussão dos resultados
Semana 09 (11/06 - 17/06) | Relatório
Semana 10 (18/06 - 24/06) | Apresentação e Entrega Final
