#-------------------------------------//--------------------------------------
#                         REGION MATRIX GENERATION
#-------------------------------------//--------------------------------------

import numpy as np


regions = np.load('final_intersection_list.npy')    

#--------------------------------------------------
#LISTA A PARTIR DE UM TXT
#--------------------------------------------------

with open('register_list.txt', 'r') as f:
    patients = [[str(entry) 
                  for entry in line.split()] 
                 for line in f.readlines()]
    print(pacientes)
   
    
#--------------------------------------------------
# Condition (All patients in all regions 
#--------------------------------------------------


for region in regions:
    
    for it, patient in list(enumerate(patients)):
        a = np.load('/Users/Lab/Documents/Murilo/glrlm_RMs/' + paciente[0] + '/region_' + str(regiao) + '.npy')
        
        if it == 0:
            matriz = a
           
        else:
            matriz = np.vstack((matriz,a))
            
            
    np.save('/Users/Lab/Documents/Murilo/glrlm_RMs_Matriz/Matriz_' + str(regiao), matriz)

# =============================================================================
#                          REGION MATRIX GENERATION
# =============================================================================
