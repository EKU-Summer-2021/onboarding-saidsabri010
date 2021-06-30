import unittest
from src.read import Issue1

class MyTestCase(unittest.TestCase):
    """ class for running unittests """
    def test(self):
        """ Your setUp """
        data = Issue1()
        self.assertIsInstance(data, Issue1)




