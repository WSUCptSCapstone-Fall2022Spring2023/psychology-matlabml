
"""This file contains the class which will preprocess inputted data files. It will have one class: AccessData. This
class will upload data files to the program and be able to process those data files into data structures that can be
used by our logic modules. """

import os

import numpy as np
import pandas as pd
from scipy import signal
from itertools import combinations
from pypl2 import pl2_ad,  pl2_info
from loadingBar import printProgressBar
from matplotlib import pyplot as plt
from statistics import fmean

class AccessData:
    """Class used to access and process data from a directory of data files into power and coherence data that can be used
    in the program. The method getDataForLasso() can be called to populate data into a pandas dataframe located in this class.
    The class object will hold this dataframe."""
    def __init__(self, sDir = r'C:\Users\aidan.nunn\Documents\Homework\CS 421\SampleSampleData'):
        self.sDir = sDir
        self.fType = '.pl2'  # File type we are looking for
        self.files = self.__getFileNames()

        # Create a pandas dataframe for use later
        # Rows are indexed by file name, and columns are labeled with each data point we want to store.
        self.df = pd.DataFrame(index=self.files,
                               columns=['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                                        'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power',

                                        'Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                                        'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                                        'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                                        'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                                        'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                                        'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                                        'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8',

                                        'A or D'])

        # Lists of channel names to be used in the below loops
        self.dfPowerChannelNames = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                                    'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power']
        self.dfCoherenceChannelNames = ['Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                                        'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                                        'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                                        'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                                        'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                                        'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                                        'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8']
        self.getDataForLasso()

    def getDataForLasso(self):
        """Main method of this class. When called, it will populate a pandas dataframe in this class with all power
        and coherence values from the data files in the directory pointed at by this class. """
        print("Getting data for Lasso")
        os.chdir(self.sDir)  # change the current working directory to where our data is stored.

        l = len(self.files)
        printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)  # print progress bar to terminal
        i = 0

        #iterate through all files and populate the pandas dataframe with power values
        for filename in self.files:
            channels_list = []  # List to hold 0-indexed channel numbers instead of what is listed in the resource tuples
            channel_number_iterator = 0  # reset iterator between files
            one_thru_eight_iterator = 0  # iterator to count thru all 8 channels in a file
            file_resource = pl2_info(filename)  # get generic info from a file so that we can see the counts of data

            for channel in file_resource.ad:  # iterate over each channel in a file (8 relevant channels per file)
                if channel.n > 0:  # if a channel has count > 0 then it has data
                    ad_info = pl2_ad(filename, channel_number_iterator)  # use pl2_ad to get a/d info from a channel

                    if filename.startswith('A'):  # the filename starts with 'A' if it's in the A group
                        self.__setDataframeCell(filename, 'A or D', 1)  # set the 'A or D' column value to 1 to represent it being an A column
                    if filename.startswith('D'):  # the filename starts with 'D' if it's in the D group
                        self.__setDataframeCell(filename, 'A or D', 0)  # set the 'A or D' column value to 0 to represent it being a D column

                    Pxx = self.__calculateChannelPower(ad_info.ad, ad_info.adfrequency)  # Use welch() to calculate the power array from the list of LFPs in ad_info
                    self.__setDataframeCell(filename, self.dfPowerChannelNames[one_thru_eight_iterator], fmean(Pxx))  # put the power values array in the dataframe
                    one_thru_eight_iterator += 1
                    channels_list.append(channel_number_iterator)  # add the channel number to a list for use later
                channel_number_iterator += 1  # iterate to the next 0-indexed channel number

            comboList = list(combinations(channels_list, 2))  # get combinations of each 0-indexed channel number
            # iterate through all channel combos and populate the pandas dataframe with coherence values
            for channelCombo, column in zip(comboList, self.dfCoherenceChannelNames):
                ad_info1 = pl2_ad(filename, channelCombo[0])
                ad_info2 = pl2_ad(filename, channelCombo[1])
                if ad_info1.adfrequency != ad_info2.adfrequency:
                    print("Coherence frequencies do not match")
                    exit(1)
                Cxy = self.__calculateChannelCoherence(ad_info1.ad, ad_info2.ad, ad_info2.adfrequency)
                self.__setDataframeCell(filename, column, fmean(Cxy))

            printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)  # update progress bar
            i += 1

    def __getFileNames(self):
        """Method for getting a list of file names from the directory pointed at by this class"""
        print("Getting file names")
        files = []
        # For each file in a list of files in the directory
        for f in os.listdir(self.sDir):
            if f.endswith(self.fType):  # if the file ends with our target file type
                files.append(f)  # append it to our list of file names
        return files

    def __calculateChannelPower(self, ad, frequency):
        """Method for calculating the power values of a channel's LFP data. This function is trivial, but necessary
        for making the code more readable. """
        f, Pxx = signal.welch(ad, fs=frequency)
        return Pxx

    def __calculateChannelCoherence(self, ad1, ad2, frequency):
        """Method for calculating the coherence values of a channel's LFP data. This function is trivial,
        but necessary for making the code more readable. """
        f, Cxy = signal.coherence(ad1, ad2, fs=frequency)
        return Cxy

    def __setDataframeCell(self, index, column, value):
        """Method for setting the cell of a dataframe. This function is technically trivial, but makes the code in
        this class more readable. """
        self.df.at[index, column] = value

    def printDataFrame(self):
        """Method for printing the dataframe to a terminal window."""
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.df)


if __name__ == "__main__":
    accessObj = AccessData()
    accessObj.printDataFrame()