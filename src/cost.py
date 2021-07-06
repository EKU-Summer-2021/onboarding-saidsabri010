"""
cost file that will handle task
"""


class KS:
    """
       Knapsack class
    """

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, data):
        self.data = data

    def cost(self, items):
        """
         cost method
        """
        total_cost = 0
        for _ in range(len(items)):
            total_cost = sum(self.data[:, 1])
        return total_cost
