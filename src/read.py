import pandas as pd

"""
reading csv data
"""
class Issue1:
    def read_csv(self):
        print('CSP data : ')
        df = pd.read_csv(
            'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
        print(df.describe())
