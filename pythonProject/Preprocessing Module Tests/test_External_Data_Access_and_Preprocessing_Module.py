import unittest  # import unittest module
from External_Data_Access_and_Preprocessing_Module import AccessData, LoadData  # import classes from file to be tested


class TestAccessData(unittest.TestCase):
    """This class contains unit tests for the Access Data class"""
    def setUp(self):
        """This method is called before every test case"""
        self.AccessDataObject = AccessData()
        self.file = open("test_file.csv", "w")

    def tearDown(self):
        """This method is called after every test case"""
        self.file.close()


class TestLoadData(unittest.TestCase):
    """This class contains unit tests for the Load Data class"""
    def setUp(self):
        """This method is called before every test case"""
        self.LoadDataObject = LoadData()
        self.file = open("test_file.csv", "w")

    def tearDown(self):
        """This method is called after every test case"""
        self.file.close()


if __name__ == "__main__":
    unittest.main()  # run all tests
