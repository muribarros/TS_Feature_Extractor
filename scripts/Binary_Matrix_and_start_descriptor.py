#-------------------------------------//---------------------------------------
#-----------------------------------------------------------------------------
#                  MATRIZ BINARIA E EXTRAÇÃO DE CARACTERISTICA  
#-----------------------------------------------------------------------------
#-------------------------------------//--------------------------------------


#-------------------------------------
# BIBLIOTECA 
#-------------------------------------

import nibabel as nib
import numpy as np
#from scipy.io import  savemat
from six.moves import range
from radiomics import base, cMatrices, deprecated, featureextractor
import os 
import radiomics
from radiomics import glcm
import nrrd

#-------------------------------------
# LEITURA .NPY
#-------------------------------------

regioes = np.load('Lista_final_interseccao.npy')    

#savemat("/Users/Lab/Documents/Murilo/GLCM/" "all_regions_nodes.mat",{"regioes":regioes})    

#-------------------------------------
#LISTA DE PACIENTES (.txt)
#-------------------------------------

with open('lista_registro.txt', 'r') as f:
    pacientes = [[str(entry) 
                  for entry in line.split()] 
                 for line in f.readlines()]
    print(pacientes)

#-------------------------------------
# CONDIÇÃO (Todas as regiões em todos os pacientes (for pacientes + for regiões))
#-------------------------------------

#pacientes = pacientes[0:10]

for paciente in pacientes:
    
    
    #paciente[0] = 'N8' 
    wherefMRI = '/Users/Lab/Documents/Murilo/DataSet_ST_sMRI/'+ paciente[0] + '/orig.nii.gz'
    n1_fMRI = nib.load (wherefMRI) 
    n1_fMRI = n1_fMRI.get_fdata()  
    
    nrrd.write('smri.nrrd', n1_fMRI)
    #print('---------------------------------------------------------------------------------------1')
    
    #savemat('/Users/Lab/Documents/Murilo/Extracao_Matriz_Binaria/'+ paciente[0] + "/fMRI.mat", {"volume":n1_fMRI})
    
    img = nib.load('/Users/Lab/Documents/Murilo/DataSet_ST_sMRI/'+ paciente[0] + '/aparc.DKTatlas+aseg.nii.gz')
    img.shape
    img2 = img.get_data()

    
    for regiao in regioes:
        data = img2.copy()
        data = (data==regiao)*1
        nrrd.write('regiao.nrrd', data)
        #print('---------------------------------------------------------------------------------------2')
        print(paciente[0] + ' - ' + str(regiao))

#-------------------------------------
# GLCM
#-------------------------------------   

        #dataDir = os.path.join(os.getcwd(), '/Users/Lab/Documents/Murilo/GLCM/'+ paciente[0])
        
        #print("dataDir, relative path", dataDir)
        #print("dataDir, absolute path", os.path.abspath(dataDir))

#Leitura da Imagem e Mascara

       # img = os.path.join('n1_fMRI')
       # mask = os.path.join('data')

        
        #paramPath = os.path.join(os.getcwd(), '/Users/Lab/Documents/Murilo/GLCM/'+ paciente[0], 'Params.yaml')
        
       # print ('Parameter file, absolute path', os.path.abspath(paramPath))

#Extração de caracteristicas

        extractor = featureextractor.RadiomicsFeatureExtractor()

        
        #print('Extraction parameters:\n\t', extractor.settings)
        #print('Enabled filters:\n\t', extractor.enabledImagetypes)
        #print('Enabled features:\n\t', extractor.enabledFeatures)

#Resultado
        
        result = extractor.execute('smri.nrrd', 'regiao.nrrd')
        
        #print ('Result type:', type(result))
        #print('')
        #print('Calculated features')
        
        lista = [] #Criar lista vazia
        
        for key, value in result.items():
           if '_glrlm' in key:
               lista.append(value)
               print("/t", key, ":", value)
       
       # np.save('/Users/Lab/Documents/Murilo/GLCM_sMRI/' + paciente[0] + '/region_' + str(regiao), lista)

        break
    break            
                  
  
           # savemat("/Users/Lab/Documents/Murilo/Extracao_Matriz_Binaria/"+paciente[0]+"/regiao_"+str(regiao)+".mat", {"mask":data})

