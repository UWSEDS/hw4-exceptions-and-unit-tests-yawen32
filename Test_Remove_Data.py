# Data 515 Homework 4
# Yawen Li

import unittest
from HW4_Functions import remove_data
import os

class TestRemoveData(unittest.TestCase):
    def testRemoveData(self):
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv "
        filename = os.path.basename(url)
        f = open(filename, "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
        f.close()
        self.assertEqual(os.path.exists(filename), True)
        remove_data(url)
        self.assertEqual(os.path.exists(filename), False)

if __name__ == '__main__':
    unittest.main()