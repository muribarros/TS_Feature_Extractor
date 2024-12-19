#-------------------------------------//--------------------------------------
#                                    SVM
#-------------------------------------//--------------------------------------

#----------------------
# BIBLIOTECA
#----------------------

# Imports
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd

tech = 'glszm'
mod = 'RMs'
comZscore = False
scaler = StandardScaler()

regioes = np.load('Lista_final_interseccao.npy')    
ids_df = pd.read_csv('id_region.csv', sep = ';')

gt_label = np.ones(68)
gt_label[0:34] = gt_label[0:34] * 0

lista = []

for regiao in regioes:
    #(original)matriz = np.load('/Users/Lab/Documents/Murilo/Matriz_GLCM_RMs/Matriz_' + str(regiao) + '.npy')
    matriz = np.load('/Users/Lab/Documents/Murilo/'+ tech +'_'+ mod + '_Matriz/Matriz_' + str(regiao) + '.npy')
    if comZscore:
        scaler.fit(matriz)
        matriz = scaler.transform(matriz)
    
    #print(matriz.shape)# Initialize SVM classifier
    clf = svm.SVC(kernel='linear')
    #print(regiao)
# Fit data
    clf = clf.fit(matriz, gt_label)   
# Predict the test set
    predictions = clf.predict(matriz)
    tn,fp,fn,tp = confusion_matrix(gt_label, predictions).ravel()
    accuracy= (tp + tn) / (tp+tn+fp+fn)
    #print('Accuracy: %f' % accuracy)
    precision = tp / (tp + fp)
    #print('Precision: %f' % precision)
    recall = tp / (tp + fn)
    #print('Recall: %f' % recall)
    f1= 2*((precision*recall)/(precision+recall))
    #print('F1 score: %f' % f1)
    #print('%d,%f,%f,%f,%f' % (regiao, accuracy, precision, recall, f1)) 
    lista.append([int(regiao), accuracy, precision, recall, f1])

results = np.asarray(lista)

results_df = pd.DataFrame(results)
results_df.columns = ['Region', 'accuracy', 'precision', 'recall', 'f1']
ids_df = ids_df.merge(results_df, how='left', on='Region')
ids_df = ids_df.sort_values(by='Region')

ids_df.to_csv('SVM_' + tech + '_' + mod + '_' + str(comZscore)+ '.csv')