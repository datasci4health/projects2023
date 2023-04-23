# Projeto Avaliação do papel dos níveis de vitamina D no desenvolvimento, gravidade e desfechos da COVID19
# Project Assessment of the role of vitamin D levels in the development, severity, and outcomes of COVID-19.

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp.

> |Nome  | RA | Especialização|
> |--|--|--|
> | Carla Regina da Silva Corrêa da Ronda  | 265769  | Saúde|
> | Eduarda Simonis Gavião  | 254615  | Computação
> | Leonardo de Queiroz Borges  | 177829  | Computação
> | Maurício Pereira Lopes  | 225242  | Computação - Líder Github - conta: [*mauricioplopes*](https://github.com/mauricioplopes/projects2023)|
> | Miguel Angel Gaybor Murillo  | 252040  | Elétrica|


# Descrição Resumida do Projeto
> A COVID-19 é uma doença infecciosa, causada pelo vírus SARS-CoV-2, um novo tipo de coronavírus que se apresenta com amplo espectro de desfechos clínicos, que vão desde quadros assintomáticos, passando por sintomas leves ou moderados do trato respiratório superior, até a condição de síndrome respiratória aguda grave (SRAG), que pode levar à falência de múltiplos órgãos, culminando em morte.
>
> Estudos mostraram que idosos e pessoas com comorbidades como diabetes mellitus, doenças cardiovasculares, hipertensão arterial e doenças respiratórias crônicas são mais suscetíveis a desenvolver formas graves da doença COVID-19.
>
> Além disso, há evidências crescentes de que a deficiência e insuficiência de vitamina D (VD) estão fortemente associadas a um risco aumentado de adquirir infecção por COVID-19. A VD demonstrou desempenhar papéis importantes na função imunomoduladora, anti-inflamatória, na indução da apoptose, na formação de peptídeos antimicrobianos e no receptor da vitamina D (VDR) por meio da interação da 1,25-dihidroxi vitamina D3, forma ativa da VD.
>
> Nesse contexto, o presente estudo busca identificar uma associação entre as concentrações plasmáticas de vitamina D e a gravidade da doença em pacientes com COVID-19, e para a análise estatística será utilizado banco de dados públicos que contenham informações relevantes para o estudo em questão, como dados demográficos e clínicos dos pacientes diagnosticado positivo para COVID-19.
> 
> [*Video de apresentação do grupo e do projeto*](https://drive.google.com/drive/folders/1hgEvyLqSxztjqW_8qDRckYYHi-u9e789?usp=sharing).

# Perguntas de Pesquisa
> 1- A deficiência ou insuficiência nos níveis de vitamina D podem estar associadas ao desenvolvimento de quadros mais graves da doença COVID-19?
>
> 2- Os níveis plasmáticos de vitamina D pré infecção podem ser considerados fatores de risco para o desenvolvimento de quadros graves da COVID19?

# Bases de Dados
> Candidato 1: Pre-infection 25-hydroxyvitamin D3 levels and association with severity of COVID-19 illness.
>
> Candidato 2: No association between vitamin D status and COVID-19 infection in São Paulo, Brazil.

# Metodologia
> Com base nos artigos relacionados a temática, duas vertentes metodológicas serão implementadas. Uma partindo da análise estatística, em que variáveis contínuas terão media, desvio padrão, mediana e variância como parâmetros, enquanto as qualitativas serão representadas por frequências e percentis. Em contramão, a análise em rede também será aplicada, a fim de encontrar padrões de comunicação entre formas graves da doença COVID-19 e os níveis de deficiência e insuficiência de vitamina D.

# Ferramentas
> Por conter um vasto conjunto de bibliotecas estatísticas, gráficas e numéricas, optou-se pela utilização da ferramenta Python, que além da implementação mais "simplificada" faz parte do conhecimento de todos os participantes do projeto.

# Cronograma
> 
<table>
<thead>
  <tr>
    <th rowspan="3"><br><br>Atividades<br></th>
    <th colspan="12">Mês</th>
  </tr>
  <tr>
    <th colspan="4">Abril</th>
    <th colspan="4">Maio</th>
    <th colspan="4">Junho</th>
  </tr>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Escolha do tema</td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Escolha da base da dados</td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Entrega 1ª versão</td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Preparação dos dados</td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Implementação</td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Entrega 2ª versão</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Aplicação da Metodologia</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Análise dos resultados</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Escrita do relatório</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
    <td>X</td>
    <td></td>
  </tr>
  <tr>
    <td>Entrega final</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>X</td>
  </tr>
</tbody>
</table>
