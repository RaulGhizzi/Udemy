#SVR
#install.packages('ggplot2')

#Data Processing
setwd("~/Git/Udemy/Machine_Learning")
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# #Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# 

# Fitting SVR
# install.packages('e1071')
library(e1071)
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = 'eps-regression')

# Predict with Polynomial Regression
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# Visualizing Linear model
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('SVR') + 
  xlab('Leavel') + 
  ylab('Salary')

