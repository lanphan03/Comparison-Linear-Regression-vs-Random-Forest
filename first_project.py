# -*- coding: utf-8 -*-
"""first-project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x0pITwkgXKet7-uSFg4kPMTLsaO39ilh

#**My First ML Project**

##Load data
"""

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
df

"""##Data Preparation

"""

y = df['logS']
y

x=df.drop('logS', axis = 1)
x

"""### Data Splitting

"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)
x_train

x_test

"""##**MODEL BUILDING**

### Linear Regression

####Training Model
"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)
LinearRegression()

"""####Applying the model to make the prediction"""

y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)
y_lr_train_pred

y_lr_test_pred

"""####Evaluating the model performance

"""

y_train

y_lr_train_pred

from sklearn.metrics import mean_squared_error, r2_score
lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)
lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)
print('LR MSE(train): ', lr_train_mse)
print('LR MSE(test): ', lr_test_mse)
print('LR R2(train): ', lr_train_r2)
print('LR R2(test): ', lr_test_r2)

lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Methods', 'Training MSE', 'Training R2', 'Testing MSE', 'Testing R2']
lr_results

"""###Random Forest

####Training Model
"""

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=2, random_state = 100)
rf.fit(x_train, y_train)

"""####Applying the model to make the prediction"""

y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)
y_rf_train_pred

"""####Evaluating the model performance




"""

from sklearn.metrics import mean_squared_error, r2_score
rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)
rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)
print('RF MSE(train): ', rf_train_mse)
print('RF MSE(test): ', rf_test_mse)
print('RF R2(train): ', rf_train_r2)
print('RF R2(test): ', rf_test_r2)

rf_results = pd.DataFrame(['Random Forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Methods', 'Training MSE', 'Training R2', 'Testing MSE', 'Testing R2']
rf_results

"""##Model Comparison

"""

df_models=pd.concat([lr_results, rf_results], axis = 0)
df_models

"""##Data Visualization

"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(5,5))
plt.scatter(x=y_train,y=y_lr_train_pred, c='#7CAE00', alpha=0.3)

z=np.polyfit(y_train, y_lr_train_pred, 1)
p=np.poly1d(z)

plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predict logS')
plt.xlabel('Experimental logS')