import pandas as pd

"""
reading csv data
"""

def read_csv():
    print('CSP data : ')
    df = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
    df2 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_53000.csv')
    df3 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_6200.csv')
    print(df)
    print(df2.describe())
    print(df3.describe())

    print('-------------------------------')

    print('KP data : ')
    df4 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_10.csv')
    df5 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_100.csv')
    df6 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_1000.csv')
    print(df4.describe())
    print(df5.describe())
    print(df6.describe())

    print('-------------------------------')

    print('TSP data : ')
    df7 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv')
    df8 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/100.csv')
    df9 = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/1000.csv')
    print(df7.describe())
    print(df8.describe())
    print(df9.describe())
