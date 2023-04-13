import sys
import os
from sklearn.model_selection import train_test_split

# Allow access pythonProject files
sys.path.append(os.path.abspath(os.path.join('..', 'pythonProject')))

# Importing pythonProject files
from pythonProject.LocalLogicModule import *
from pythonProject.External_Data_Access_and_Preprocessing_Module import *

# Initializing test class
class LocalLogicModuleTest:

    def TestLambdaValues(self, x_train, y_train, x_test, y_test):
        lambda_vals = [0.000001, 0.0001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1]  # set lambda. review documentation for explanation on what this does
        for val in lambda_vals:
            logic_module = LocalLogicModule(val, Lasso(val))  # create lasso model
            logic_module.Fit(x_train, y_train)  # fit lasso model to our training data
            y_pred = logic_module.Predict(x_test)  # make a prediction
            mse_lasso = logic_module.MSE(y_pred, y_test)  # calculate the mean squared error of the prediction
            print(("\nLasso MSE with Lambda={} is {}").format(val, mse_lasso))

    
# MAIN
if __name__ == "__main__":
    #Preprocess the data
    accessObj = AccessData(r'C:\Users\charl\Desktop\SampleSampleData')
    dataframe = LoadData('test.csv')
    # Initialize the target and feature values
    target = ['A or D']
    features = accessObj.header
    # Create data frame for features and targets
    y = dataframe.df[target]
    x = dataframe.df[features]
    # Split the data into testing and training data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)
    # Test lambda functions to find the most accurate model
    test_logic_module = LocalLogicModuleTest()
    test_logic_module.TestLambdaValues(x_train, y_train, x_test, y_test)