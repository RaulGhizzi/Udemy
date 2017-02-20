#Decision Tree Regression

#install.packages('ggplot2')

#Data Processing
setwd("~/Git/Udemy/Machine_Learning")
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# #Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# 

# Fitting Decision Tree Regression
# install.packages('rpart')
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Predict with Decision Tree Regression
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# Visualizing Linear model
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Decision Tree Regression') + 
  xlab('Leavel') + 
  ylab('Salary')

