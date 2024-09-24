# -*- coding: utf-8 -*-
"""Linear Regression_MachineLearning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pmSAQ9U5uEKvZpM8et27zQ-3kI8O1jzK
"""

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()

diabetes.keys()

print(diabetes.keys())

print(diabetes.data)

print(diabetes.DESCR)

diabetes = datasets.load_diabetes()

# diabetes_X =  diabetes.data
diabetes_X =  diabetes.data[:,np.newaxis,2]

print(diabetes_X)

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes_X[-30:]
diabetes_X_test = diabetes_X[-30:]

diabetes_y_train =diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train,diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)
print(diabetes_y_predicted)

print("Mean squared error is: ",mean_squared_error(diabetes_y_test,diabetes_y_predicted))

print("Weights",model.coef_)
print("Intercept",model.intercept_)

plt.scatter(diabetes_X_test,diabetes_y_test)
plt.plot(diabetes_X_test,diabetes_y_predicted)
plt.show()



