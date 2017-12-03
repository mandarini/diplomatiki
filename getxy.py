# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:26:54 2017

@author: ANASTASIS
"""
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_json('TESTING_Basmati-Track_2575761290148.json', lines=True) 
dataset1 = dataset[dataset.astype(str)['Points'] != '[]']
dataset1 = dataset1.reset_index(drop=True)



points = np.zeros(shape=(len(dataset1),2))
# = np.zeros(shape=(len(dataset.index),2))

rows=len(dataset1)

for i in range(rows):
    
    man = dataset1.iloc[i].get(0)
    points[i] = np.array([man[0][1],man[0][0]])


#    
#    man = dataset.iloc[0]
#
#    points[0] = np.array([man[0][0][1],man[0][0][0]])
#    
#    
#     
#    man = dataset.iloc[rows]
#
#    points[rows] = np.array([man[0][0][1],man[0][0][0]])
#    
#    
#    