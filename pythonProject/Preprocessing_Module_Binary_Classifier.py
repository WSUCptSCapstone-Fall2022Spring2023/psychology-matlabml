"""This file preprocesses data for a model which will predict whether a rodent is dependent (room air) or non-dependent (vapor) for each sex."""

import os

import numpy as np
import pandas
import pandas as pd
import scipy.signal
from scipy import signal
from itertools import combinations
from pypl2 import pl2_ad, pl2_info
from statistics import fmean
import openpyxl

class Config:
    """This class holds info for the configuration of our data cleaning"""

    def __init__(self):
        self.filterRange = [57, 63]
        self.dwnSample = 5
        self.artifactThreshold = 1.5
        self.onset = 0.0125  # 25 values prior
        self.offset = 0.5  # 1000 values after
        self.sex = 'M'  # set to 'F' to process data for female models
        self.excel_sheet = r'D:\CS 421\Binary_Predictor_Data\Sex_Differences_Alcohol_SA_Cohort_#3.xlsx'

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

    def __init__(self, sDir, cfg):
        self.sDir = sDir
        self.cfg = cfg
        self.fType = '.pl2'  # File type we are looking for
        self.dFrameDict = {}
        self.dataframe = pandas.DataFrame()

        # Lists of channel names to be used in the below loops
        self.power_channel_names = ['Channel 1 Power', 'Channel 2 Power', 'Channel 3 Power', 'Channel 4 Power',
                                    'Channel 5 Power', 'Channel 6 Power']
        self.coherence_channel_names = ['Coherence 1 & 2', 'Coherence 1 & 3', 'Coherence 1 & 4', 'Coherence 1 & 5',
                                        'Coherence 1 & 6', 'Coherence 2 & 3', 'Coherence 2 & 4', 'Coherence 2 & 5',
                                        'Coherence 2 & 6', 'Coherence 3 & 4', 'Coherence 3 & 5', 'Coherence 3 & 6',
                                        'Coherence 4 & 5', 'Coherence 4 & 6', 'Coherence 5 & 6']
        self.band_names = [' Delta', ' Theta', ' Alpha', ' Beta', ' Low Gamma', ' High Gamma']

        self.header = []
        if sDir != '':
            self.pl2_files = self.__getFileNames()
            self.preProcessData()

    def getDataSpecifications(self, cfg, file):
        """Method that gets additional details about our data that cannot be stored in CSV files.
        File is the csv or properly formatted Excel file we want to use.
        cfg is the config settings we are using.
        Outputs are stored in the CSV file that holds data processed from the .pl2 files."""
        data_array = []
        with open(file, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                if row['Sex'] == cfg.sex:  # if statement to get only animals of the sex we are testing on
                    data_array.append(row['Condition'])
        data_object = {"condition": data_array}
        drinking_amounts = pd.DataFrame(data_object)
        return drinking_amounts

    def preProcessData(self):
        """Main method of this class. When called, it will populate the pandas dataframe stored in self. with all power
        and coherence values from the data files in the directory pointed at by this class."""
        print("Getting data for Lasso")
        os.chdir(self.sDir)  # change the current working directory to where our data is stored.

        # set the header and rows for the dataframe
        self.__buildHeader()

        # open the Excel sheet with additional info
        wb = openpyxl.load_workbook(self.cfg.excel_sheet)
        ws = wb.active

        # iterate through all files and populate the pandas dataframe with power and coherence values
        for row in ws.iter_rows(values_only=True):
            if row[2] == self.cfg.sex:
                for pl2_filename in self.pl2_files:
                    if pl2_filename == row[0]:
                        print("Processing file {} for Rat # {}".format((pl2_filename + '.pl2'), row[1]))
                        self.__pl2ToDictionaryRow((pl2_filename + '.pl2'))

        # Turn Dictionary into Dataframe
        self.dataframe = pd.DataFrame.from_dict(self.dFrameDict, orient='index', columns=self.header)
        self.dataframe.head()



    def __buildHeader(self):
        """This function creates the rows and columns for our dataframe. Since the header is 216 columns, it's much easier
        to create it programmatically"""

        # order is all powers + bandNames, then all coherences + band names
        header = []

        # power channels + bands
        for i in range(0, 6):
            for j in range(0, 6):
                header.append(self.power_channel_names[i] + self.band_names[j])

        # coherence channels + bands
        for i in range(0, 15):
            for j in range(0, 6):
                header.append(self.coherence_channel_names[i] + self.band_names[j])

        header.append('Condition')

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

    def __pl2ToDictionaryRow(self, filename):
        """Ths method accepts a pl2 file and converts its information into a row of data corresponding to the header of
        the pandas dataframe we're writing to."""

        # count the number of active channels and store their numbers
        file_resource = pl2_info(filename)
        channel_count = 0
        channel_number = 0
        channel_numbers = []

        for channel in file_resource.ad:
            if channel.n > 0:  # if a channel has count > 0 then it has data
                channel_count += 1
                channel_numbers.append(channel_number)
            channel_number += 1  # update the current channel's number

        print("Detected {} active channels".format(channel_count))

        # convert data in channels from volts to raw a/d
        ad_array = []
        for channel in channel_numbers:
            print("Converting volts to a/d in channel {}".format(channel+1))
            ad_info = pl2_ad(filename, channel)
            ad = self.voltsToRawAD(ad_info.ad)
            ad_array.append(ad)

        # perform data cleaning
        cleaned_ad_array = []
        iterator = 1
        for ad in ad_array:
            print("Cleaning Channel {}".format(iterator))

            # 1. 60 Hertz Filter
            print("Applying 60hz Filter")
            ad = self.__60HertzFilter(ad, ad_info.adfrequency)

            # 2. Down-sampling
            print("Applying Down-Sampling")
            ad = self.__downSampling(ad, self.cfg.dwnSample, ad_info.adfrequency)

            # 3. Threshold filter
            #print("Applying Threshold Filter")
            #ad = self.__noiseArtifactsFilter(ad, self.cfg.artifactThreshold, self.cfg.onset, self.cfg.offset, ad_info.adfrequency)

            cleaned_ad_array.append(ad)
            iterator += 1

        del ad_array  # release memory of uncleaned data

        # calculate power values for data
        power_array = []
        iterator = 0
        for ad in cleaned_ad_array:
            print("Processing Power for Channel {}".format(self.power_channel_names[iterator]))
            f, Pxx = self.__calculateChannelPower(ad, ad_info.adfrequency)
            power_array.append((f, Pxx))
            iterator += 1


        # calculate coherence values for data
        iterator = 0
        combo_list = list(combinations(channel_numbers, 2))  # get combinations of each 0-indexed channel number
        coherence_array = []
        for combo in combo_list:
            print("Processing Coherence for Channel Pair {}".format(self.coherence_channel_names[iterator]))
            ad1 = cleaned_ad_array[combo[0]]
            ad2 = cleaned_ad_array[combo[1]]
            f, Cxy = self.__calculateChannelCoherence(ad1, ad2, ad_info.adfrequency)
            coherence_array.append((f, Cxy))
            iterator += 1

        # Split power signals into power bands and combine into one list
        split_signal_array = []
        for tup in power_array:
            split_signal_array.extend(self.__splitSignal(tup[0], tup[1]))

        # Split coherence signals into power bands and combine into one list
        for tup in coherence_array:
            split_signal_array.extend(self.__splitSignal(tup[0], tup[1]))

        
        # Add info to dictionary
        self.dFrameDict[filename] = split_signal_array



    def __getFileNames(self):
        """Method for getting a list of file names from the directory pointed at by this class"""
        print("Getting file names")
        files = []
        # open the Excel sheet with additional info
        wb = openpyxl.load_workbook(self.cfg.excel_sheet)
        ws = wb.active

        # For each file in a list of files in the directory
        for row in ws.iter_rows(values_only=True):
            files.append(row[0])  # append it to our list of file names
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

    def __60HertzFilter(self, sig, freq):
        """Cleans the data for frequencies of 60Hz using a second order Chebyshev type 1 notch filter. This is because the machine used to collect data naturally produces
        this signal, so it cannot be used. x is array to be cleaned, freq is sampling frequency."""

        b, a = scipy.signal.iirnotch(60, 30, freq)
        sig = scipy.signal.filtfilt(b, a, sig)
        return sig


    def __noiseArtifactsFilter(self, sig, artifactThreshold, onset, offset, f):
        """Cleans the data for noise artifacts created by interference by sources like the rat bashing its head against the enclosure wall.
        Filter is performed by scanning the signal array for values greater than the threshold, then removing all values a fraction of a second before and after that value."""

        ranges_to_remove = []  # make list of signals to remove after searching
        onset = round(onset * f)
        offset = round(offset * f)

        # iterate through array
        end_of_array = len(sig)-1
        for i in range(len(sig)):
            if sig[i] >= artifactThreshold:  # if a value is greater than the threshold
                ranges_to_remove.extend(range(i-onset, i+offset+1))

        ranges_to_remove = list(filter(lambda x: x >= 0, ranges_to_remove))
        ranges_to_remove = list(filter(lambda x: x <= end_of_array, ranges_to_remove))

        ranges_to_remove = list(set(ranges_to_remove))  # remove potential duplicates

        for r in sorted(ranges_to_remove, reverse=True):
            del sig[r]

        clean_sig = sig

        return clean_sig

    def __downSampling(self, sig, dsf, adfreq):
        """Downsamples the data for faster processing. sig is the signal to be downsampled. dsf needs to be a divisor of adfreq, which is the sampling frequency."""

        if adfreq % dsf != 0:
            raise Exception("Downsampling Frequency is not a divisor of Sampling Frequency")

        sig = scipy.signal.decimate(sig, dsf)

        return sig





if __name__ == "__main__":
    cfg = Config()
    accessObj = AccessData(r'D:\CS 421\Binary_Predictor_Data', cfg)
    #dataframe = LoadData('test.csv')
    #target = accessObj.getDataSpecifications(cfg)
    #dataframe.df[''] = target['']
    #dataframe.printDataFrame()

