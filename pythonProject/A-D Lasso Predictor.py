# This is another practice file where I will prove a concept for a lasso predictor. First, import all data from sample
# files into the program and sort them into two arrays by A and D types. Then, for each file, calculate the power for
# each channel in that file and store in a dictionary of arrays. Do the same for coherence for each file.
# The power and coherence values are in arrays, but to avoid an error with numpy we take the mean of the array for now.
# Place all of this data into a pandas dataframe in the following format:
#
# |   Channel 1 Power    |   Channel 2 Power   | ... |   Channel 8 Power   |   Coherence Between 1 and 2   |   Coherence Between 1 and 3   | ... | Coherence Between 7 and 8   |   A or D   |
#             ####                ####                       ####                       #####                       ####                                      ######                   1
#
# The rows will be indexed by file name.
# We use 1 to describe A and 0 to describe D in the dataframe
# Use 80% of the data as training data, keeping 20% as testing Fit the lasso model by using the channel powers and
# coherences as features, and the 'A or D' column as the target. We can also use a series of lambda values to test
# multiple times to find the best fit. Use all of the data to prevent overfitting. We can use os.chdir() to find the
# directory where the data is stored and run on all of it at once

# Additionally, this file does not represent our final software product. As stated above, it is a proof of concept
# for Dr. Henrick's initial assignment of creating an A/D binary classifier

# Import Statements
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from External_Data_Access_and_Preprocessing_Module import AccessData, LoadData


# start of the program
if __name__ == "__main__":

    processingObject = AccessData(r'C:\Users\aidan.nunn\Documents\Homework\CS 421\Sample Data')

    # lists holding the target value we want to predict and the feature values we will use in the prediction
    features = processingObject.header
    target = ['A or D']
    """features = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power',
                'Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8']"""

    dataObject = LoadData(r'C:\Users\aidan.nunn\Documents\Homework\CS 421\Sample Data\test.csv')

    # set y as the target column and x as the features columns
    y = dataObject.df[target]
    x = dataObject.df[features]

    # split the data into test and train sets
    # test_size=0.2 makes it so 80% of data is for training and 20% is for testing
    print("Splitting data")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

    print("Fitting Data")
    lambda_val = [0.000001, 0.0001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1]  # set lambda. review documentation for explanation on what this does
    for val in lambda_val:
        lasso = Lasso(val)  # create lasso model
        lasso.fit(x_train, y_train)  # fit lasso model to our training data
        y_pred = lasso.predict(x_test)  # make a prediction
        mse_lasso = mean_squared_error(y_pred, y_test)  # calculate the mean squared error of the prediction
        print(("\nLasso MSE with Lambda={} is {}").format(val, mse_lasso))
    print(lasso.coef_)
    print("\ndone")
