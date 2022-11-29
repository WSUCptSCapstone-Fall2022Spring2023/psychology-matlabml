"""
This file contains the class which stores algorithms that will be run locally.
It will have one class, LocalLogic, which holds the algorithm for testing the accuracy of a machine learning model and running the model against experiment data to make predictions on the data.
"""

from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

class LocalLogic:

    def __init__(self, val, model):
        self.val = val
        self.model = Lasso(val)

    def Fit(X, y):
        return self.model.fit(X, y)

    def MeanSquaredError():
        return 

    def Predict(self, x_test):
        return self.model.predict(x_test) 

    def TestAccuracy(y_true, y_pred):
        return accuracy_score(y_true, y_pred)