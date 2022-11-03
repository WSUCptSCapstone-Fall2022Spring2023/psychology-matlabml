# This is another practice file where I will prove a concept for a lasso predictor First, import all data from sample
# files into the program and sort them into two arrays by A and D types Then, for each file, calculate the power for
# each channel in that file and store in a dictionary of arrays Do the same for coherence for each file,
# using a dictionary of dictionaries of arrays? to store coherence between each channel The power and coherence
# values are arrays. Hopefully this still works for the sklearn lasso function Place all of this data into a pandas
# dataframe in the following format (arrays are replaced with random chars for convenience of the example):
#
# |   File Name   |   Channel 1 Power    |   Channel 2 Power   | ... |   Channel 8 Power   |   Coherence Between 1 and 2   |   Coherence Between 1 and 3   | ... | Coherence Between 7 and 8   |   A or D   |
#     A170...                [xyz]                [zyx]                        [xyz]                       [yxz]                   [zyw]                                     [yzs]                    'A'
#
#
# Use 80% of the data as training data, keeping 20% as testing Fit the lasso model by using the channel powers and
# coherences as features, and the 'A or D' column as the target We can also use a series of lambda values to test
# multiple times to find the best fit Use all of the data to prevent overfitting. We can use os.chdir() to find the
# directory where the data is stored and run on all of it at once

# Additionally, this file does not represent our final software product. As stated above, it is a proof of concept
# for Dr. Henrick's initial assignment of creating an A/D binary classifier

import os
import sys
import warnings
import ctypes
from scipy import signal
from sklearn.linear_model import Lasso
from matplotlib import pyplot as plt
from itertools import combinations
import pandas as pd
from pypl2 import pl2_info, pl2_ad, pl2_spikes, pl2_events, pl2_info

# divide a list l into chunks of length n
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == "__main__":

    # add all data file names in the target directory to a list
    sDir = r'C:\Users\aidan.nunn\Documents\Homework\CS 421\SampleSampleData'
    fType = '.pl2'
    os.chdir(
        sDir)  # set the directory we are looking at to where all of the data is stored. Since this is a proof of concept, this will be different for each machine this program runs on.
    files = []
    print("Finding file names")
    for f in os.listdir(sDir):
        if f.endswith(fType):
            files.append(f)

    # Create a pandas dataframe for use later
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
    # Get generic file data from each file into a named resource tuple and put each resource object into an array
    resourceArray = []
    print("Getting generic data")
    for filename in files:
        resource = pl2_info(filename)
        resourceArray.append(resource)

    # Get AD file data from each file and put each resource object into a dictionary
    ADict = {}
    DDict = {}
    channelsList = []
    print("Getting AD data")
    for filename, resource in zip(files, resourceArray):
        channelNameIterator = 0  # reset iterator between files
        for channel in resource.ad:
            if channel.n > 0:
                ad = pl2_ad(filename, channelNameIterator)  # add channel variable
                if filename.startswith('A'):
                    ADict[(filename, channelNameIterator)] = ad  # keys are tuples named as (filename, channel number)
                    channelsList.append(channelNameIterator)
                if filename.startswith('D'):
                    DDict[(filename, channelNameIterator)] = ad  # keys are tuples named as (filename, channel number)
                    channelsList.append(channelNameIterator)
            channelNameIterator += 1

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
    # Also, label the row as an 'A' row
    print("Calculating Power for A groups and storing in the dataframe")
    channelNameIterator = 0
    for key in ADict:
        df.at[key[0], 'A or D'] = 'A'
        f, Pxx = signal.welch(ADict[key].ad)
        df.at[key[0], dfPowerChannelNames[channelNameIterator]] = Pxx
        if channelNameIterator < 7:
            channelNameIterator += 1
        else:
            channelNameIterator = 0

    # Iterate through the dictionary of D files and populate the pandas dataframe with each file's powers
    # Also, label the row as a 'D' row
    print("Calculating Power for D groups and storing in the dataframe")
    channelNameIterator = 0
    for key in DDict:
        df.at[key[0], 'A or D'] = 'D'
        f, Pxx = signal.welch(DDict[key].ad)
        df.at[key[0], dfPowerChannelNames[channelNameIterator]] = Pxx
        if channelNameIterator < 7:
            channelNameIterator += 1
        else:
            channelNameIterator = 0

    # Iterate through the dictionary of A files and populate the pandas dataframe with each file's coherences
    # We need combinations between each chunk of 8 keys in the dictionary
    print("Calculating Coherence for A groups and storing in the dataframe")
    channelNameIterator = 0
    divList = list(divide_chunks(list(ADict.keys()), 8))
    for file in divList:
        combList = list(combinations(file, 2))
        for comb in combList:
            f, Cxy = signal.coherence(ADict[comb[0]].ad, ADict[comb[1]].ad)
            df.at[comb[0][0], dfCoherenceChannelNames[channelNameIterator]] = Pxx
            if channelNameIterator < 27:
                channelNameIterator += 1
            else:
                channelNameIterator = 0

    # Iterate through the dictionary of D files and populate the pandas dataframe with each file's coherences
    # We need combinations between each chunk of 8 keys in the dictionary
    print("Calculating Coherence for D groups and storing in the dataframe")
    channelNameIterator = 0
    divList = list(divide_chunks(list(DDict.keys()), 8))
    for file in divList:
        combList = list(combinations(file, 2))
        for comb in combList:
            f, Cxy = signal.coherence(DDict[comb[0]].ad, DDict[comb[1]].ad)
            df.at[comb[0][0], dfCoherenceChannelNames[channelNameIterator]] = Pxx
            if channelNameIterator < 27:
                channelNameIterator += 1
            else:
                channelNameIterator = 0


    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
    print("\ndone")


