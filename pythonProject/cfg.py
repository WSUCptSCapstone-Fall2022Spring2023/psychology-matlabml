# This class holds the configuration specifications for running our machine learning algorithm on a file dir
# containing experiment data. The specifications will be held as a class object. scbParamsMulti.py will create
# this class object. This design is borrowed from the previous team's work. We intend on making it easier
# to change parameters in the future.

class CFG:
    def __init__(self, sdir, file):
        self.sdir = sdir
        self.file = file
        self.nFilt = [57, 63]
        self.dsf = 5
        self.thresh = 1.5
        self.onset = 0.0125
        self.offset = 0.5
        self.foi = [1,1,100]
        self.bands = {'delta': [1,4],
             'theta': [5,10],
             'alpha': [11,14],
             'beta': [15,30],
             'lgamma': [45,65],
             'hgamma': [70,90]}
        self.overlap = 0.5
        self.cohMethod = 'mtm'
        self.skip = []
        self.vis = 'n'
        self.saveParent = sdir + '\processed'
