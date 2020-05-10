import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math
import time
import datetime
import operator
import sklearn
#from sklearn import linear_model
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.svm import  SVR
from sklearn.metrics import  mean_squared_error, mean_absolute_error
plt.style.use('seaborn')



data = pd.read_csv("CA_COVID.csv")

# print(data.head())

predict = "LAST"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=.9)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print("How accurate the model will be: ", acc)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
	print("\n#", x, "Program predicts: ", predictions[x], "\n#", x, "Actual answer for last day: ", y_test[x])
