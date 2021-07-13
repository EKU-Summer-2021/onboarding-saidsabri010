"""
cost file that will handle task
"""

import unittest
import pandas as pd
import numpy as np
from src.psosolver import PSO
from src.read import read_csv


class MyTestCase(unittest.TestCase):
    """ class for running unittests """

    def test_psosolver(self):
        """ TEST METHOD """
        data = read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
            'main/Intelligent%20System%20Data/KP/KP_10.csv')
        dataframe = pd.DataFrame(data)
        k = PSO(dataframe.values)
        actual = k.solve(dataframe.values, np.sort(dataframe.iloc[:, 0:1].values),
                         [0, 1, 1, 0, 1, 1, 0, 0, 1])
        expected = 286
        self.assertEqual(expected, actual)
