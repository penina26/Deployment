# Bank Customer Churn Prediction
<img src ='images\isometric-bank-composition-visitors.avif'>
<hr>
## Overview

Churn rate is the measure of how many items or individuals are moving out of a particular group, in this case how many customers are unsubscribing from a bank's services.Customer churn has become a major problem among for many businessed given that their revenue stream is directly related to the amount of customers that subscribe and pay for their services and products therefore earning them revenue. 
<hr>
## Business and Data Understanding

It is important for a business to be able to identify customers at risk of churning and come up with startegies that will maximize the likelihood of the customer staying.This is quite difficult especially for a large banking institution with many different types of customers, to know why a customer is cancelling their subscription to its services because of their different behaviours and preferences.In the current digital environment where it is very easy for a customer to switch from one banking institution to another , customer churn prediction will allow a bank to identify when a customer is about to leave and act proactively to reverse a potential customer chrun and mitigate revenue losses.

This project will use a dataset obtained from 
<a href = 'https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset'> Bank Customer Churn Dataset </a>
.The dataset represents customers of ABC Multinational Bank which is a European bank operational in 3 countries namely France, Germany and Spain. It has 10,000 observations and 12 features.
<hr>
### A Few Findings From EDA
<br>
The bank's customers comprise of more Males than Females.
There are also more female churned customers than there are male, showing that the likelihood of a female customer unsubscribing from the bank's services

<br>
<img src ='images\churn_gender.PNG'>

<br>
<hr>
Germany has the highest number of churned customers, followed closely by France with Spain having the smallest number.

<br>
<img src ='images\country churn.PNG'>
<hr>
Distribution of Churn among the numerical features

<br>
<img src ='images\churn vs various variables.PNG'>


<br>

## Modeling
3 models were used for classification:
<hr>
1. Logistic regression - with a few transformations done to the data.

<br>
<img src ='images\logreg.PNG'>
<hr>
2. Random Forest Classifier
A random forest model that uses a pipeline to pass transformers and GridSearchCv to find the the best hyperparameters for the model.

<br>
<img src ='images\rf.PNG'>

<br>
<hr>
3. XGB Boost Classifier
A more complex model that is fitted to the data after feature engineering and more transformations are done to the data to maximize model performance.

<br>
<img src ='images\xgb.PNG'>

<br>
<hr>
## Evaluation

Various evaluation metrics were employed but f1 score was the most significant as there was a class imbalance propblem.
Overall the XGB classifier performed the best.

<br>
<img src ='images\model performances.PNG'>
<hr>
<br>

<img src ='images\rf cm.PNG'>
<hr>
<br>

<img src ='images\xgb cm.PNG'>
<hr>
<br>

## Conclusion
<hr>
1. The best performing model was the XGB boost which had the highest accuracy score and tied with the Random Forest calssifier on the f1 score.

2. All three models were able to predict the unchurned class well but failed to achieve good scores inpredicting the Unchurned class
<hr>