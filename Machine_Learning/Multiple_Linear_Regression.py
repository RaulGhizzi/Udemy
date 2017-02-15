#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:19:26 2017

@author: gaulbg
"""

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv("50_Startups.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values


#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 3] = labelencoder_x.fit_transform(x[:, 3]) 
onehotencoder = OneHotEncoder(categorical_features = [3])
x = onehotencoder.fit_transform(x).toarray()

#Avoiding Dummy Variable Trap
x = x[:,1:]

#Spliting Dataset
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

#Optimizing with Backward Elimination
import statsmodels.formula.api as sm
x = np.append(arr = np.ones(shape=(50,1)).astype(int), values = x , axis = 1)
#Significance_level
sl = 0.05

#Start Elimination (if max(P-value) in x > sl: remove columns else model is ready)

#Select Columns to keep
x_opt = x[:,[0, 1, 2, 3, 4, 5]]
#Object Least Squares (OLS)
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0, 1, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0, 3, 4, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0, 3, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0, 5]]
regressor_ols = sm.OLS(endog = y, exog = x_opt).fit()
regressor_ols.summary()









