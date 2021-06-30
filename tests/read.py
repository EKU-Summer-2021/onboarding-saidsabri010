import unittest


class MyTestCase(unittest.TestCase):
    def test_upper(self):
        """
          test
          """
        self.assertEqual('foo'.upper(), 'FOO')



