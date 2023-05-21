dinamo
==============================

# Modelo para Apresentação do Projeto

# Projeto `<Título em Português>`
# Project `<Title in English>`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2023, na Unicamp.

> ## **Membros do grupo.**
> |**Nome**  | **RA** | **Especialização**|
> |--|--|--|
> | Lidia Regina de Carvalho Freitas Barban  | 20362  | Saúde|
> | **Wladimir Arturo Garces Carrillo**  | **204059**  | **Ciência da Computação - Líder Github - @WladIMirG**|
> | Luciano de Melo Martins  | 223825  | Ciência da Computação|
> | Denise Fernandes Barbosa  | 161452  | Ciências da Cirurgia|


# Descrição Resumida do Projeto
> Este projeto busca a identificação de eventos hipoglicêmicos e hiperglicêmicos em sinais biológicos de eletrocardiograma de ECG, utilizando o conjunto de dados D1NAMO [1] e com base na metodologia descrita em Dave. D. [2].

<!-- > Descrição do tema do projeto, incluindo motivação e contexto gerador.
> 
> Link para vídeo de apresentação da proposta do projeto (máximo 3 minutos). -->

# Perguntas de Pesquisa
> Perguntas de pesquisa que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.

# Bases de Dados

Neste projeto, pretendemos utilizar um conjunto de dados abertos que relaciona medidas biométricas obtidas por dispositivos vestíveis aos níveis glicêmicos.

## O Conjunto de Dados Abertos D1NAMO
O D1NAMO é um conjunto de dados composto por 2 subconjuntos[1]. Ele reúne informações de 29 pacientes, sendo 9 pacientes com diagnóstico de diabetes e 20 pacientes com diagnóstico saudável, que foram cuidadosamente monitorados ao longo de 4 dias. Ambos os subconjuntos possuem as seguintes características:

- Sinais de ECG.
- Sinais de respiração.
- Saídas do acelerômetro.
- Medidas de glicose (o método difere entre os subconjuntos).
- Imagens de alimentos e anotações feitas por um nutricionista.

Os sinais de ECG, respiração e acelerômetro, com frequências de amostragem de 250, 18 e 100 Hz, respectivamente, são provenientes do dispositivo Zephyr BioHarness 3. Para a glicose, dois métodos diferentes foram aplicados no caso de pessoas com diagnóstico de diabetes: um sensor CGM iPro2 Professional, que por meio do Monitoramento Contínuo de Glicose realizou amostras a cada 5 minutos. No caso dos pacientes saudáveis, as amostras de glicose foram relacionadas ao momento em que o paciente se alimentou. As imagens dos alimentos foram tiradas no momento em que o paciente estava prestes a consumi-los e, além disso, anotações foram geradas em relação à qualidade e valor nutricional dos alimentos.

No total, foram coletadas ${\sim}$1550 horas de sinais biométricos, ${\sim}$8884 medidas de glicose, 473 anotações de alimentos e 352 imagens de alimentos [1].

# Metodologia

Inicialmente, a metodologia que utilizaremos será a descrita em Dave. D. et al.[2]. Também colocamos no radar o método utilizado em Porumb, M. et al.[3].
<!-- 
> Esta seção será evoluída ao longo do projeto. Nesta primeira entrega informe técnicas que pretende-se explorar
> tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas. Para a primeira entrega, descreva de maneira mais genérica que tipo de abordagem seu grupo pretende realizar. -->

# Ferramentas
> Ferramentas a serem utilizadas (com base na visão atual do grupo sobre o projeto).

# Cronograma
> Proposta de cronograma. Procure estimar quantas semanas serão gastas para cada etapa do projeto.

# Bibliografia
<div class="csl-entry">

> [1] Dubosson, F., Ranvier, J. E., Bromuri, S., Calbimonte, J. P., Ruiz, J., &#38; Schumacher, M. (2018). The open D1NAMO dataset: A multi-modal dataset for research on non-invasive type 1 diabetes management. <i>Informatics in Medicine Unlocked</i>, <i>13</i>, 92–100. https://doi.org/10.1016/J.IMU.2018.09.003
</div>

<div class="csl-entry">

> [2] Dave, D., Vyas, K., Branan, K., McKay, S., DeSalvo, D. J., Gutierrez-Osuna, R., Cote, G. L., &#38; Erraguntla, M. (2022). Detection of Hypoglycemia and Hyperglycemia Using Noninvasive Wearable Sensors: ECG and Accelerometry. <i>Journal of Diabetes Science and Technology</i>. https://doi.org/10.1177/19322968221116393
</div>

<div class="csl-entry">

> [3] Porumb, M., Stranges, S., Pescapè, A., &#38; Pecchia, L. (2020). Precision Medicine and Artificial Intelligence: A Pilot Study on Deep Learning for Hypoglycemic Events Detection based on ECG. <i>Scientific Reports 2020 10:1</i>, <i>10</i>(1), 1–16. https://doi.org/10.1038/s41598-019-56927-5
</div>

