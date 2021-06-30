import pandas as pd

def read_csv():
    """
    reading csv data
    """
    print('CSP data : ')
    x = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_360.csv')
    y = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_53000.csv')
    m = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/CSP/CSP_6200.csv')
    print(x.describe())
    print(y.describe())
    print(m.describe())

    print('-------------------------------')

    print('KP data : ')
    i = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_10.csv')
    j = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_100.csv')
    k = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/KP/KP_1000.csv')
    print(i.describe())
    print(j.describe())
    print(k.describe())

    print('-------------------------------')

    print('TSP data : ')
    l = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/10.csv')
    n = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/100.csv')
    d = pd.read_csv(
        'https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data/main/Intelligent%20System%20Data/TSP/1000.csv')
    print(l.describe())
    print(n.describe())
    print(d.describe())
