"""
This file contains the class which stores algorithms that will be run locally.
It will have one class, LocalLogic, which holds the algorithm for testing the accuracy of a machine learning model and running the model against experiment data to make predictions on the data.
"""

from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error


class LocalLogicModule:

    def __init__(self, lambda_val, model):
        self.lambda_val = lambda_val
        self.model = model

    def Fit(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def MSE(self, y_pred, y_test):
        return mean_squared_error(y_pred, y_test)

    def Predict(self, x_test):
        return self.model.predict(x_test)

    def TestAccuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

