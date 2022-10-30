import time
import os


# Generic script to batch process files
# Inactivate/activate function cells with commenting

#Inputs (pick one from fType and files, set the otehr to []):
# fun = function group to run; options = 'scb' for spectcompbase.py, 'tab' for tabulateData.py, 'sleep' for sleepDetect.py, 'pre' for preProcess.m
# fType = wildcard(s) to search for in order to populate list of files to be processed. format = string array. N.B.: not case sensitive, but use best practice to avoid problems
# files = array of filenames to use
# sdir = source directory of files; format = string. N.B.: if more than one source directory is to be used, rerun fileCycle.py for each

#Outputs: Depend of function group called (see those functions for more detail)

# Example:
# fileCycle('scb',{'Base','FoodDep24'},[],'C:\Users\Aidan\Documents\Capstone\data'); Runs all files in C:\...\data that have either 'Base' or 'FoodDep24' in their name through spectcompbase.m

def fileCycle(fun, fType, files, sdir):

    #setup files to be processed, then run through spectcompbase.py
    if fun.casefold() == 'scb':
        #First setup files to be processed if 'fType' rather than 'files' is used
        os.chdir(sdir)
        if not fType:
            # Creates data structure with information on files with fType in name. if >1 fType, then concatenates together
            files = []
            # search list of files in the target directory and pull names matching the inputted filetype out, appending to the 'files' array
            for f in os.listdir(sdir):
                if f.endswith(fType):
                    files.append(f)

        # Run spectcompbase.py
        for i in range(1, len(files)):
            t = time.time() # begin recording time elapsed
            print("Running spectcompbase.py on file {} out of {}", i, len(files))
            cfg = scbParamsMulti(files[i])
            LFPTs,trls,clnTrls,relPower,psdTrls,coh,stdPower,stdCoh = spectcompbase(cfg)

            #TODO close files. clear all variables except files, i, sdir, and fun?
            files[i].close()

            timeElapsed = time.time() - t # calculate time elapsed

    # Run preProcess.py
    if fun.casefold() == 'pre':
        # First setup files to be processed if 'fType' rather than 'files' is used
        os.chdir(sdir)
        if not fType:
            # Creates data structure with information on files with fType in name. if >1 fType, then concatenates together
            files = []
            # search list of files in the target directory and pull names matching the inputted filetype out, appending to the 'files' array
            for f in os.listdir(sdir):
                if f.endswith(fType):
                    files.append(f)

        # Run spectcompbase.py
        for i in range(1, len(files)):
            print("Running preProcess.py on file {} out of {}", i, len(files))
            # TODO load data from file. try numpy routines https://numpy.org/doc/stable/reference/routines.io.html
            LFPTs,chk_nan,zeroedChannel,clnTrls,clnEvents,trls,adfreq = preProcess(LFPTs,adfreq,dsf,thresh,onset,offset,minInt,eoi,eventTs)
            # TODO save data to file. try numpy routines https://numpy.org/doc/stable/reference/routines.io.html
            # TODO close files. clear all variables except files, i, sdir, and fun?




















