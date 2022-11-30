import pythonProject.LocalLogicModule


def TestLambdaValues(model, x_train, y_train, x_test, y_test):
    lambda_vals = [0.000001, 0.0001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1]  # set lambda. review documentation for explanation on what this does
    for val in lambda_vals:
        model = Lasso(val)
        lasso = LocalLogic(val, model)  # create lasso model
        lasso.Fit(x_train, y_train)  # fit lasso model to our training data
        y_pred = lasso.Predict(x_test)  # make a prediction
        mse_lasso = lasso.mean_squared_error(y_pred, y_test)  # calculate the mean squared error of the prediction
        print(("\nLasso MSE with Lambda={} is {}").format(val, mse_lasso))

    

if __name__ == "__main__":
    