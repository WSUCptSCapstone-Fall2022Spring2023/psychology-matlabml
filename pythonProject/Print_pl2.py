# This file is a test project meant to be used to play with the pypl2api. It will use the API to print data from
# a sample .pl2 file.
# The basic idea is to upload a .pl2 file using the window.
# Then, the program iterates through all the available channels to find which ones have data in them (it checks the count variable from pl2_info())
# Once pl2_ad() gets the data in the form of the named tuple, those values can be printed!

# From my understanding, each a/d number is the LFP at the timeframe when it was recorded. These are recorded over the course of a little over an hour
# We calculate power at each site, and coherence between sites
# This means power for each channel (each channel is recorded at a different site) and coherence between channels

import os
import sys
import warnings
import ctypes
from scipy.signal import welch
from matplotlib import pyplot as plt
from pypl2 import pl2_info, pl2_ad, pl2_spikes, pl2_events, pl2_info


#function that opens a file explorer window to select a file to read
def choose_file():
    try:
        import tkinter
    except ImportError:
        print("Tkinter not installed.")
        exit()

    from tkinter import filedialog

    # Suppress the Tkinter root window
    tkroot = tkinter.Tk()
    tkroot.withdraw()

    return str(tkinter.filedialog.askopenfilename())


if __name__ == "__main__":

    # If no file is passed at the command line, or if the file
    # passed can not be found, open a file chooser window.
    if len(sys.argv) < 2:
        filename = os.path.abspath(choose_file())
    else:
        filename = os.path.abspath(sys.argv[1])
        if not os.path.isfile(filename):
            filename = choose_file()


    ####################
    # pl2_ad() example #
    ####################

    #Get file info and print it out
    # Printed as a named tuple with names: 'adfrequency, n, timestamps, fragmentcounts, ad'
    # by using the file 'A171_post05_2020-4-8_pl2_spl_ead_plx.pl2' in Sample Data with the channel 80, we can find ad info for the file!
    # trying to use a channel without counts results in a numpy PEP 3118 error.
    # currently channel counts can be observed by using PlexUtil, but I plan on figuring out a way to scan a file for all FP channels with counts automatically

    #get FP channels with info in them from the file
    #TODO clean up this code
    resource = pl2_info(filename)
    l = []
    channelList = []
    iterator = 0
    # this loop grabs all channels with counts > 0 and puts them into the list l
    # the channels are 0-indexed in the file, but numbered in repeating sets of 0-32 in the tuple. channelList appends the actual channel each time a good one is found
    for item in resource.ad:
        if item.n > 0:
            l.append(item)
            channelList.append(iterator)
        iterator += 1
    print(l)

    # usually 8 channels, representing analyses of different parts of the brain
    adList = []
    temp = []
    index = 0
    for i in channelList:
        ad = pl2_ad(filename, i)

        print("Here's what I found in Channel {}".format(i-63))
        print("Frequency: {}".format(ad.adfrequency)) # this number is how many a/d value are recorded per second (frequency of recordings). # There are about 2000 a/d numbers recorded a second for FP channels
        print("Number of Data Points: {}".format(ad.n)) # total number of data points in the channel
        print("List of Timestamps: {}".format(ad.timestamps))
        #print("Number of Fragments: {}".format(ad.fragmentcounts))
        for j in range(256):# len(ad.ad)): #there are millions of data points in this tuple, so viewing the first 100 or so is more feasible for this test
            temp.append(ad.ad[j])
            print("a/d Number {}: {}".format(j, ad.ad[j]))
        adList.append(temp)
        temp = []
        print('\n')

        # try using scipy.signal.welch as a replacement for MATLAB's pwelch function
        # prints two arrays, one of frequencies and one of PSDs. From my understanding these will be used to create a graph.
        f, Pxx = welch(adList[index])
        print("Array of sample frequencies: {}".format(f))
        print("Power spectral density or power spectrum of input array: {}".format(Pxx))
        plt.plot(f, Pxx)# plot a graph of frequencies on the x-axis and PSDs on the y-axis
        plt.xlabel("Frequency")
        plt.ylabel("PSD")
        plt.show()# open window displaying graph
        index += 1


