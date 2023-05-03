"""
This file contains the class which stores algorithms that will be run locally.
It will have one class, LocalLogic, which holds the algorithm for testing the accuracy of a machine learning model and running the model against experiment data to make predictions on the data.
"""
import sklearn.metrics
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import accuracy_score, r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from Load_Data import *
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

    def predict_on_dataframe(self, dataframe, target):
        print("Predicting on dataframe")

        # retrieve data from dataframe
        y = dataframe[target].values
        features = list(dataframe.columns.values)
        features.remove(target)
        features.remove('Unnamed: 0')
        x = dataframe[features].values

        # predict on the data
        prediction = self.model.predict(x)

        return prediction

    def train_binary_model_vapor_room_air(self, dataframe):
        """Method which builds a model for predicting on if a rodent is exposed to room air or alcohol vapor"""
        print("Building Room Air vs Vapor Model")

        # set the target condition
        target = 'Condition'

        # create model
        # max_iter is the maximum number of iterations we run to try to converge the model
        self.model = Lasso(alpha=self.lambda_val, max_iter=100_000, warm_start=True, positive=True)

        #self.model = LassoCV(n_alphas=1, alphas=[0.1], max_iter=100_000, verbose=1, n_jobs=-1)

        # retrieve data from dataframe
        y = dataframe[target].values
        features = list(dataframe.columns.values)
        features.remove(target)
        features.remove('Unnamed: 0')
        x = dataframe[features].values

        # Split data
        print("Splitting Data")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, shuffle=True)

        # fit data to the model
        print("Fitting Data")
        self.model.fit(x_train, y_train)

        # print model parameters
        print("\nPrinting Model Coefficients")
        print(self.model.coef_)

        # predict on the training data
        prediction = self.model.predict(x_train)
        train_accuracy = sklearn.metrics.r2_score(y_train, prediction)

        # predict on the testing data
        prediction = self.model.predict(x_test)
        test_accuracy = sklearn.metrics.r2_score(y_test, prediction)

        return train_accuracy, test_accuracy

    def train_continuos_model_consumption(self, dataframe):
        """Method which builds a model for predicting how much alcohol ing g\kg a rodent has consumed"""
        print("Building Alcohol Consumption Model")

        # set the target condition
        target = 'g/kg'

        # create model
        # max_iter is the maximum number of iterations we run to try to converge the model
        self.model = Lasso(alpha=self.lambda_val, max_iter=10000000)

        # retrieve data from dataframe
        y = dataframe[target]
        features = list(dataframe.columns.values)
        features.remove(target)
        features.remove('Unnamed: 0')
        x = dataframe[features]

        # Split data
        print("Splitting Data")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

        # fit data to the model
        print("Fitting Data")
        self.model.fit(x_train, y_train)

        # print model parameters
        print("\nPrinting Model Coefficients")
        print(self.model.coef_)

        # predict on the training data
        prediction = self.model.predict(x_train)
        train_accuracy = sklearn.metrics.r2_score(y_train, prediction)

        # predict on the testing data
        prediction = self.model.predict(x_test)
        test_accuracy = sklearn.metrics.r2_score(y_test, prediction)

        return train_accuracy, test_accuracy

    def graph_binary_lasso_accuracy(self, dataframe, epochs):
        """This method fits data to a model a number of times equal to the epochs value,
        and then graphs the accuracy over a series of models"""

        test_accuracy_arr = []
        training_accuracy_arr = []
        best_test = 0
        best_model = 0
        for epoch in range(epochs):
            print("\nBuilding Model {} of {}".format(epoch+1, epochs))
            # train the model
            train_accuracy, test_accuracy = self.train_binary_model_vapor_room_air(dataframe)

            if test_accuracy > best_test:
                best_model = self.model

            training_accuracy_arr.append(train_accuracy)
            test_accuracy_arr.append(test_accuracy)
            print("Training Accuracy: {}".format(train_accuracy))
            print("Testing Accuracy: {}".format(test_accuracy))

        average_training_accuracy = sum(training_accuracy_arr)/len(training_accuracy_arr)
        print("Average Training Accuracy: {}".format(average_training_accuracy))

        average_test_accuracy = sum(test_accuracy_arr)/len(test_accuracy_arr)
        print("Average Testing Accuracy: {}".format(average_test_accuracy))

        best_training_accuracy = max(training_accuracy_arr)
        index_training = training_accuracy_arr.index(best_training_accuracy)
        print("Best Training Accuracy: {} for model number {}".format(best_training_accuracy, index_training+1))

        best_testing_accuracy = max(test_accuracy_arr)
        index_testing = test_accuracy_arr.index(best_testing_accuracy)
        print("Best Testing Accuracy: {} for model number {}".format(best_testing_accuracy, index_testing + 1))

        loader.saveModel(best_model, 'model.sav')  # save as a .sav file

        plt.plot(range(1, epochs+1), test_accuracy_arr, label="Test Accuracy")
        plt.plot(range(1, epochs+1), training_accuracy_arr, label="Training Accuracy")
        plt.legend()
        plt.xlabel("Fit Epoch")
        plt.ylabel("R2 Score")
        plt.show()  # open window displaying graph

    def graph_continuous_lasso_accuracy(self, dataframe, epochs):
        """This method fits data to a model a number of times equal to the epochs value,
        and then graphs the accuracy over a series of models"""

        test_accuracy_arr = []
        training_accuracy_arr = []
        best_test = 0
        best_model = 0
        for epoch in range(epochs):
            print("\nBuilding Model {} of {}".format(epoch+1, epochs))
            # train the model
            train_accuracy, test_accuracy = self.train_continuos_model_consumption(dataframe)

            if test_accuracy > best_test:
                best_model = self.model


            training_accuracy_arr.append(train_accuracy)
            test_accuracy_arr.append(test_accuracy)
            print("Training Accuracy: {}".format(train_accuracy))
            print("Testing Accuracy: {}".format(test_accuracy))

        average_training_accuracy = sum(training_accuracy_arr)/len(training_accuracy_arr)
        print("Average Training Accuracy: {}".format(average_training_accuracy))

        average_test_accuracy = sum(test_accuracy_arr)/len(test_accuracy_arr)
        print("Average Testing Accuracy: {}".format(average_test_accuracy))

        best_training_accuracy = max(training_accuracy_arr)
        index_training = training_accuracy_arr.index(best_training_accuracy)
        print("Best Training Accuracy: {} for model number {}".format(best_training_accuracy, index_training+1))

        best_testing_accuracy = max(test_accuracy_arr)
        index_testing = test_accuracy_arr.index(best_testing_accuracy)
        print("Best Testing Accuracy: {} for model number {}".format(best_testing_accuracy, index_testing + 1))

        loader.saveModel(best_model, 'model.sav')  # save as a .sav file

        plt.plot(range(1, epochs+1), test_accuracy_arr, label="Test Accuracy")
        plt.plot(range(1, epochs+1), training_accuracy_arr, label="Training Accuracy")
        plt.legend()
        plt.xlabel("Fit Epoch")
        plt.ylabel("R2 Score")
        plt.show()  # open window displaying graph

    def graph_lambda_accuracy(self, dataframe):
        lambda_vals = [0.000001, 0.0001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1]  # set lambda.
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        accuracy_arr = []
        for val in lambda_vals:
            self.lambda_val = val
            accuracy = self.train_continuos_model_consumption(dataframe)
            accuracy_arr.append(accuracy)
            print(("\nLasso RSqaured Score with Lambda={} is {}").format(val, accuracy))

        plt.plot(x, accuracy_arr)
        plt.xlabel("Lambda Values")
        plt.ylabel("Lasso Score")
        plt.xticks(x, lambda_vals)
        plt.show()



if __name__ == "__main__":

    """Always run this code"""
    learning_rate = 0.01  # set the learning rate
    model_object = LocalLogicModule(learning_rate)  # create the class which will hold the model


    """run this code when training. comment it out when testing a model"""
    #loader = LoadData(r"D:\Capstone\Processed_Dataframes\dataframe_binary_all_subjects.xlsx")  # input the addresses of each dataframe you want to train the model on
    
    """if you want to build one binary model, run this code"""
    #train, test = model_object.train_binary_model_vapor_room_air(loader.df)
    #print("Training Accuracy: {}".format(train))
    #print("Testing Accuracy: {}",format(test))
    #loader.saveModel(model_object.model, 'model.sav')  # save as a .sav file to the location of LocalLogicModule.py

    """if you want to build one continuous model, run this code"""
    #train, test = model_object.train_continuos_model_consumption(loader.df)
    #print("Training Accuracy: {}".format(train))
    #print("Testing Accuracy: {}",format(test))
    #loader.saveModel(model_object.model, 'model.sav')  # save as a .sav file to the location of LocalLogicModule.py

    """if you want to build an array of binary models, run this code
    this code also saves the best model out of the array"""
    #model_object.graph_binary_lasso_accuracy(loader.df, 100) # (data, number of epochs)

    """if you want to build an array of continuous models, run this code
    this code also saves the best model out of the array"""
    #model_object.graph_continuous_lasso_accuracy(loader.df, 100) # (data, number of epochs)

    """if you want to test a saved model, run this code
    the inputted dataframe should be made up of preprocessing one .pl2 file"""
    #dataframe = r'D:\Capstone\79_8232022.xlsx' # dataframe of one file you wish to predict on
    #loader = LoadData(dataframe)
    #model_object.model = loader.loadModel(r"C:\Users\aidan\model.sav") # load the model by inputting the filepath to the file
    #prediction = model_object.predict_on_dataframe(loader.df, 'Condition')  # (dataframe, target column ('Condition' for binary, 'g/kg' for continuous))
    #print('Prediction: {}'.format(prediction))

    """Notes for binary:
    A prediction of above 0.5 for the binary means vapor, otherwise means room air
    the prediction should be bounded between 0 and 1. If it is not, the model might
    be faulty"""
    """Notes for continuous
    The prediction should be bounded from 0 to infinity"""
    
    print("\n\nDone\n\n")

