# importing libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import rand
from numpy.random import seed
from scipy.stats import spearmanr


d1=pd.read_excel('dbSaudeManipulado.xlsx')
d2= pd.read_excel('dbSaudeManipulado.xlsx')
d3= pd.read_excel('dbSaudeManipulado.xlsx')
dc=pd.read_excel('dbSaudeManipulado.xlsx')
dados=pd.read_excel('dbSaudeManipulado.xlsx')

#age_group

# separação por idade
d1.query('BMI == 0', inplace = True)
d2.query('BMI == 1', inplace = True)


age1D= d1.loc[:,"pre-infection"]
age2D=d2.loc[:,"pre-infection"]
age3D= d3.loc[:,"pre-infection"]

age1G= d1.loc[:,"max_dg_sev_during_hospitalization"]
age2G=d2.loc[:,"max_dg_sev_during_hospitalization"]
age3G= d3.loc[:,"max_dg_sev_during_hospitalization"]


#calculo da correlação
coef, p = spearmanr(age3D, age3G)
print(coef, p)

#plot da correlção
sns.regplot(x="pre-infection", y= "max_dg_sev_during_hospitalization",ci = None,data=d1,color='darkgreen')
ticks, labels = plt.yticks()
plt.yticks(ticks, labels=['','','Leve','', 'Moderado','','Grave','','Critico',"",""])
plt.xlabel('Vitamina D(ng/mL)')
plt.ylabel('Gravidade COVID-19')

plt.show()