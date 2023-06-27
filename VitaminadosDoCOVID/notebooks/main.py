import pandas as pd
from scipy import stats
import statistics
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dl=pd.read_excel('dbSaudeManipulado.xlsx')
dm= pd.read_excel('dbSaudeManipulado.xlsx')
dg= pd.read_excel('dbSaudeManipulado.xlsx')
dc=pd.read_excel('dbSaudeManipulado.xlsx')
dados=pd.read_excel('dbSaudeManipulado.xlsx')

#print(dados)

# separação por nível
dl.query('max_dg_sev_during_hospitalization == 0', inplace = True)
dm.query('max_dg_sev_during_hospitalization == 1', inplace = True)
dg.query('max_dg_sev_during_hospitalization == 2', inplace = True)
dc.query('max_dg_sev_during_hospitalization == 3', inplace = True)

#print(dl)
niveis= dados.loc[:,"pre-infection"]
nivelLeve= dl.loc[:,"pre-infection"]
nivelModerado=dm.loc[:,"pre-infection"]
nivelGrave= dg.loc[:,"pre-infection"]
nivelCritico=dc.loc[:,"pre-infection"]


testeWilcoxonLeveModerado= stats.ranksums(nivelLeve,nivelModerado)
print('Valor do teste de Wilcoxon',testeWilcoxonLeveModerado[0])
print('P-value Wilcoxon',testeWilcoxonLeveModerado[1])

testeWilcoxonModeradoGrave= stats.ranksums(nivelModerado,nivelGrave)
print('Valor do teste de Wilcoxon',testeWilcoxonModeradoGrave[0])
print('P-value Wilcoxon',testeWilcoxonModeradoGrave[1])

testeWilcoxonGraveCritico= stats.ranksums(nivelGrave,nivelCritico)
print('Valor do teste de Wilcoxon',testeWilcoxonGraveCritico[0])
print('P-value Wilcoxon',testeWilcoxonGraveCritico[1])

# Calculo das médias
mediaD=statistics.mean(niveis)
mediaL = statistics.mean(nivelLeve)
mediaM = statistics.mean(nivelModerado)
mediaG = statistics.mean(nivelGrave)
mediaC = statistics.mean(nivelCritico)

#Calculo da mediana
medianaD=statistics.median(niveis)
medianaL = statistics.median(nivelLeve)
medianaM = statistics.median(nivelModerado)
medianaG = statistics.median(nivelGrave)
medianaC = statistics.median(nivelCritico)

#calculo da moda
modaD=statistics.mode(niveis)
modaL = statistics.mode(nivelLeve)
modaM = statistics.mode(nivelModerado)
modaG = statistics.mode(nivelGrave)
modaC = statistics.mode(nivelCritico)

#calculo do desvio padrão
dpD=np.std(niveis)
dpL = np.std(nivelLeve)
dpM = np.std(nivelModerado)
dpG = np.std(nivelGrave)
dpC = np.std(nivelCritico)

## Verificar a saida
#print('Média VD Geral',mediaD)
#print('Média VD Leve',mediaL)
#print('Média VD Moderado',mediaM)
#print('Média VD Grave',mediaG)
#print('Média VD Critico',mediaC)

## Preparação para o plot
data = [nivelLeve, nivelModerado, nivelGrave, nivelCritico]
 
fig = plt.figure(figsize =(10, 10))
 
ax = fig.add_subplot(111)

bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)

ax.set_yticklabels(['Leve', 'Moderado',
                    'Grave', 'Crítico'])
#ax.set_xticklabels(['20','40','60','80','100','120','140','160'])

plt.title("Box-plots dos níveis séricos pré-infecção de 25(OH)D")
 
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()



plt.show()

