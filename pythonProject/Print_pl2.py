# This file is a test project meant to be used to play with the pypl2api. It will use the API to print data from
# a sample .pl2 file.
# The basic idea is to upload a .pl2 file using the window.
# Then, the program iterates through all the available channels to find which ones have data in them (it checks the count variable from pl2_info())
# Once pl2_ad() gets the data in the form of the named tuple, those values can be printed!


import os
import sys
import warnings
import ctypes
from pypl2 import pl2_info, pl2_ad, pl2_spikes, pl2_events, pl2_info


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
    # this loos grabs all channels with counts > 0 and puts them into the list l
    # the channels are 0-indexed in the file, but numbered in repeating sets of 0-32 in the tuple. channelList appends the actual channel each time a good one is found
    for item in resource.ad:
        if item.n != 0:
            l.append(item)
            channelList.append(iterator)
        iterator += 1
    print(l)


    for i in channelList:
        ad = pl2_ad(filename, i)

        if ad.n == 0:
            pass
        else:
            print("Here's what I found")
            print("{}".format(ad.adfrequency))
            print("{}".format(ad.n))
            print("{}".format(ad.timestamps))
            print("{}".format(ad.fragmentcounts))
            for i in range(1, 10):  #len(ad.ad)): there are hundreds of thousands of data points in this tuple, so viewing the first 100 is more feasible for this test
                print("ad number {}: {}".format(i, ad.ad[i]))



