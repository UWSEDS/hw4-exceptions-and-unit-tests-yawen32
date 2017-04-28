# Data 515 Homework 4
# Yawen Li

import unittest
from HW4_Functions import get_data
import os


class TestGetData(unittest.TestCase):

    def testFileExistLocally(self):
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv "
        result = get_data(url)
        self.assertEqual(result,0,"File is not present locally.")

    def testFileNotLocally(self):
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv "
        filename = os.path.basename(url)
        #remove_data(filename)
        if os.path.exists(filename):
            os.remove(filename)
        result = get_data(url)
        self.assertEqual(result,0,"File has already presented locally.")

    def testUrlNotExists(self):
        url = "https://data.seattle.gov/resource/4xydfdf5-26gy.csv"
        result = get_data(url)
        self.assertEqual(result, 404, "Url result is not 404")




if __name__ == '__main__':
    unittest.main()

