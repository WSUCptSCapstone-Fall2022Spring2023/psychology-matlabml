import unittest  # import unittest module
from External_Data_Access_and_Preprocessing_Module import AccessData, LoadData  # import classes from file to be tested


class TestAccessData(unittest.TestCase):
    """This class contains unit tests for the Access Data class"""
    def setUp(self):
        """This method is called before every test case"""
        self.AccessDataObject = AccessData(r'C:\Users\aidan.nunn\Documents\Homework\CS 421\Sample Data')
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
        self.fail("No test yet")
    def testGetFileNames(self):
        self.fail("No test yet")




class TestLoadData(unittest.TestCase):
    """This class contains unit tests for the Load Data class"""
    def setUp(self):
        """This method is called before every test case"""
        self.LoadDataObject = LoadData()

    def tearDown(self):
        """This method is called after every test case"""


if __name__ == "__main__":
    unittest.main()  # run all tests
