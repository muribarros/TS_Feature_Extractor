import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



lista = []

techs  = ['glcm_RMf_True','glcm_RMf_False','glcm_RMs_True','glcm_RMs_False','glrlm_RMf_True','glrlm_RMf_False','glrlm_RMs_True','glrlm_RMs_False','glszm_RMf_True','glszm_RMf_False','glszm_RMs_True','glszm_RMs_False','ngtdm_RMf_True','ngtdm_RMf_False','ngtdm_RMs_True','ngtdm_RMs_False']
classif = 'SVM'

#for classif in ['SVM','NB']: #Classificador 
img = pd.read_csv(classif + '_regiao_de_interesse.csv', sep=';')    
rois=img['Name'].tolist()
classif_matriz = np.zeros((len(techs),len(img))) 
    
for i, tech in enumerate(techs): #Tecnicas 
    img2 = pd.read_csv(classif+'_'+tech+'.csv', sep = ';')
    img2 = img2.sort_values(by='accuracy')
    regiao_ordenada=img2['Name'].tolist()
    print(classif+'_'+tech+'.csv')
    for j, roi in enumerate(rois): #Regioes
        #print(regiao_ordenada.index(roi))
        classif_matriz[i,j] = regiao_ordenada.index(roi)
#region = ['a_','b_','c_','d_','e_']
#tech = ['t_1','t_2','t_3','t_4']

df_matriz = pd.DataFrame(classif_matriz)

df_matriz.columns = rois
df_matriz.index = techs
#sns.lineplot(data=df)
plt.ylabel('Rank')
plt.xlabel('Technique')
g = sns.scatterplot(data = df_matriz)
g.set_xticks(range(len(techs)))
g.set_xticklabels(techs, rotation= 90)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#g.figure.savefig(classif + '_regiao_tecnica' +'.eps',bbox_inches='tight')

    
                                 