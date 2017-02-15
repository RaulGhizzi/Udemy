#Data Processing
setwd("~/Git/Udemy/Machine_Learning")
dataset = read.csv("50_Startups.csv")
# dataset = dataset[, 2:3]

#Encoding Categorical
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))



#Splitting Data
#install.packages('caTools')
library(caTools)

set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting Multiple Linear Regression to Training set
# regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
#                data = training_set)
#The dot at the end calls for all the other features in the set
regressor = lm(formula = Profit ~ .,
               data = training_set)

#Predictor
y_pred = predict(regressor, newdata = test_set)

#Optimizing with Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
summary(regressor)
#Remove State
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
summary(regressor)
#Remove Adm
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
summary(regressor)

