#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:13:51 2017

@author: gaulbg
"""

#Data Preprocessing

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv("Position_Salaries.csv")
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x = sc_x.fit_transform(x)
sc_y = StandardScaler()
y = sc_y.fit_transform(y)
                
                
# Fitting SRV to data set
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(x, y)

# Predicting 
y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

#Visualizing the SVR Regression
plt.scatter(x, y, color = 'green')
plt.plot(x, regressor.predict(x), color = 'pink')
plt.title('SVR')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


