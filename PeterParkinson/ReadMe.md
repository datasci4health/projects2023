# O impacto das atividades físicas na melhora da mobilidade e sintomas depressivos em pacientes com doença de Parkinson: um estudo de associação
# The impact of physical activities on the improvement of mobility and depressive symptoms in patients with Parkinson's disease: an association study
# Apresentação 
| Nome | RA| Especialização |
| :---         |     :---:      |          ---: |
| Giovani Luiz dos Reis    | 259156   | Análise e Desenvolvimento de Sistemas  |
| Julia de Melo Franco Fernandes |  248945   | Eng computação  |
| Lauana Andrade Messias| 183936  | Mestranda em Neurociências    |
| Maria Victoria  Soares Fiori  | 256905    | Mestranda Ciência da computação    |
| Suelen Aparecida Ribeiro de Souza   | 252483   |Mestranda em clinica medica  |
# Descrição Resumida do Projeto
O Parkinson é uma doença degenerativa complexa que afeta uma região importante do cérebro, resultando na degeneração dos neurônios. Os pacientes com DP sofrem com a perda gradativa na coordenação motora apresentando sintomas como: mudança no comportamento, lentidão nos movimentos, desequilíbrio e rigidez muscular devido a uma deficiência na neurotransmissão dopaminérgica localizada no putâmen posterior e no circuito motor cerebral (Rodriguez et al., 2009). Muitos pacientes percebem que os sintomas motores pioram durante períodos de estresse e podem apresentar sintomas de depressão e ansiedade (Crizzle et al., 2006). 

Atualmente, o diagnóstico é feito quando os sintomas estão evidentes, já em estágio avançado da doença, e não existem medicamentos capazes de curá-la (Myszczynska et al., 2020). À medida que a doença progride, os pacientes tendem a se tornar mais sedentários e diminuir suas atividades sociais, o que também piora a qualidade de vida relacionada à saúde. Estudos indicam que cerca de 50% dos pacientes desenvolvem depressão, o que contribui para o sedentarismo, independentemente do estágio da doença de Parkinson (Janet et al., 2017). Manifestações psiquiátricas como apatia, ansiedade e depressão são comuns na DP, e podem ser atribuídas a um déficit dopaminérgico no estriado ventral, além de uma redução na disponibilidade de serotonina e norepinefrina (Rodriguez et al., 2009).
Outros estudos apontam correlações ao comprometimento motor e global mais significativo em pacientes com depressão. Isso não significa que um paciente deprimido terá um prognóstico pior ou que a doença avançará mais rapidamente, mas provavelmente ele precisará de reposição de dopamina em estágios iniciais da doença (Prange et al., 2022).

Existe evidência de que a prática de atividade física intensa pode melhorar não apenas os sintomas motores, mas também os sintomas não motores, como o funcionamento cognitivo e o sono em pacientes com DP. Além disso, estudos preliminares indicam que a atividade física intensa pode ter efeitos modificadores na progressão da doença em pacientes com DP (de Vries NM et al,. 2021).

Diversas pesquisas mostram que a prática de atividade física melhora a qualidade de vida e aumenta a sobrevida dos pacientes. Isso ocorre porque o exercício físico aumenta os níveis de dopamina, reduz o estresse e alivia os sintomas da doença de Parkinson (Van der Heide et al., 2021). Além dos benefícios mencionados, o exercício físico também tende a diminuir a degradação dos neurônios dopaminérgicos e melhorar a função motora nos gânglios de base (Janet et al., 2017). 

Embora esses resultados ainda precisem ser confirmados por mais pesquisas, eles sugerem que a atividade física intensa pode ser uma estratégia promissora para melhorar a qualidade de vida de pacientes com DP (de Vries NM et al,. 2021).
O uso de bancos de dados é uma das ferramentas fundamentais na análise de dados biomédicos. Eles permitem o armazenamento de grandes volumes de dados gerados na pesquisa biomédica e sua análise mais eficiente. Fornecem uma forma organizada de armazenar e acessar dados brutos, permitindo que os pesquisadores analisem e interpretem esses dados de maneira eficaz e eficiente (Rajkomar, A et al,.2018). 

- Objetivo Geral: 
Demonstrar através da visualização de dados a correlação entre fazer exercício físico e a melhora dos sintomas do Parkinson, como por exemplo melhoria na mobilidade e depressão.
- [vídeo](https://youtu.be/67sz-QkUunE)
# Perguntas de Pesquisa
1. Qual é a melhor forma de exercício físico para ajudar a melhorar os sintomas de
Parkinson e reduzir a depressão (Atividades de baixa, média e alta intensidade)?
2. Existem riscos adicionais associados a exercícios físicos em pacientes com
Parkinson e depressão?
3. Qual é a duração mínima e frequência ideal para sessões de exercícios físicos para obter benefícios na melhora dos sintomas de Parkinson e redução da depressão ?

# Banco de dados
## Bases Estudadas mas Não Adotadas
| Base de Dados | Endereço na Web | Resumo descritivo |
| :---         |     :---:      |          ---: |
| Brain Diseases - BrainBase - CNCB-NGDC | https://ngdc.cncb.ac.cn/brainbase/diseases | Dados sobre o tema de Alzheimer, que descreve a doença, tipo e símbolo do gene e a fonte |
| CTD_MESHD003704_exposure_20230520230416 | https://ctdbase.org/detail.go?type=disease&acc=MESH%3AD003704&view=expStudies | Dados sobre o tema de Alzheimer/Demência, mostrando resumo, países, agentes de estresse para algumas doenças cerebrais|
| CTD_MESHD000544_exposure_20230520230729 | https://ctdbase.org/detail.go?type=disease&acc=MESH%3AD000544&view=expConsol | O dataset mostra dados de países, receptores da doença, tipos de estressor, sua relação com alguns eventos de exposição |


Como as bases encontradas eram muito pequenas ou não possuíam dados o suficiente para a análise de  Alzheimer/Demência, foi decidido a troca de tema para encontrar uma base mais estruturada com informação. 

Para as bases não adotadas foi necessário o filtro para a doença de Alzheimer, juntamente com o tratamento para valores nulos ou não respondidos.

A análise pode ser encontrada em data/external/bases não adotadas .

## Bases Estudadas e Adotadas
| Base de Dados | Endereço na Web | Resumo descritivo |
| :---         |     :---:      |          ---: |
| Michael J. Fox Foundation for Parkinson's Research | https://foxden.michaeljfox.org/insight/explore/fox.jsp | Base de dados retirada de um site com dados sobre a doença de Parkinson, que descreve os dados desde questões de saúde, emocional e médicas, até condições próprias que o paciente descreve |

- Michael J. Fox Foundation for Parkinson's Research

O site michaeljfox.org é o site oficial da Fundação Michael J. Fox, uma organização sem fins lucrativos dedicada a encontrar uma cura para a doença de Parkinson e a melhorar a vida das pessoas afetadas por ela. O site oferece informações e recursos valiosos sobre a doença de Parkinson, opções de tratamento, pesquisas em andamento e suporte emocional. Além disso, a fundação financia pesquisas em todo o mundo e oferece uma comunidade online chamada "Fox Insight", onde pessoas com Parkinson podem se conectar e compartilhar suas experiências para ajudar a avançar a pesquisa.

O banco de dados é em formato '.csv' e qualquer um com cadastro no site pode acessar a base. É um banco extremamente completo que compreende questões biológicas, médicas e pessoais, sendo necessário uma filtragem inicial para selecionar características e fatos específicos para a pesquisa. Foi selecionado variáveis sobre exercício físico e questões sobre saúde mental para responder as perguntas de pesquisa.

Inicialmente foi feita uma limpeza de valores incorretos sobre a idade dos participantes, retirando os valores, além de uma decisão inicial de utilizar somente um conjunto de dados de cada participando, excluindo dados de participantes que responderam mais de uma vez os questionários. Foi feito também uma categorização das idades, transformando-as em grupos de acordo com os quartis da base.

A análise pode ser vista em data/external/bases adotadas 
# Metodologia  
Para a seleção cuidadosa de artigos relacionados à doença de Parkinson, depressão e atividade física no total 10, será utilizado um banco de dados renomado e acessível, como o MichaelJ.Fox. Os dados obtidos serão cruzados por meio de um fluxograma preciso e organizados em clusters, permitindo extrair insights relevantes e aprofundar o conhecimento sobre essa doença complexa. A visualização e análise dessas informações serão facilitadas pela construção de fluxogramas interligados a clusters, utilizando ferramentas de dados como o Orange. Esse processo permitirá a identificação de padrões e tendências importantes, fornecendo subsídios para a criação de novas abordagens terapêuticas e para a melhoria da qualidade de vida dos pacientes com Parkinson. Com essa metodologia rigorosa, espera-se que os resultados sejam confiáveis e úteis para a comunidade médica e científica no desenvolvimento de tratamentos mais eficazes para a doença de Parkinson.
## Banco de dados e Bases de Dados e Evolução
### Bases Estudadas mas Não Adotadas
| Base de Dados | Endereço na Web | Resumo descritivo |
| :---         |     :---:      |          ---: |
| Brain Diseases - BrainBase - CNCB-NGDC | https://ngdc.cncb.ac.cn/brainbase/diseases | Dados sobre o tema de Alzheimer, que descreve a doença, tipo e símbolo do gene e a fonte |
| CTD_MESHD003704_exposure_20230520230416 | https://ctdbase.org/detail.go?type=disease&acc=MESH%3AD003704&view=expStudies | Dados sobre o tema de Alzheimer/Demência, mostrando resumo, países, agentes de estresse para algumas doenças cerebrais|
| CTD_MESHD000544_exposure_20230520230729 | https://ctdbase.org/detail.go?type=disease&acc=MESH%3AD000544&view=expConsol | O dataset mostra dados de países, receptores da doença, tipos de estressor, sua relação com alguns eventos de exposição |


Como as bases encontradas eram muito pequenas ou não possuíam dados o suficiente para a análise de  Alzheimer/Demência, foi decidido a troca de tema para encontrar uma base mais estruturada com informação. 

Para as bases não adotadas foi necessário o filtro para a doença de Alzheimer, juntamente com o tratamento para valores nulos ou não respondidos.

A análise pode ser encontrada em data/external/bases não adotadas .

### Bases Estudadas e Adotadas
| Base de Dados | Endereço na Web | Resumo descritivo |
| :---         |     :---:      |          ---: |
| Michael J. Fox Foundation for Parkinson's Research | https://foxden.michaeljfox.org/insight/explore/fox.jsp | Base de dados retirada de um site com dados sobre a doença de Parkinson, que descreve os dados desde questões de saúde, emocional e médicas, até condições próprias que o paciente descreve |

- Michael J. Fox Foundation for Parkinson's Research

O site michaeljfox.org é o site oficial da Fundação Michael J. Fox, uma organização sem fins lucrativos dedicada a encontrar uma cura para a doença de Parkinson e a melhorar a vida das pessoas afetadas por ela. O site oferece informações e recursos valiosos sobre a doença de Parkinson, opções de tratamento, pesquisas em andamento e suporte emocional. Além disso, a fundação financia pesquisas em todo o mundo e oferece uma comunidade online chamada "Fox Insight", onde pessoas com Parkinson podem se conectar e compartilhar suas experiências para ajudar a avançar a pesquisa.

O banco de dados é em formato '.csv' e qualquer um com cadastro no site pode acessar a base. É um banco extremamente completo que compreende questões biológicas, médicas e pessoais, sendo necessário uma filtragem inicial para selecionar características e fatos específicos para a pesquisa. Foi selecionado variáveis sobre exercício físico e questões sobre saúde mental para responder as perguntas de pesquisa.

Inicialmente foi feita uma limpeza de valores incorretos sobre a idade dos participantes, retirando os valores, além de uma decisão inicial de utilizar somente um conjunto de dados de cada participando, excluindo dados de participantes que responderam mais de uma vez os questionários. Foi feito também uma categorização das idades, transformando-as em grupos de acordo com os quartis da base.

A análise pode ser vista em data/external/bases adotadas 
### Integração entre Bases e Análise Exploratória

No Gráfico 1  é representado o nível de ansiedade vs a mobilidade. A mobilidade na base de dados é descrita e classificada como: 

Mobility	0	I have no problems in walking about
Mobility	1	I have slight problems in walking about
Mobility	2	I have moderate problems in walking about
Mobility	3	I have severe problems in walking about
Mobility	4	I am unable to walk about
Mobility	5	Prefer not to answer
Foi possível observar que quanto menor a mobilidade do paciente maior o nível de ansiedade. 

No Gráfico 2  é representado o nível de ansiedade vs autocuidado. A autocuidado na base de dados é descrita e classificada como:

Care	0	I have no problems washing or dressing myself
Care	1	I have slight problems washing or dressing myself
Care	4	I am unable to wash or dress myself
Care	2	I have moderate problems washing or dressing myself
Care	3	I have severe problems washing or dressing myself
Care	5	Prefer not to answer

Diante disso, é visto que há uma relação similar entre a mobilidade e o autocuidado, pois se o paciente consegue realizar atividades de forma independente o nível de ansiedade demonstrado pelo gráfico é menor.
Pain	1	I have slight pain or discomfort
Pain	2	I have moderate pai or discomfort
Pain	3	I have severe pain or discomfort
Pain	0	I have no pain or discomfort
Pain	4	I have extreme pain or discomfort
Pain	5	Prefer not to answer
No Gráfico 3  é representado o nível de ansiedade vs atividade. A atividade na base de dados é descrita e classificada como:

Active	0	I have no problems doing my usual activities
Active	1	I have slight problems doing my usual activities
Active	2	I have moderate problems doing my usual activities
Active	4	I am unable to do my usual activities
Active	3	I have severe problems doing my usual activities
Active	5	Prefer not to answer
No Gráfico 4 é representado o nível de ansiedade vs dor. A dor na base de dados é descrita e classificada como:

!(./assets/exp/pain-semXcom.jpg)

Pain	1	I have slight pain or discomfort
Pain	2	I have moderate pai or discomfort
Pain	3	I have severe pain or discomfort
Pain	0	I have no pain or discomfort
Pain	4	I have extreme pain or discomfort
Pain	5	Prefer not to answer


Foi possível observar que quanto menor a ansiedade do paciente menor o nível de dor. 
 Diante disso, é visto que há uma relação entre a mobilidade, autocuidado e realização de atividade, pois se o paciente consegue realizar atividades de forma independente o nível de ansiedade demonstrado pelo gráfico é menor. Sendo assim, conclui-se que ansiedade pode ser apresentada em pacientes de parkinson com a maior perda de mobilidade e mudanças severas na rotina. 
No gráfico, 5, há a distribuição dos grupos de pessoas em idades por ranges, onde:
Range 0: pessoas entre 18 e 30 anos
Range 1: pessoas entre 31 e 57 anos
Range 2: pessoas entre 58 e 66 anos
Range 3: pessoas entre 67 e 72 anos
Range 4: pessoas acima de 72 anos
 A partir da análise do gráfico, é possível concluir que o range 1, com pessoas entre 31 e 57 anos, representa o grupo de idade mais afetado pela doença, com mais de 12.000 pacientes. Os ranges 2, 3 e 4, apresentam praticamente os mesmos números de pessoas, com aproximadamente 10.000 em cada um. Já o range 0, com pessoas entre 18 e 30 anos apresenta o menor índice, com menos de 1.000 pessoas.
Usuários que possuem problema em atividade X depressão
No gráfico, 6, há a distribuição dos grupos de pessoas por ranges, onde contagem das pessoas vs problemas de atividades físicas:

0	I have no problems doing my usual activities    
1	I have slight problems doing my usual activities
2	I have moderate problems doing my usual activities
4	I am unable to do my usual activities
3	I have severe problems doing my usual activities
5	Prefer not to answer
6	na 
Range de atividades 0: Qtda de pessoas 16.000
Range de atividades 1: Qtda de pessoas 12.000
Range de atividades 2: Qtda de pessoas 6.000
Range de atividades 3: Qtda de pessoas 0
Range de atividades 4: Qtda de pessoas 500
Range de atividades 5: Qtda de pessoas 1000
Range de atividades 6: Qtda de pessoas 9000
Podemos observar que o grupo de range 1: com quantidade de 12.000 pessoas tem pequenos problemas em fazer atividades habituais comparado ao grupo 0 na qual não possui nenhuma atividade. E em relação ao grupo de range de atividades 2: onde possui 6.000 pessoas tem moderados problemas ao realizarem atividades habituais. Enquanto os demais grupos de ranges de atividades 3 possuem severos problemas em realizar atividades habituais e o 6 apresentaram 9.000 pessoas que não responderam.

O gráfico 7 representa a contagem de pessoas com problemas de depressão, classificadas em ranges:
Range 0: não possui depressão
Range 1: possui depressão 
Range 3: preferiram não responder
Range 4: dados não foram disponibilizados
 Diante da análise desse gráfico, foi possível concluir que não houve diferença significativa entre os grupos 0 e 1, representando algo em torno de 1.000 pessoas. A quantidade de pessoas no range 3 ou não é significativa a ponto de aparecer no gráfico, ou não existem pessoas nesse grupo. Já o range 4, incluiu mais de 40.000 pessoas que não tiveram essa informação disponibilizada.


imagens dos  ultilizadas gráficos na análise estão no arquivo data/external/bases adotadas/analisys.ipynb 

 video da analise feita pelo orange: https://youtu.be/5N9QGw55-Qo
Utilizando questionários respondidos por pessoas entre 51 e 86 anos, constatamos que uma grande quantidade de participantes apresentava problemas de mobilidade associados ao Parkinson. Mais da metade relatou dificuldades de locomoção devido à condição. Além disso, uma proporção significativa dessas pessoas manifestava sintomas de ansiedade e depressão. Esses resultados ressaltam a correlação entre os problemas de mobilidade decorrentes do Parkinson e os sintomas de ansiedade e depressão, destacando a importância de abordar não apenas os aspectos motores, mas também os emocionais e psicológicos da doença

# Ferramentas 
Ferramenta de dados de linguagem  Python e Orange para design dos gráficos 
# Cronograma
| ETAPA   | SEMANAS |
| ------------- | ------------- |
| Coleta de dados  | 2 semanas  |
| Pré-processamento de dados | 2 semanas |
| Análise integrativa de dados | 3 semanas |
|Análise funcional de genes | 2 semanas |

## Fluxograma das análises

![Figura 1](./assets/fluxograma-analise.png)

# Organizaçaõ do git

```
├── README.md                     <- apresentação do projeto
│
├── data
│   ├── external                
│       ├── bases adotadas       <- base de terceira utilizada para o trabalho
│       ├── baeses não adotadas  <- base de terceiros estudadas, porém não utilizadas
│   ├── interim                  <- dados intermediários, e.g., resultado de transformação
│   ├── processed                <- dados finais usados para a modelagem
│
├── notebooks                    <- jupyter notebooks ou equivalentes
│
├── models                       <- modelos simples salvos
│
├── src                <- fonte em linguagem de programação ou sistema (e.g., Orange)
│   └── README.md      <- instruções básicas de instalação/execução
│
└── assets             <- mídias usadas no projeto
```