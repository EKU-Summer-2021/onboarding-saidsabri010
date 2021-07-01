import unittest
from src.cost import cost

class MyTestCase(unittest.TestCase):
    """ class for running unittests """
    def test_something(self):
        """ TEST METHOD """
        cost_of_items = cost(2)
        self.assertIsInstance(cost_of_items, int)



