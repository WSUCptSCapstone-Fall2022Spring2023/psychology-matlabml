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
import os
import sys
import warnings
import ctypes
import numpy as np
import gc
from statistics import mean
from scipy import signal
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from itertools import combinations
import pandas as pd
from pypl2 import pl2_info, pl2_ad, pl2_spikes, pl2_events, pl2_info


# divide a list l into chunks of length n
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# start of the program
if __name__ == "__main__":

    # add all data file names in the target directory to a list

    sDir = r'C:\Users\aidan.nunn\Documents\Homework\CS 421\SampleSampleData'  # Target directory for Aidan's machine.
    # This string needs to be changed for other users.

    fType = '.pl2'  # File type we are looking for

    os.chdir(sDir)  # change the current working directory to where our data is stored.
    files = []  # make a list to store file names
    print("Finding file names")

    # For each file in a list of files in the directory
    for f in os.listdir(sDir):
        if f.endswith(fType):  # if the file ends with our target file type
            files.append(f)  # append it to our list of file names

    # Create a pandas dataframe for use later
    # Rows are indexed by file name, and columns are labeled with each data point we want to store.
    df = pd.DataFrame(index=files, columns=['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                                            'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power',

                                            'Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                                            'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                                            'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                                            'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                                            'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                                            'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                                            'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8',

                                            'A or D'])

    # Get generic file data from each file into a named tuple and put each tuple into an array
    resourceArray = []
    print("Getting generic data")
    for filename in files:
        resource = pl2_info(filename)
        resourceArray.append(resource)

    # Get A/D file data from each file and put each tuple into a dictionary
    # We will store A group data in one dictionary and D group data in another
    ADict = {}  # Dictionary for A group data
    DDict = {}  # Dictionary for D group data
    channelsList = []  # List to hold 0-indexed channel numbers instead of what is listed in the resource tuples
    print("Getting AD data")

    # zip files and resourceArray together so we can iterate through them at the same time
    for filename, resource in zip(files, resourceArray):
        channelNameIterator = 0  # reset iterator between files
        for channel in resource.ad:  # iterate over each channel in a file (8 relevant channels per file)
            if channel.n > 0:  # if a channel has count > 0 then it has data
                ad = pl2_ad(filename, channelNameIterator)  # use pl2_ad to get a/d info from a channel
                if filename.startswith('A'):  # the filename starts with 'A' if it's in the A group
                    ADict[(filename, channelNameIterator)] = ad  # keys are tuples named as (filename, channel number)
                    channelsList.append(channelNameIterator)  # add the channel number to a list for use later
                if filename.startswith('D'):  # the filename starts with 'D' if it's in the D group
                    DDict[(filename, channelNameIterator)] = ad  # keys are tuples named as (filename, channel number)
                    channelsList.append(channelNameIterator)  # add the channel number to a list for use later
            channelNameIterator += 1  # iterate to the next 0-indexed channel number

    del files  # Release memory holding all file names
    gc.collect()
    del resourceArray  # Release memory holding all files generic info
    gc.collect()

    # Lists of channel names to be used in the below loops
    dfPowerChannelNames = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                           'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power']
    dfCoherenceChannelNames = ['Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                               'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                               'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                               'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                               'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                               'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                               'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8']

    # Iterate through the dictionary of A files and populate the pandas dataframe with each file's powers
    # currently trying average of the powers
    # Also, label the row as an 'A' row
    print("Calculating Power for A groups and storing in the dataframe")
    channelNameIterator = 0
    for key in ADict:
        df.at[key[0], 'A or D'] = 1  # set the 'A or D' column value to 1 to represent it being an A column
        f, Pxx = signal.welch(ADict[key].ad)  # Use welch() to calculate the power array from the list of LFPs in ADict
        # use the average of power values because of an error with numpy that needs to be resolved
        df.at[key[0], dfPowerChannelNames[channelNameIterator]] = mean(Pxx)
        # This if/else check makes sure the channelNameIterator doesn't go past 7, since the list dfPowerChannelNames
        # is only 8 values long (0-indexed)
        if channelNameIterator < 7:
            channelNameIterator += 1
        else:
            channelNameIterator = 0

    # Iterate through the dictionary of D files and populate the pandas dataframe with each file's powers
    # currently trying average of the powers
    # Also, label the row as a 'D' row
    print("Calculating Power for D groups and storing in the dataframe")
    channelNameIterator = 0
    for key in DDict:
        df.at[key[0], 'A or D'] = 0  # set the 'A or D' column value to 0 to represent it being a D column
        f, Pxx = signal.welch(DDict[key].ad)  # Use welch() to calculate the power array from the list of LFPs in DDict
        # use the average of power values because of an error with numpy that needs to be resolved
        df.at[key[0], dfPowerChannelNames[channelNameIterator]] = mean(Pxx)
        # This if/else check makes sure the channelNameIterator doesn't go past 7, since the list dfPowerChannelNames
        # is only 8 values long (0-indexed)
        if channelNameIterator < 7:
            channelNameIterator += 1
        else:
            channelNameIterator = 0

    # Iterate through the dictionary of A files and populate the pandas dataframe with each file's coherences
    # currently trying average of the coherences
    # We need combinations between each chunk of 8 keys in the dictionary
    print("Calculating Coherence for A groups and storing in the dataframe")
    channelNameIterator = 0

    # divide the list of dictionary keys into chunks of 8 because each file has 8 channels
    # this enables us to calculate combinations between each file's channels
    divList = list(divide_chunks(list(ADict.keys()), 8))

    # each sublist in divList represents a file, hence the naming convention
    for file in divList:
        combList = list(combinations(file, 2))  # get all combinations of the channels in the file

        # iterate through the combinations
        for comb in combList:
            # calculate the coherence between two channels
            # comb is a nested tuple of channel names
            f, Cxy = signal.coherence(ADict[comb[0]].ad, ADict[comb[1]].ad)

            # put the mean of the coherence in the right dataframe cell
            df.at[comb[0][0], dfCoherenceChannelNames[channelNameIterator]] = mean(Cxy)

            # 28 coherence columns
            if channelNameIterator < 27:
                channelNameIterator += 1
            else:
                channelNameIterator = 0

    # Iterate through the dictionary of D files and populate the pandas dataframe with each file's coherences
    # currently trying average of the coherences
    # We need combinations between each chunk of 8 keys in the dictionary
    print("Calculating Coherence for D groups and storing in the dataframe")
    channelNameIterator = 0

    # divide the list of dictionary keys into chunks of 8 because each file has 8 channels
    # this enables us to calculate combinations between each file's channels
    divList = list(divide_chunks(list(DDict.keys()), 8))

    # each sublist in divList represents a file, hence the naming convention
    for file in divList:
        combList = list(combinations(file, 2))  # get all combinations of the channels in the file

        # iterate through the combinations
        for comb in combList:
            # calculate the coherence between two channels
            # comb is a nested tuple of channel names
            f, Cxy = signal.coherence(DDict[comb[0]].ad, DDict[comb[1]].ad)

            # put the mean of the coherence in the right dataframe cell
            df.at[comb[0][0], dfCoherenceChannelNames[channelNameIterator]] = mean(Cxy)

            # 28 coherence columns
            if channelNameIterator < 27:
                channelNameIterator += 1
            else:
                channelNameIterator = 0

    del ADict  # Release dictionary holding A group info
    gc.collect()
    del DDict  # Release dictionary holding D group info
    gc.collect()

    # print the dataframe in its entirety. Currently commented out to save space in the terminal
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        # print(df)

    # lists holding the target value we want to predict and the feature values we will use in the prediction
    target = ['A or D']
    features = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power',
                'Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8']

    # set y as the target column and x as the features columns
    y = df[target]
    x = df[features]

    # split the data into test and train sets
    # test_size=0.2 makes it so 80% of data is for training and 20% is for testing
    print("Splitting data")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

    print("Fitting Data")
    lambda_val = 0.1  # set lambda. review documentation for explanation on what this does
    lasso = Lasso(lambda_val)  # create lasso model
    lasso.fit(x_train, y_train)  # fit lasso model to our training data
    y_pred = lasso.predict(x_test)  # make a prediction
    print("Prediction -> {}".format(y_pred))
    mse_lasso = mean_squared_error(y_pred, y_test)  # calculate the mean squared error of the prediction
    print(("\nLasso MSE with Lambda={} is {}").format(lambda_val, mse_lasso))

    print("\ndone")
