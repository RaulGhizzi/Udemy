#Data Processing
setwd("~/Git/Udemy/Machine_Learning")
dataset = read.csv("Salary_Data.csv")

library(caTools)

set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting Simple Linear Regression to the training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

#Predicting the Test set
y_pred = predict(regressor, newdata = test_set)

# Visualising the Training set
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'yellow') +
  ggtitle('Salary vs Experience (Training set)') + 
  xlab('Years of experience') +
  ylab('Salary')


# Visualising the Test set

ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'yellow') +
  ggtitle('Salary vs Experience (Training set)') + 
  xlab('Years of experience') +
  ylab('Salary')


