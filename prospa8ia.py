# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:53:41 2017

@author: ANASTASIS
"""

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_json('TESTING_Basmati-Track_2575761290148.json', lines=True)
geofence = pd.read_json('Geofences.json')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values