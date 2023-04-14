# Projeto `DataBetes - Prevendo Diabetes`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp, pelos membros:


> |Nome  | RA | Especialização|
> |--|--|--|
> | Ana Carolina Benite Alves  | 165741  | Saúde|
> | João Victor Palhares Barbosa  | 173664  | Computação - Líder Github - Conta jvpalhares |
> | Caique Santos Lima  | 217040  | Eng. Elétrica e Computação |
> | Gustavo Pessoa Caixeta Pinto de Luz  | 271582  | Computação |


# Descrição Resumida do Projeto
> Descrição do tema do projeto, incluindo motivação e contexto gerador.

> O projeto busca entender como os hábitos de uma pessoa ligados ao contexto social e econômico em que ela está inserida podem afetar no desenvolvimento de diabetes, a partir do uso de aprendizado de máquina. O contexto gerador foi o interesse em trabalhar com o problema de diabetes que foi um elo entre os membros que vieram de diferentes cursos. O resultado do projeto poderá ser utilizado como medida auxiliadora de políticas públicas ao entender quais populações tem o maior risco de desenvolver diabetes. 

> Link para vídeo de apresentação da proposta do projeto (máximo 3 minutos).

> https://youtu.be/Ti_Q1Hb_aM4

# Perguntas de Pesquisa
> Perguntas de pesquisa que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.

>  Investigar se uma pessoa tem ou não diabetes baseado em fatores sociais, econômicos e de saúde em grandes capitais do Brasil.
# Bases de Dados
> Elencar bases de dados candidatas a serem utilizadas no projeto.

> Link da base oficial: https://svs.aids.gov.br/download/Vigitel/

> Segundo o ministério da saúde: "trata-se de dados de um dos mais tradicionais questionários de saúde do Brasil, o Sistema de Vigilância de Fatores de Risco e Proteção para Doenças Crônicas por Inquérito Telefônico, o Vigitel. Os resultados desse sistema subsidiam o monitoramento das metas propostas no Plano de Ações Estratégicas para o Enfrentamento das Doenças Crônicas Não Transmissíveis no Brasil 2011-2022 e do Plano de Ações Estratégicas para o Enfrentamento das Doenças Crônicas e Agravos não Transmissíveis no Brasil 2021-2030, entre outros, a nível global." Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2022/setembro/com-entrevistas-por-telefone-saude-comeca-operacao-do-vigitel-2022

> Link do google drive com subsets da base e dicionários de dados com pré seleção de features: https://drive.google.com/drive/folders/1NMwv2sC3bnlQBedWxnHki7KG_jT0peuU?usp=sharing

> Segunda opção de base: base de diabetes internacional já com processamentos e dados de saúde das pessoas: https://data.mendeley.com/datasets/wj9rwkp9c2/1/files/2eb60cac-96b8-46ea-b971-6415e972afc9



# Metodologia
> Esta seção será evoluída ao longo do projeto. Nesta primeira entrega informe técnicas que pretende-se explorar
> tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas. Para a primeira entrega, descreva de maneira mais genérica que tipo de abordagem seu grupo pretende realizar.

> A metodologia prevista é o CRISP-DM, em que será desenvolvido um modelo de classificação de aprendizado supervisionado que retorna a classe de uma pessoa ser diabética ou não. Antes de o desenvolver, será realizado um entendimento do negócio, análise exploratória de dados, estratificação para ver a diferença por grupos, escolha de features e pré processamento. Depois de chegar em um modelo baseline, ele será refinado até que esteja de acordo com a performance considerada aceitável.Iniciaremos criando um modelo para todas as capitais e caso necessário quebraremos por região se os grupos forem muito diversos. Quando o modelo estiver concluído, será apresentado para a turma, correspondendo a fase de deploy do CRISP-DM.

![Fases da metodologia](img/crispdm.png)
> Fonte: https://www.datageeks.com.br/pre-processamento-de-dados/

# Ferramentas
> Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

> Python, Google Collab,Bibliotecas de manipulação de dados(Pandas,numpy), Bibliotecas de machine learning (Scikit-learn, Tensorflow, Pytorch - a depender da dificuldade do problema) , Bibliotecas de visualização de dados (Matplotlib, seaborn, plotly) e o que mais for necessário para resolver o problema.

# Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.


> |Data  | Entrega Esperada |
> |--|--|
> | 14 de maio | Resultado parcial: análise descritiva estratificada por grupos, modelo baseline. 4 primeiras etapas do CRISP-DM   |
> | 22 de junho | Modelo refinado e finalizado. Últimas etapas de metodologia  |
> | 22 ou 27 de junho  | Apresentação  |

