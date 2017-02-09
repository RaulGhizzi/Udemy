#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:53:12 2017

@author: gaulbg
"""

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv('Salary_Data.csv')
#Independent Variable X
x = dataset.iloc[:,:-1].values
#Dependent Variable Y
y = dataset.iloc[:,1].values

#Spliting Dataset
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Predict the Test set results
y_pred = regressor.predict(x_test)

#Visualising the Training set
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'green')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualising the Test set
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'green')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


