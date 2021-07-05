""" class for running unittests """

import unittest
import pandas as pd
from src.cost import KS


class MyTestCase(unittest.TestCase):
    """ class for running unittests """

    def test_something(self):
        """ TEST METHOD """
        total_cost = KS.cost(
            'https://raw.githubusercontent.com/EKU-Summer-2021/'
            'intelligent_system_data/main/Intelligent'
        '%20System%20Data/CSP/CSP_360.csv')
        data = pd.DataFrame(total_cost)
        self.assertIsInstance(data, pd.DataFrame)
