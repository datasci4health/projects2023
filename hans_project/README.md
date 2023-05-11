# Projeto `Análise de dados da hanseníase: uma abordagem preditiva para a saúde pública`

# Project `Data analysis of leprosy: a predictive approach for public health`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp, pelos membros:

> |Nome  | RA | Especialização|
> |--|--|--|
> | Alexsandro Ferreira de Barros Júnior  | 233768  | Computação - Líder Github - [Conta GitHub](https://github.com/alexbjr) |
> | Giovanna Gennari Jungklaus  | 198010  | Computação - [Conta GitHub](https://github.com/gigennari)|
> | José Ernesto Stelzer Monar  | 139553  | Computação - [Conta GitHub](https://github.com/stelzer-monar-ifood)|
> | Maria Clara Castro Higino de Sousa  | 243237  | Computação - [Conta GitHub](https://github.com/mc-castro)|
> | Miriam Reyes Ortiz  | 265762  | Saúde - [Conta GitHub](https://github.com/MiriamOrtiz)|


# Descrição Resumida do Projeto
> A hanseníase é uma doença infecciosa crônica que afeta principalmente a pele e os nervos periféricos. Apesar dos avanços no tratamento, a hanseníase ainda é um problema de saúde pública em muitos países, incluindo o Brasil. O tratamento da hanseníase é longo e requer o uso de múltiplos medicamentos, o que pode levar a custos elevados para os sistemas de saúde. Além disso, a duração do tratamento pode variar de acordo com cada paciente, o que torna o planejamento financeiro ainda mais desafiador.
>
> Nesse contexto, este projeto tem como objetivo analisar uma grande base de dados sobre casos de hanseníase com o objetivo de estimar o tempo de cura dos pacientes. Para isso, serão utilizadas técnicas de machine learning para identificar as variáveis mais relevantes para o resultado, bem como a relação entre elas e o tempo de cura.
>
> Espera-se que os resultados deste projeto possam ajudar na otimização do tratamento da hanseníase, permitindo a alocação de recursos adequados para cada paciente e melhorando o planejamento financeiro dos sistemas de saúde. Além disso, a análise desses dados pode fornecer percepções importantes sobre a doença e ajudar na prevenção e controle da hanseníase em nível nacional.
> 
> [Vídeo de apresentação](https://drive.google.com/file/d/1LdYcPP0i0cjiHvt-HNTh64a2jiKPNRNR/view?usp=sharing)

# Perguntas de Pesquisa
> Quais variáveis clínicas e epidemiológicas estão associadas ao tempo de cura dos pacientes com hanseníase?
>
> Como as percepções obtidas a partir da análise de dados podem ser utilizadas para melhorar o planejamento financeiro dos sistemas de saúde em relação ao tratamento da hanseníase?
>
> Existe uma correlação entre o índice geográfico e o índice de desenvolvimento social das regiões afetadas pela hanseníase e a incidência e gravidade da doença?
>
> Qual é o desempenho dos modelos de machine learning na previsão do tempo de cura dos pacientes com hanseníase?

# Bases de Dados
> |Fonte | Descrição|
> |--|--|
> |[Sistema de Informação de Agravos de Notificação (SINAN)](http://portalsinan.saude.gov.br/hanseniase) |
> |[Indicadores Epidemiológicos](http://indicadoreshanseniase.aids.gov.br/) |Base mantida pelo Departamento de Doenças de Condições Crônicas e Infecções Sexualmente Transmissíveis - DCCI, do Ministério da Saúde. É uma centralização de todos os casos de hanseníase ocorridos no Brasil assim como diversas informações associadas a cada caso por paciente.| 

# Metodologia
> Será realizada uma análise exploratória de dados para identificar e selecionar características que mostrem correlação com os desfechos da doença. A partir desses dados, será utilizado um modelo de aprendizado de máquina que realize previsões quanto ao tempo de cura dos pacientes analisados. Para concluir o estudo, análises estatísticas serão realizadas para testar as hipóteses formuladas. 

# Ferramentas
> O projeto será realizado em Python e serão utilizadas a seguintes ferramentas e bibliotecas:
>
> |Ferramenta/Biblioteca | Descrição|
> |--|--|
> |[Pandas](https://pandas.pydata.org/) |Biblioteca para manipulação e análise de dados| 
> |[Numpy](https://numpy.org/) |Biblioteca para cálculos matemáticos e estatísticos| 
> |[Scikit-learn](https://scikit-learn.org/stable/) |Biblioteca para modelagem preditiva e aprendizado de máquina| 
> |[Matplotlib](https://matplotlib.org/) e [Seaborn](https://seaborn.pydata.org/) |Bibliotecas para visualização de dados| 
> |[Jupyter Notebook](https://jupyter.org/) |Ferramenta para desenvolvimento e apresentação de notebooks interativoss| 

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
