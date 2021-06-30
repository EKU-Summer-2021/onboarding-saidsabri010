'''
Polynomial module with a simple Polynomial example class.
'''
import pandas as pd


def read_csv(source):
    """
    reading csv data
    """
    i = pd.read_csv(source)
    print(i.describe())

