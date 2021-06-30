import unittest
import pandas as pd

from pandas.util.testing import assert_frame_equal

class MyTestCase(unittest.TestCase):
    """ class for running unittests """
    def setUp(self):
        """ Your setUp """
        try:
            data = pd.read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
        except IOError:
            print
            'cannot open file'
        self.fixture = data

    def test_dataFrame_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        foo = pd.read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
        assert_frame_equal(self.fixture, foo)



