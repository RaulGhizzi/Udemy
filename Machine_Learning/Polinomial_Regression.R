#Polynomial Regression
#install.packages('ggplot2')

#Data Processing
setwd("~/Git/Udemy/Machine_Learning")
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# #Splitting Data
# #install.packages('caTools')
# library(caTools)
# 
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# 
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# #Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# 

# Fitting Linear Regression
lin_reg = lm(formula = Salary ~ .,
             data = dataset)

# Fitting Polynomial Regression
# Insert the polinomial levels
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

poly_reg = lm(formula = Salary ~ .,
              data = dataset)

# Visualizing Linear model
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
            color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Linear Model') + 
  xlab('Leavel') + 
  ylab('Salary')

# Visualizing Polynomial model
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Polynomial Model') + 
  xlab('Leavel') + 
  ylab('Salary')

# Predict with Linear Regression
y_pred_lin = predict(lin_reg, newdata = data.frame(Level = 6.5))
# Predict with Polynomial Regression
y_pred_poly = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                     Level2 = 6.5^2,
                                                     Level3 = 6.5^3,
                                                     Level4 = 6.5^4))

