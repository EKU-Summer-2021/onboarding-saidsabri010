"""
 model for testing
"""

import unittest
import pandas as pd
from src.cost import KS


class MyTestCase(unittest.TestCase):
    """ class for running unittests """

    def test_something(self):
        """ TEST METHOD """
        data = pd.read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
            'main/Intelligent%20System%20Data/KP/KP_10.csv')
        dataframe = pd.DataFrame(data)
        k = KS(dataframe.values)
        actual = k.cost(dataframe.values, dataframe.iloc[:4, 0:1].values, [1, 0, 0, 1, 1, 0])
        expected = 162
        self.assertEqual(expected, actual)
