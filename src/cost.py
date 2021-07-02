"""
cost file that will handle task
"""
import pandas as pd
from src.read import read_csv


def cost(source):
    """
     cost method
     """
    total_cost = 0
    data = read_csv(source)
    dataframe = pd.DataFrame(data)
    for item in dataframe.columns:
        total_cost += dataframe[item]
    return total_cost
