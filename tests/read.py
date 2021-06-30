import unittest
import pandas as pd
from src.read import read_csv

class MyTestCase(unittest.TestCase):
    """ class for running unittests """
    def test(self):
        """ Your setUp """
        data = read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent'
                        '%20System%20Data/CSP/CSP_360.csv')
        df = pd.DataFrame(data)
        self.assertIsInstance(df, pd.DataFrame)




