"""
this is the main class
"""

import pandas as pd
from src.read import read_csv
from src.cost import KS

data = read_csv(
    'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
    'main/Intelligent%20System%20Data/KP/KP_10.csv')
dataframe = pd.DataFrame(data)
k = KS(dataframe.values)
print(k.cost(dataframe.index))
