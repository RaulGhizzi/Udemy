#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:27:14 2017

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

##Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc_x = StandardScaler()
#x = sc_x.fit_transform(x)
#sc_y = StandardScaler()
#y = sc_y.fit_transform(y)
               
# Fitting Decision Tree to data set
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x, y)

# Predicting 
y_pred = regressor.predict(6.5)


#Increment precision in X
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'green')
plt.plot(x_grid, regressor.predict(x_grid), color = 'pink')
plt.title('Decision Tree')
plt.xlabel('Position Level')
plt.ylabel('Salary')


