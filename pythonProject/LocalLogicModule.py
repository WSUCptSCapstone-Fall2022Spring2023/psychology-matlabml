"""
This file contains the class which stores algorithms that will be run locally.
It will have one class, LocalLogic, which holds the algorithm for testing the accuracy of a machine learning model and running the model against experiment data to make predictions on the data.
"""

from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score, r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from Preprocessing_Module_Binary_Classifier import *
from matplotlib import pyplot as plt

class LocalLogicModule:

    def __init__(self, lambda_val):
        self.lambda_val = lambda_val
        self.model = 0

    def fit(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def calculate_mse(self, y_pred, y_test):
        return mean_squared_error(y_pred, y_test)

    def predict(self, x_test):
        return self.model.predict(x_test)

    def test_accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    #def graph_accuracy(self, mse_arr, coef_arr):
     #   plt.plot(self.lambda_val, mse_arr)  # plot a graph of lambda values vs MSEs
      #  plt.xlabel("Lambda Value")
       # plt.ylabel("Mean Squared Error")
      #  plt.show()  # open window displaying graph
      #  for coef in coef_arr:
       #    print(coef)

    def train_binary_model_vapor_room_air(self, dataframe):
        """Method which builds a model for predicting on if a rodent is exposed to room air or alcohol vapor"""
        print("Building Room Air vs Vapor Model")

        # set the target condition
        target = 'Condition'

        # create model
        # max_iter is the maximun number of iterations we run to try to converge the model
        self.model = Lasso(alpha=self.lambda_val, max_iter=10000000)

        # retrieve data from dataframe
        y = dataframe[target]
        features = list(dataframe.columns.values)
        features.remove('Condition')
        features.remove('Unnamed: 0')
        x = dataframe[features]

        # Split data
        print("Splitting Data")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

        # fit data to the model
        print("Fitting Data")
        self.fit(x_train, y_train)

        # make a prediction on the fit and print accuracy
        print("Predicting on Data")
        y_prediction = self.predict(x_test)
        print("Mean Squared Error: {}".format((mean_squared_error(y_test, y_prediction))))
        print("R Squared Score: {}".format(r2_score(y_test, y_prediction)))



if __name__ == "__main__":
    loader = LoadData(r'D:\CS 421\Binary_Predictor_Data\output.xlsx')
    learning_rate = 0.000001 # this value is necessary for the model to converge
    model_object = LocalLogicModule(learning_rate)
    model_object.train_binary_model_vapor_room_air(loader.df)
    print("\n\nDone\n\n")

