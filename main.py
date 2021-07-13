"""
this is the main class
"""

import pandas as pd
import numpy as np
from src.read import read_csv
from src.psosolver import PSO

data = read_csv(
    'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/'
    'main/Intelligent%20System%20Data/KP/KP_10.csv')
dataframe = pd.DataFrame(data)
k = PSO(dataframe.values)
print(k.solve(dataframe.values,  np.sort(dataframe.iloc[:, 0:1].values),
              [0, 1, 1, 0, 1, 1, 0, 0, 1]))
