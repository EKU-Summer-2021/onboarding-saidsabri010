import pandas as pd

"""
reading csv data
"""

def read_csv(source):
    df = pd.read_csv(source)
    print(df.describe())

