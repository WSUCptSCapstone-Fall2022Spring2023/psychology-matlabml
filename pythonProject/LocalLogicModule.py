"""
This file contains the class which stores algorithms that will be run locally.
It will have one class, LocalLogic, which holds the algorithm for testing the accuracy of a machine learning model and running the model against experiment data to make predictions on the data.
"""

from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from Preprocessing_Module_Binary_Classifier import *
from matplotlib import pyplot as plt

class LocalLogicModule:

    def __init__(self, lambda_val):
        self.lambda_val = lambda_val
        self.model = None

    def fit(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def calculate_mse(self, y_pred, y_test):
        return mean_squared_error(y_pred, y_test)

    def predict(self, x_test):
        return self.model.predict(x_test)

    def test_accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    def graph_accuracy(self, mse_arr, coef_arr):

        plt.plot(self.lambda_val, mse_arr)  # plot a graph of lambda values vs MSEs
        plt.xlabel("Lambda Value")
        plt.ylabel("Mean Squared Error")
        plt.show()  # open window displaying graph
        for coef in coef_arr:
           print(coef)

    def train_binary_model_vapor_room_air(self):
        """Method which builds a model for predicting on if a rodent is exposed to room air or alcohol vapor"""
        print("Building Room Air vs Vapor Model")

        # make class object for configurations
        cfg = Config()

        # make class object with data formatted into a dataframe
        print("Preprocessing data")
        access_obj = AccessData(r'D:\CS 421\Binary_Predictor_Data', cfg)

        print("Training Model")
        # set the target condition
        target = 'Condition'

        # set learning rate
        learning_rate = 0.001

        # create model
        model = Lasso(self.lambda_val)

        # set current model to what was just produced
        self.model = model

        # retrieve data from dataframe
        y = access_obj.dataframe[target]
        features = access_obj.header
        features.remove('Condition')
        x = access_obj.dataframe[features]

        # Split data
        print("Splitting data")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

        # fit data to the model
        print("Fitting Data")
        self.fit(x_train, y_train)

        # make a prediction on the fit
        y_pred = self.predict(x_test)

        # calculate the mean squared error of the accuracy
        mse_model = self.calculate_mse(y_pred, y_test)

        # print the model's accuracy
        print("\nLasso score is {}".format(self.test_accuracy(list(y_test['Condition']), y_pred)))



if __name__ == "__main__":
    c = LocalLogicModule(0.001)
    c.train_binary_model_vapor_room_air()

