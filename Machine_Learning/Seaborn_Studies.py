#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:02:34 2017

@author: gaulbg
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

os.chdir('/home/gaulbg/Git/Udemy/Machine_Learning') 

# Visualizing Linear Regression

#Import Dataset
dataset = pd.read_csv('50_Startups.csv')
#Independent Variable X
x = dataset.iloc[:,:-1].values
#Dependent Variable Y
y = dataset.iloc[:,1].values

plt1 = sns.distplot(dataset["Profit"])

boxplot1 = sns.boxplot(data = dataset, x = "State", y = "Profit")

linplot1 = sns.lmplot(data = dataset, x = "Profit", y = "R&D Spend")
linplot2 = sns.lmplot(data = dataset, x = "Profit", y = "Administration")
linplot3 = sns.lmplot(data = dataset, x = "Profit", y = "Marketing Spend")

hueplot1 = sns.lmplot(data = dataset, x = "Profit", y = "R&D Spend",
                      fit_reg = False, hue = "State")
hueplot2 = sns.lmplot(data = dataset, x = "Profit", y = "Administration",
                      fit_reg = False, hue = "State")
hueplot3 = sns.lmplot(data = dataset, x = "Profit", y = "Marketing Spend",
                      fit_reg = False, hue = "State")

# Visualizing Clusters

# Importing the dataset
dataset2 = pd.read_csv('Mall_Customers.csv')

# Find the number of categories
# bins = 5
distplot1 = sns.distplot(dataset2["Spending Score (1-100)"])
# bins = 3
distplot2 = sns.distplot(dataset2["Annual Income (k$)"])
# bins = 3
distplot3 = sns.distplot(dataset2["Age"])

dataset2["Income Group"] = pd.cut(dataset2["Annual Income (k$)"],
                                  bins = 3,
                                  labels = ["Low", "Medium", "High"])
dataset2["Age Group"] = pd.cut(dataset2["Age"],
                               bins = 3,
                               labels = ["Low", "Medium", "High"])


boxplot1 = sns.boxplot(data = dataset2,
                       x = "Genre",
                       y = "Spending Score (1-100)")

linplot1 = sns.lmplot(data = dataset2,
                      x = "Age",
                      y = "Spending Score (1-100)")
linplot2 = sns.lmplot(data = dataset2,
                      x = "Annual Income (k$)",
                      y = "Spending Score (1-100)")

hueplot1 = sns.lmplot(data = dataset2,
                      x = "Age",
                      y = "Spending Score (1-100)",
                      fit_reg = False,
                      hue = "Income Group",
                      size = 10,
                      aspect = 1.5,                    
                      legend_out = True)

#Visualização Interessante
hueplot2 = sns.lmplot(data = dataset2,
                      x = "Annual Income (k$)",
                      y = "Spending Score (1-100)",
                      fit_reg = False,
                      hue = "Age Group",                    
                      size = 10,
                      aspect = 1.5,                      
                      legend_out = True)











