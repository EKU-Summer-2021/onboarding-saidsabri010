"""
 model for testing
"""

import unittest
import pandas as pd
from src.cost import KS
from src.read import read_csv


class MyTestCase(unittest.TestCase):
    """ class for running unittests """

    def test_something(self):
        """ TEST METHOD """
        data = read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
            'main/Intelligent%20System%20Data/CSP/CSP_360.csv')
        dataframe = pd.DataFrame(data)
        k = KS(dataframe)
        expected = k.cost([1, 3, 2])
        self.assertIsInstance(expected, pd.DataFrame)
