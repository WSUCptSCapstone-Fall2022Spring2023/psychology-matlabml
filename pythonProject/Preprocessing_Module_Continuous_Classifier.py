"""This file contains the class which will preprocess inputted data files. It will have one class: AccessData. This
class will upload data files to the program and be able to process those data files into data structures that can be
used by our logic modules. """

import os

import numpy as np
import pandas as pd
import scipy.signal
from scipy import signal
from itertools import combinations
from pypl2 import pl2_ad, pl2_info
from loadingBar import printProgressBar
from matplotlib import pyplot as plt
from statistics import fmean
import csv

class Config:
    """This class holds info for the configuration of our data cleaning"""

    def __init__(self):
        self.filterRange = [57, 63]
        self.dwnSample = 5
        self.artifactThreshold = 1.5
        self.onset = 0.0125  # 25 values prior
        self.offset = 0.5  # 1000 values after


class LoadData:
    """Class used to load a CSV file of data into a pandas dataframe for use in the logic modules"""

    def __init__(self, file):
        self.df = pd.read_csv(file)

    def __setDataframeCell(self, index, column, value):
        """Method for setting the cell of a dataframe. This function is technically trivial, but makes the code in
        this class more readable. """
        self.df.at[index, column] = value

    def printDataFrame(self):
        """Method for printing the dataframe to a terminal window."""
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.df)


class AccessData:
    """Class used to access and process data from a directory of data files into power and coherence data that can be used
    in the program. The method getDataForLasso() can be called to populate data into a pandas dataframe located in this class.
    The class object will hold this dataframe."""

    def __init__(self, sDir):
        self.sDir = sDir
        self.fType = '.pl2'  # File type we are looking for
        self.files = self.__getFileNames()

        # Lists of channel names to be used in the below loops
        self.power_channel_names = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                                    'Channel 5 Power', 'Channel 6 Power', 'Channel 7 Power', 'Channel 8 Power']
        self.coherence_channel_names = ['Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                                        'Coherence 1 & 6', 'Coherence 1 & 7', 'Coherence 1 & 8', 'Coherence 2 & 3',
                                        'Coherence 2 & 4', 'Coherence 2 & 5', 'Coherence 2 & 6', 'Coherence 2 & 7',
                                        'Coherence 2 & 8', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                                        'Coherence 3 & 7', 'Coherence 3 & 8', 'Coherence 4 & 5', 'Coherence 4 & 6',
                                        'Coherence 4 & 7', 'Coherence 4 & 8', 'Coherence 5 & 6', 'Coherence 5 & 7',
                                        'Coherence 5 & 8', 'Coherence 6 & 7', 'Coherence 6 & 8', 'Coherence 7 & 8']
        self.band_names = [' Delta', ' Theta', ' Alpha', ' Beta', ' Low Gamma', ' High Gamma']
        self.header = []

    def preProcessData(self, target_file):
        """Main method of this class. When called, it will populate a csv file with all power
        and coherence values from the data files in the directory pointed at by this class. """
        print("Getting data for Lasso")
        os.chdir(self.sDir)  # change the current working directory to where our data is stored.

        # open target csv file for write
        f = open(target_file, 'w', newline='')
        writer = csv.writer(f)
        self.__createHeaderForBinaryClassifierCSV()
        writer.writerow(self.header)
        # iterate through all files and populate the pandas dataframe with power values
        for filename in self.files:
            print("Processing file {}".format(filename))
            self.__pl2ToCSV(filename, writer)

        f.close()

    def __createHeaderForBinaryClassifierCSV(self):
        """This function creates the header for our csv output file. Since the header is 216 columns, it's much easier
        to create it programmatically"""

        # order is all powers + bandNames, then all coherences + band names
        header = []

        # power channels + bands
        for i in range(0, 8):
            for j in range(0, 6):
                header.append(self.power_channel_names[i] + self.band_names[j])

        # coherence channels + bands
        for i in range(0, 28):
            for j in range(0, 6):
                header.append(self.coherence_channel_names[i] + self.band_names[j])

        header.append('g/kg')
        self.header = header

    def __splitSignal(self, f, signal):
        """splits an array of signal (power or coherence) values into an array of 6 arrays based on the 6 signal labels"""
        delta = []       # range 1-4
        theta = []       # range 5-10
        alpha = []       # range 11-14
        beta = []        # range 15-30
        low_gamma = []   # range 45-65
        high_gamma = []  # range 70-90

        for i in range(len(f)):
            if 1 <= f[i] <= 4:
                delta.append(signal[i])
            if 5 <= f[i] <= 10:
                theta.append(signal[i])
            if 11 <= f[i] <= 14:
                alpha.append(signal[i])
            if 15 <= f[i] <= 30:
                beta.append(signal[i])
            if 45 <= f[i] <= 65:
                low_gamma.append(signal[i])
            if 70 <= f[i] <= 90:
                high_gamma.append(signal[i])

        if len(delta) == 0:
            delta.append(0)
        if len(theta) == 0:
            theta.append(0)
        if len(alpha) == 0:
            alpha.append(0)
        if len(beta) == 0:
            beta.append(0)
        if len(low_gamma) == 0:
            low_gamma.append(0)
        if len(high_gamma) == 0:
            high_gamma.append(0)

        l = []
        l.append(fmean(delta))
        l.append(fmean(theta))
        l.append(fmean(alpha))
        l.append(fmean(beta))
        l.append(fmean(low_gamma))
        l.append(fmean(high_gamma))

        return l


    def __pl2ToCSV(self, filename, writer):
        # TODO needs refactoring into multiple functions. use voltsToRawAD in first loop only, not in second loop to save processing time. three loops: one for data access and cleaning, one for power, and one for coherence?
        """Ths method accepts a pl2 file and converts its information into a row of data corresponding to the header of
        the CSV file we're writing to. It prints the row to the file."""
        channels_list = []  # List to hold 0-indexed channel numbers instead of what is listed in the resource tuples
        channel_number_iterator = 0  # reset iterator between files
        one_thru_eight_iterator = 1  # iterator to count thru all 8 channels of a file
        file_resource = pl2_info(filename)

        row = []
        for channel in file_resource.ad:  # iterate over each channel in a file (8 relevant channels per file)
            if channel.n > 0:  # if a channel has count > 0 then it has data
                print("Processing power for channel {}".format(one_thru_eight_iterator))
                ad_info = pl2_ad(filename, channel_number_iterator)  # use pl2_ad to get a/d info from a channel

                # convert volts in ad_info.ad to raw A/D values
                #ad = self.voltsToRawAD(ad_info.ad)

                # perform data cleaning here

                # calculate power
                f, Pxx = self.__calculateChannelPower(ad_info.ad, 200)#ad_info.adfrequency)  # Use welch() to calculate the power array from the list of LFPs in ad_info

                # split power into 6 frequency bands
                power_bands = self.__splitSignal(f, Pxx)

                # add new values to row to be written to the csv later
                for item in power_bands:
                    row.append(item)
                one_thru_eight_iterator += 1
                channels_list.append(channel_number_iterator)  # add the channel number to a list for use later
            channel_number_iterator += 1  # iterate to the next 0-indexed channel number

        # calculate coherence
        comboList = list(combinations(channels_list, 2))  # get combinations of each 0-indexed channel number

        # iterate through all channel combos and get all coherence values split by frequency band
        for channelCombo, column in zip(comboList, self.coherence_channel_names):
            print("Processing coherence for channel pair {}".format(column))
            ad_info1 = pl2_ad(filename, channelCombo[0])
            ad_info2 = pl2_ad(filename, channelCombo[1])

            # convert volts in ad_info.ad to raw A/D values
            #ad1 = self.voltsToRawAD(ad_info1.ad)

            # convert volts in ad_info.ad to raw A/D values
            #ad2 = self.voltsToRawAD(ad_info2.ad)

            f, Cxy = self.__calculateChannelCoherence(ad_info1.ad, ad_info2.ad, 200)#ad_info.adfrequency)
            power_bands = self.__splitSignal(f, Cxy)
            # add new values to row to be written to the csv later
            for item in power_bands:
                row.append(item)


        writer.writerow(row)

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
        """Method for calculating the power values of a channel's LFP data. This function is trivial, but useful
        for making the code more readable. """
        f, Pxx = signal.welch(ad, fs=frequency)
        return f, Pxx

    def __calculateChannelCoherence(self, ad1, ad2, frequency):
        """Method for calculating the coherence values of a channel's LFP data. This function is trivial,
        but useful for making the code more readable. """
        f, Cxy = signal.coherence(ad1, ad2, fs=frequency)
        return f, Cxy

    def voltsToRawAD(self, arr):
        arr = list(map(lambda x: x / (1.9488 * pow(10, -7)), arr))
        arr = list(map(lambda x: round(x), arr))
        return arr

    def __60HertzFilter(self, x, freq):
        """Cleans the data for frequencies of 60Hz using a second order Chebyshev type 1 notch filter. This is because the machine used to collect data naturally produces
        this signal, so it cannot be used. x is array to be cleaned, freq is sampling frequency."""


    def __noiseArtifactsFilter(self, sig, artifactThreshold, onset, offset):
        """Cleans the data for noise artifacts created by interference by sources like the rat bashing its head against the enclosure wall.
        Filter is performed by scanning the signal array for values greater than the threshold, then removing all values a fraction of a second before and after that value."""

        rangesToRemove = []  # make list of ranges to remove after searching

        # iterate through array
        endOfArray = len(sig)-1
        for i in range(len(sig)):
            if sig[i] >= artifactThreshold:  # if a value is greater than the threshold
                if i-onset < 0:  # check for out-of-bounds-ing
                    rangesToRemove.append([0, i + offset])  # add range to be removed to array
                elif i+offset > endOfArray:
                    rangesToRemove.append([i-onset, endOfArray])  # add range to be removed to array
                elif i-onset < 0 and i+offset > endOfArray:
                    rangesToRemove.append([0, endOfArray])
                else:
                    rangesToRemove.append([i-onset, i+offset])  # add range to be removed to array

        for r in rangesToRemove:
            for i in range(r[0], r[1] + 1):
                sig[i] = 'erase'

        cleanSig = []
        for val in sig:
            if val != 'erase':
                cleanSig.append(val)



        return cleanSig

    def __downSampling(self, sig, dsf, adfreq):
        """Downsamples the data for faster processing. sig is the signal to be downsampled. dsf needs to be a divisor of adfreq, which is the sampling frequency."""

        if adfreq % dsf != 0:
            raise Exception("Downsampling Frequency is not a divisor of Sampling Frequency")

        sig = scipy.signal.decimate(sig, dsf)

        return sig





if __name__ == "__main__":
    accessObj = AccessData(r'C:\Users\aidan.nunn\Documents\Homework\CS 421\SampleSampleData')
    dataframe = LoadData('test.csv')
    dataframe.printDataFrame()