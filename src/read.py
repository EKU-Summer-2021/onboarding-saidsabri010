"""
Polynomial module with a simple Polynomial example class.
"""
import pandas as pd


def read_csv(source):
    """
    reading csv data
    """
    df = pd.read_csv(source)
    return df
