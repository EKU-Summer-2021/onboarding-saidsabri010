"""
cost file that will handle task
"""
import pandas as pd
from src.read import read_csv


class KS:
    """
       Knapsack class
    """

    def __str__(self):
        return self.__class__.__name__

    def cost(self):
        """
         cost method
         """
        total_cost = 0
        data = read_csv(self)
        dataframe = pd.DataFrame(data)
        for item in dataframe.columns:
            total_cost += dataframe[item]
        return total_cost
