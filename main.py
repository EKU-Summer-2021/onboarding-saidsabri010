import numpy as np
from src import Polynomial
from src.read import read_csv
if __name__ == '__main__':
    coeffs = np.array([1,0,0])
    polynom = Polynomial(coeffs)
    print(polynom.evaluate(3))
    print(polynom.roots())

print(read_csv())