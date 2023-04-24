import pandas as pd
import pickle

class LoadData:
    """Class used to load a CSV file of data into a pandas dataframe for use in the logic modules"""

    def __init__(self, *args):
        excl_list = []
        for arg in args:
            excl_list.append(pd.read_excel(arg))
        self.df = pd.concat(excl_list)

    def printDataFrame(self):
        """Method for printing the dataframe to a terminal window."""
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.df)

    def saveModel(self, model, filename):
        pickle.dump(model, open(filename, 'wb'))

    def loadModel(self, filename):
        return pickle.load(open(filename, 'rb'))