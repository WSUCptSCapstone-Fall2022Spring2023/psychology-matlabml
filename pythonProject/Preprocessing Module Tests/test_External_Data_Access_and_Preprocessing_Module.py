import unittest  # import unittest module
from Preprocessing_Module_Binary_Classifier import AccessData, LoadData  # import classes from file to be tested


class TestAccessData(unittest.TestCase):
    """This class contains unit tests for the Access Data class"""
    def setUp(self):
        """This method is called before every test case. Please create a directory for AccessData to open with one .pl2 file in it, otherwise testGetFileNames() will fail."""
        self.AccessDataObject = AccessData(r'C:\Users\aidan.nunn\Documents\Homework\CS 421\SampleSampleData')
        self.file = open("test_file.csv", "w")

    def tearDown(self):
        """This method is called after every test case"""
        self.file.close()

    def testSplitSignal(self):
        """Unit test of the splitSignal() method. We use two sample arrays of signal values and frequency values"""

        signalArray =    [1,    2, 3,  4, 5,  6,  7,  8,  9,  10,  11, 12, 13,   14,  15]
        frequencyArray = [0.02, 2, 66, 9, 78, 12, 30, 40, 91, 4.5, 2,  43, 55.6, 120, 17]

        expectedResult = [6.5, 4, 6, 11, 13, 5]

        actualResult = self.AccessDataObject._AccessData__splitSignal(frequencyArray, signalArray)

        self.assertEqual(expectedResult, actualResult)

    def testCreateHeader(self):
        """Unit test of the method which creates the header for the csv file power and coherence values are sent to."""

        expectedResult = ['Channel 1 Power Delta', 'Channel 1 Power Theta', 'Channel 1 Power Alpha', 'Channel 1 Power Beta',
                          'Channel 1 Power Low Gamma', 'Channel 1 Power High Gamma', 'Channel 2 Power Delta', 'Channel 2 Power Theta',
                          'Channel 2 Power Alpha', 'Channel 2 Power Beta', 'Channel 2 Power Low Gamma', 'Channel 2 Power High Gamma',
                          'Channel 3 Power Delta', 'Channel 3 Power Theta', 'Channel 3 Power Alpha', 'Channel 3 Power Beta',
                          'Channel 3 Power Low Gamma', 'Channel 3 Power High Gamma', 'Channel 4 Power Delta', 'Channel 4 Power Theta',
                          'Channel 4 Power Alpha', 'Channel 4 Power Beta', 'Channel 4 Power Low Gamma', 'Channel 4 Power High Gamma',
                          'Channel 5 Power Delta', 'Channel 5 Power Theta', 'Channel 5 Power Alpha', 'Channel 5 Power Beta',
                          'Channel 5 Power Low Gamma', 'Channel 5 Power High Gamma', 'Channel 6 Power Delta', 'Channel 6 Power Theta',
                          'Channel 6 Power Alpha', 'Channel 6 Power Beta', 'Channel 6 Power Low Gamma', 'Channel 6 Power High Gamma',
                          'Channel 7 Power Delta', 'Channel 7 Power Theta', 'Channel 7 Power Alpha', 'Channel 7 Power Beta', 'Channel 7 Power Low Gamma',
                          'Channel 7 Power High Gamma', 'Channel 8 Power Delta', 'Channel 8 Power Theta', 'Channel 8 Power Alpha', 'Channel 8 Power Beta',
                          'Channel 8 Power Low Gamma', 'Channel 8 Power High Gamma', 'Coherence 1 & 2 Delta', 'Coherence 1 & 2 Theta', 'Coherence 1 & 2 Alpha',
                          'Coherence 1 & 2 Beta', 'Coherence 1 & 2 Low Gamma', 'Coherence 1 & 2 High Gamma', 'Coherence 1 & 3 Delta', 'Coherence 1 & 3 Theta',
                          'Coherence 1 & 3 Alpha', 'Coherence 1 & 3 Beta', 'Coherence 1 & 3 Low Gamma', 'Coherence 1 & 3 High Gamma', 'Coherence 1 & 4 Delta',
                          'Coherence 1 & 4 Theta', 'Coherence 1 & 4 Alpha', 'Coherence 1 & 4 Beta', 'Coherence 1 & 4 Low Gamma', 'Coherence 1 & 4 High Gamma',
                          'Coherence 1 & 5 Delta', 'Coherence 1 & 5 Theta', 'Coherence 1 & 5 Alpha', 'Coherence 1 & 5 Beta', 'Coherence 1 & 5 Low Gamma',
                          'Coherence 1 & 5 High Gamma', 'Coherence 1 & 6 Delta', 'Coherence 1 & 6 Theta', 'Coherence 1 & 6 Alpha', 'Coherence 1 & 6 Beta',
                          'Coherence 1 & 6 Low Gamma', 'Coherence 1 & 6 High Gamma', 'Coherence 1 & 7 Delta', 'Coherence 1 & 7 Theta', 'Coherence 1 & 7 Alpha',
                          'Coherence 1 & 7 Beta', 'Coherence 1 & 7 Low Gamma', 'Coherence 1 & 7 High Gamma', 'Coherence 1 & 8 Delta', 'Coherence 1 & 8 Theta',
                          'Coherence 1 & 8 Alpha', 'Coherence 1 & 8 Beta', 'Coherence 1 & 8 Low Gamma', 'Coherence 1 & 8 High Gamma', 'Coherence 2 & 3 Delta',
                          'Coherence 2 & 3 Theta', 'Coherence 2 & 3 Alpha', 'Coherence 2 & 3 Beta', 'Coherence 2 & 3 Low Gamma', 'Coherence 2 & 3 High Gamma',
                          'Coherence 2 & 4 Delta', 'Coherence 2 & 4 Theta', 'Coherence 2 & 4 Alpha', 'Coherence 2 & 4 Beta', 'Coherence 2 & 4 Low Gamma',
                          'Coherence 2 & 4 High Gamma', 'Coherence 2 & 5 Delta', 'Coherence 2 & 5 Theta', 'Coherence 2 & 5 Alpha', 'Coherence 2 & 5 Beta',
                          'Coherence 2 & 5 Low Gamma', 'Coherence 2 & 5 High Gamma', 'Coherence 2 & 6 Delta', 'Coherence 2 & 6 Theta', 'Coherence 2 & 6 Alpha',
                          'Coherence 2 & 6 Beta', 'Coherence 2 & 6 Low Gamma', 'Coherence 2 & 6 High Gamma', 'Coherence 2 & 7 Delta', 'Coherence 2 & 7 Theta',
                          'Coherence 2 & 7 Alpha', 'Coherence 2 & 7 Beta', 'Coherence 2 & 7 Low Gamma', 'Coherence 2 & 7 High Gamma', 'Coherence 2 & 8 Delta',
                          'Coherence 2 & 8 Theta', 'Coherence 2 & 8 Alpha', 'Coherence 2 & 8 Beta', 'Coherence 2 & 8 Low Gamma', 'Coherence 2 & 8 High Gamma',
                          'Coherence 3 & 4 Delta', 'Coherence 3 & 4 Theta', 'Coherence 3 & 4 Alpha', 'Coherence 3 & 4 Beta', 'Coherence 3 & 4 Low Gamma',
                          'Coherence 3 & 4 High Gamma', 'Coherence 3 & 5 Delta', 'Coherence 3 & 5 Theta', 'Coherence 3 & 5 Alpha', 'Coherence 3 & 5 Beta',
                          'Coherence 3 & 5 Low Gamma', 'Coherence 3 & 5 High Gamma', 'Coherence 3 & 6 Delta', 'Coherence 3 & 6 Theta', 'Coherence 3 & 6 Alpha',
                          'Coherence 3 & 6 Beta', 'Coherence 3 & 6 Low Gamma', 'Coherence 3 & 6 High Gamma', 'Coherence 3 & 7 Delta', 'Coherence 3 & 7 Theta',
                          'Coherence 3 & 7 Alpha', 'Coherence 3 & 7 Beta', 'Coherence 3 & 7 Low Gamma', 'Coherence 3 & 7 High Gamma', 'Coherence 3 & 8 Delta',
                          'Coherence 3 & 8 Theta', 'Coherence 3 & 8 Alpha', 'Coherence 3 & 8 Beta', 'Coherence 3 & 8 Low Gamma', 'Coherence 3 & 8 High Gamma',
                          'Coherence 4 & 5 Delta', 'Coherence 4 & 5 Theta', 'Coherence 4 & 5 Alpha', 'Coherence 4 & 5 Beta', 'Coherence 4 & 5 Low Gamma',
                          'Coherence 4 & 5 High Gamma', 'Coherence 4 & 6 Delta', 'Coherence 4 & 6 Theta', 'Coherence 4 & 6 Alpha', 'Coherence 4 & 6 Beta',
                          'Coherence 4 & 6 Low Gamma', 'Coherence 4 & 6 High Gamma', 'Coherence 4 & 7 Delta', 'Coherence 4 & 7 Theta', 'Coherence 4 & 7 Alpha',
                          'Coherence 4 & 7 Beta', 'Coherence 4 & 7 Low Gamma', 'Coherence 4 & 7 High Gamma', 'Coherence 4 & 8 Delta', 'Coherence 4 & 8 Theta',
                          'Coherence 4 & 8 Alpha', 'Coherence 4 & 8 Beta', 'Coherence 4 & 8 Low Gamma', 'Coherence 4 & 8 High Gamma', 'Coherence 5 & 6 Delta',
                          'Coherence 5 & 6 Theta', 'Coherence 5 & 6 Alpha', 'Coherence 5 & 6 Beta', 'Coherence 5 & 6 Low Gamma', 'Coherence 5 & 6 High Gamma',
                          'Coherence 5 & 7 Delta', 'Coherence 5 & 7 Theta', 'Coherence 5 & 7 Alpha', 'Coherence 5 & 7 Beta', 'Coherence 5 & 7 Low Gamma',
                          'Coherence 5 & 7 High Gamma', 'Coherence 5 & 8 Delta', 'Coherence 5 & 8 Theta', 'Coherence 5 & 8 Alpha', 'Coherence 5 & 8 Beta',
                          'Coherence 5 & 8 Low Gamma', 'Coherence 5 & 8 High Gamma', 'Coherence 6 & 7 Delta', 'Coherence 6 & 7 Theta', 'Coherence 6 & 7 Alpha',
                          'Coherence 6 & 7 Beta', 'Coherence 6 & 7 Low Gamma', 'Coherence 6 & 7 High Gamma', 'Coherence 6 & 8 Delta', 'Coherence 6 & 8 Theta',
                          'Coherence 6 & 8 Alpha', 'Coherence 6 & 8 Beta', 'Coherence 6 & 8 Low Gamma', 'Coherence 6 & 8 High Gamma', 'Coherence 7 & 8 Delta',
                          'Coherence 7 & 8 Theta', 'Coherence 7 & 8 Alpha', 'Coherence 7 & 8 Beta', 'Coherence 7 & 8 Low Gamma', 'Coherence 7 & 8 High Gamma', 'A or D']


        self.AccessDataObject._AccessData__createHeaderForBinaryClassifierCSV()
        actualResult = self.AccessDataObject.header

        self.assertEqual(expectedResult, actualResult)

    def testGetFileNames(self):
        """Unit test of the method which gets the file names of all files in a directory. This method reads a directory
        on your local PC, so the test will fail unless a directory matching the one in the setup method exists with a
        file matching the name in this function (Please change if running on your PC)"""

        expectedResult = ['A170_post0_2020-4-20_pl2_spl_ead_plx.pl2']
        actualResult = self.AccessDataObject._AccessData__getFileNames()

        self.assertEqual(expectedResult, actualResult)

    def testVoltsToRawAD(self):
        """Unit test of the voltsToRawAD() method."""

        input = [-0.000007, 0.0000033, -0.0000058, -0.000015, 0.0000175]

        expectedResult = [-36, 17, -30, -77, 90]

        actualResult = self.AccessDataObject.voltsToRawAD(input)

        self.assertEqual(expectedResult, actualResult)

    def testNoiseArtifactsFilter(self):
        """Unit test of the noiseArtifactsFilter() method. Inputs for filtering are a 1.5 threshold, 1 onset, and 2 offset."""

        input = [2, -0.24, 0.8, 0.76, 0.01, 0.04, 0.07, 7, 0.09, 0.08, 0.04, 0.9, 1.5, 0.001, 81, 0.5, -1.7, 0.4, -1, -4, 0.05, -0.9, 8]

        expectedResult = [0.76, 0.01, 0.04, 0.04, 0.4, -1, -4, 0.05]

        actualResult = self.AccessDataObject._AccessData__noiseArtifactsFilter(input, 1.5, 1, 2)

        self.assertEqual(expectedResult, actualResult)



class TestLoadData(unittest.TestCase):
    """This class contains unit tests for the Load Data class"""
    def setUp(self):
        """This method is called before every test case"""
        self.LoadDataObject = LoadData()

    def tearDown(self):
        """This method is called after every test case"""


if __name__ == "__main__":
    unittest.main()  # run all tests
