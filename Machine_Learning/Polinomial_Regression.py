#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:16:44 2017

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

#Spliting Dataset
#No need, too small of a data set.

#Fitting Linear Regression to the data set
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

#Fitting Polynomial Regression to the date set
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 6)
x_poly = poly_reg.fit_transform(x)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

#Visualizing the Linear Regression
plt.scatter(x, y, color = 'green')
plt.plot(x, lin_reg.predict(x), color = 'pink')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#Visualize the Polynomial Regression

#==============================================================================
# #Increment precision in X
# x_grid = np.arange(min(x), max(x), 0.1)
# x_grid = x_grid.reshape((len(x_grid), 1))
# plt.plot(x_grid, lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color = 'pink')

#==============================================================================
plt.scatter(x, y, color = 'green')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'pink')
plt.title('Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')

#Predict a new result with Linear Regression
lin_reg.predict(6.5)

#Predict a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))






