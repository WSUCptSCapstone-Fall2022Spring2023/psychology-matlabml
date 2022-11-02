# This is another practice file where I will prove a concept for a lasso predictor
# First, import all data from sample files into the program and sort them by A and D types
# Then, for each file, calculate the power for each channel in that file and store in a dictionary of arrays
# Do the same for coherence for each file, using a dictionary of dictionaries of arrays? to store coherence between each channel
# The power and coherence values are arrays. Hopefully this still works for the sklearn lasso function
# Place all of this data into a pandas dataframe in the following format (arrays are replaced with random chars for convenience of the example):
#
# |   File Name   |   Channel 1 Power    |   Channel 2 Power   | ... |   Channel 8 Power   |   Coherence Between 1 and 2   |   Coherence Between 1 and 3   | ... | Coherence Between 7 and 8   |   A or D   |
#     A170...                [xyz]                [zyx]                        [xyz]                       [yxz]                   [zyw]                                     [yzs]                    'A'
#
#
# Use 80% of the data as training data, keeping 20% as testing
# Fit the lasso model by using the channel powers and coherences as features, and the 'A or D' column as the target
# We can also use a series of lambda values to test multiple times to find the best fit
# Use all of the data to prevent overfitting. We can use os.chdir() to find the directory where the data is stored and run on all of it at once

# Additionally, this file does not represent our final software product. As stated above, it is a proof of concept for Dr. Henrick's initial assignment of creating an A/D binary classifier

import os
import sys
import warnings
import ctypes
from scipy import signal
from sklearn.linear_model import Lasso
from matplotlib import pyplot as plt
import pandas as pd
from pypl2 import pl2_info, pl2_ad, pl2_spikes, pl2_events, pl2_info





if __name__ == "__main__":

    # add all data file names in the target directory to a list
    sdir = r'C:\Users\aidan.nunn\Documents\Homework\CS 421\Sample Data'
    fType = '.pl2'
    os.chdir(sdir)# set the directory we are looking at to where all of the data is stored. Since this is a proof of concept, this will be different for each machine this program runs on.
    files = []
    print("Finding file names")
    for f in os.listdir(sdir):
        if f.endswith(fType):
            files.append(f)

    # Get generic file data from each file into a named resource tuple and put each resource object into an array
    resourceArray = []
    print("Getting generic data")
    for filename in files:
        resource = pl2_info(filename)
        resourceArray.append(resource)

    # Get AD file data from each file and put each resource object into an array
    ADArray = []
    print("Getting AD data")
    for filename, resource in zip(files, resourceArray):
        iterator = 0
        for channel in resource.ad:
            if channel.n > 0:
                print(channel)
                ad = pl2_ad(filename, iterator) # add channel variable
                ADArray.append(ad)
            iterator += 1


    print("done")





