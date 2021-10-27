#-------------------------------------//--------------------------------------
#                          GERAR MATRIZ DE REGIÕES
#-------------------------------------//--------------------------------------

import numpy as np


regioes = np.load('Lista_final_interseccao.npy')    

#--------------------------------------------------
#LISTA A PARTIR DE UM TXT
#--------------------------------------------------

with open('lista_registro.txt', 'r') as f:
    pacientes = [[str(entry) 
                  for entry in line.split()] 
                 for line in f.readlines()]
    print(pacientes)
   
    
#--------------------------------------------------
# CONDIÇÃO (Todos os pacientes em todas as regiões 
#--------------------------------------------------


for regiao in regioes:
    
    for it, paciente in list(enumerate(pacientes)):
        a = np.load('/Users/Lab/Documents/Murilo/glrlm_RMs/' + paciente[0] + '/region_' + str(regiao) + '.npy')
        
        if it == 0:
            matriz = a
           
        else:
            matriz = np.vstack((matriz,a))
            
            
    np.save('/Users/Lab/Documents/Murilo/glrlm_RMs_Matriz/Matriz_' + str(regiao), matriz)

# =============================================================================
#                            GERAR MATRIZ DE REGIÕES
# =============================================================================
