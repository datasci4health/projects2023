
# Projeto `Avaliação da Correlação entre os Parâmetros Renais CK e CPK e a Administração Intravenosa de Insulina em Pacientes com Obesidade`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação Ciência e Visualização de Dados em Saúde, oferecida no primeiro semestre de 2023, na Unicamp.

|Nome  | RA | Especialização|
|--|--|--|
| Fernando Fortes Granado | 171517 | Computação |
| Glinka Lino Duarte Estadulho  | 271104  | Física|
| João Augusto Rosa Feltran  | 174083 | Computação |
| Michel Frank Ferrazo  | 224972  | Farmacologia |
| Thársis Salathiel | 226066 | Computação - Líder Github - Conta salathiel10|

# Descrição Resumida do Projeto

A obesidade é uma condição de saúde crescente em todo o mundo, afetando milhões de pessoas e apresentando diversos riscos à saúde, incluindo o desenvolvimento de diabetes tipo 2. A administração adequada de insulina é fundamental para o controle glicêmico em pacientes obesos com diabetes. No entanto, a dosagem correta de insulina e o método de administração ainda são desafios significativos na prática clínica.

Nesse contexto, uma área de pesquisa promissora é a investigação da relação entre os parâmetros renais CK (creatina quinase) e CPK (creatina fosfoquinase) e a escolha da administração intravenosa de insulina em pacientes com obesidade. Estudos anteriores sugerem que níveis elevados desses marcadores renais podem estar associados a complicações metabólicas e renais em pacientes obesos com diabetes.

O objetivo deste projeto é analisar se há uma correlação entre os exames laboratoriais de CK e CPK e a decisão de administrar insulina intravenosa em pacientes obesos. Além disso, buscamos determinar o tamanho da oportunidade de aumento na administração intravenosa de insulina em pacientes obesos, com base nos resultados obtidos.

Para alcançar esses objetivos, será conduzido um estudo retrospectivo envolvendo uma amostra representativa de pacientes obesos com diabetes, cujos dados laboratoriais de CK, CPK e a forma de administração de insulina estão disponíveis nos registros médicos. As informações serão analisadas estatisticamente, utilizando métodos apropriados, para identificar possíveis correlações entre os parâmetros renais e a administração intravenosa de insulina.

Espera-se que os resultados desse estudo possam fornecer insights valiosos para os profissionais de saúde envolvidos no tratamento de pacientes obesos com diabetes. Além disso, a análise da oportunidade de aumento na administração intravenosa de insulina poderá ajudar a melhorar as estratégias terapêuticas e promover uma abordagem mais individualizada no tratamento desses pacientes, com potenciais benefícios na gestão do diabetes e na prevenção de complicações metabólicas e renais.

Link para video:
https://drive.google.com/file/d/1ZVwDOocFzThgN53GMuOPy3mcSKYTh6Pq/view?usp=sharing


# Perguntas de Pesquisa

1. Existe uma correlação entre os exames laboratoriais de CK e CPK (parâmetros renais) e a escolha de administração de insulina intravenosa em pacientes com obesidade? 

2. Qual é o tamanho da oportunidade de aumento na administração intravenosa de insulina em pacientes obesos?

# Metodologia

1. Processar dados do MIMIC-IV
2. Observar parâmetros relativos ao CK e CPK e a administração intravenosa de insulina
3. Usar analise estatísticas descritivas para gerar conclusões

# Bases de Dados e Evolução

### Bases Estudadas mas Não Adotadas

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Pub med (e outras bases de artigos) | https://pubmed.ncbi.nlm.nih.gov/ | Base de artigos sobre literatura biomedica.

Inicialmente o grupo tinha considerado se utilizar de dados provenientes de artigos da literatura. Entretanto, notou-se certa dificuldade em minerar esses dados a parti dos arquivos PDFs dos artigos. Assim, optou-se por abandonar esse tipo de abordagem.

### Bases Estudadas e Adotadas

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
MIMIC-IV<sup>1</sup> | https://physionet.org/content/mimiciv/2.2/ | O banco de dados Medical Information Mart for Intensive Care (MIMIC) fornece dados de cuidados intensivos para mais de 40.000 pacientes internados em unidades de terapia intensiva no Beth Israel Deaconess Medical Center (BIDMC).

<sup>1</sup>Johnson, Alistair, et al. "MIMIC-IV" (version 2.2). PhysioNet (2023), https://doi.org/10.13026/6mm1-ek67.

Esse banco de dados é formado por diversas tabelas no formato CSV (comma-separated values), cada tabela aborda uma "entidade" do hospital. Assim, há uma tabela para informações dos pacientes, uma para medicamentos aplicados, uma para exames realizados, etc. Cada tabela tem seu próprio conjunto de colunas, mas a coluna relacionada ao ID do paciente aparece em praticamente todas as tabelas.

Analisando os dados foi possível constar que essa base possui abundância de informações. Algumas tabelas chegam ao tamanho de 30GB. Por vezes foi necessário processar as tabelas em partes para não haver um estouro de memória.

Houve um pre-processamento inicial da base para separar apenas os dados de interesse do projeto. Mais informações sobre esse pre-processamento podem ser encontradas no notebook [process_raw_mimic.ipynb](notebooks/process_raw_mimic.ipynb). Após esse pre-processamento, são geradas 3 tabelas a parti das tabelas originais do MIMIC: 
- `ck_events.csv`: tabela com todos os exames CK (CPK) realizados
- `pacients_with_ck.csv`: informações dos pacientes (peso, altura, IMC e pressão arterial) que realizaram exames de CK (CPK)
- `insulin_inputs_in_ck_pacients.csv`: todos os eventos de aplicação de insulina em pacientes que fizeram algum exame de CK (CPK).`

Para realizar as primeiras análises, foi necessário aplicar alguns passos de limpeza de dados. Mais detalhes podem ser encontrados no notebook [limpeza_de_dados.ipynb](notebooks/limpeza_de_dados.ipynb). Após essa limpeza, são geradas 2 tabelas a parti das tabelas intermediarias geradas anteriormente:
- `bmi_norm.csv`: tabela das informações dos pacientes após filtragem de valores de BMI (IMC), com remoção de valores de BMI (IMC) extremamente elevados
- `ck_norm.csv`: tabela dos exames CK (CPK) após filtragem de valores de CK considerados outliers 

### Integração entre Bases e Análise Exploratória

> TODO:
> Descreva etapas de integração de fontes de dados e apresente a seguir uma análise exploratória que envolva ambas.
> Inclua um sumário com estatísticas descritivas da(s) base(s) de estudo.
> Utilize gráficos que descrevam os aspectos principais da base que são relevantes para as perguntas de pesquisa consideradas.

# Ferramentas

- [Python](https://www.python.org/)
- [jupyter](https://jupyter.org/)
- [pandas](https://pandas.pydata.org/)
- [scipy](https://scipy.org/)
- [numpy](https://numpy.org/)

# Cronograma

1. Processar dados do MIMIC-IV: 3 semanas
3. Usar técnicas de análise estatística: 4 semanas
4. Escrever o texto relativo aos resultados obtidos na 3 etapa: 3 semanas
