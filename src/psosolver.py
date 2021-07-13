"""
 PSOsolver model
"""
import os
import configparser
import numpy as np


def move_to_gposition(position, binary_list):
    """
        this function looks for the position where the output is 1
        if it finds 0 it turned into 1
    """
    for i in binary_list:
        if binary_list[i] == 1:
            position = binary_list.index(i)
        else:
            position = binary_list.index(i)
    return position


class PSO:
    """
    PSOsolver class
    """
    def __str__(self):
        return self.__class__.__name__

    def __init__(self, data):
        self.data = data
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../config', 'config.conf'))
        self.constant1 = int(float(config['Parameters']['c1']))
        self.constant2 = int(float(config['Parameters']['c2']))
        self.beta = int(float(config['Parameters']['beta']))
        self.random1 = int(float(config['Parameters']['r1']))
        self.random2 = int(float(config['Parameters']['r2']))

    def solve(self, _, items_can_we_choose_from, binary_list):
        """
            in this function,we first sort the values and we check
            if the weight is less than capacity
            if it is so,we sum the total_cost and if the
            binary list gives a 0 we call the function above
            to turn it into 1 and count it as well
        """
        total_cost = 0
        capacity = 30
        weight, value = self.data[:, 0], self.data[:, 1]
        sorted_values = -np.sort(-value)
        for index, _ in enumerate(np.sort(sorted_values)):
            if np.any(weight[index] > capacity):
                break
            else:
                capacity = capacity - weight[index]
                if weight in items_can_we_choose_from[index] and binary_list[index] == 1:
                    total_cost += sorted_values[index]
                elif weight in items_can_we_choose_from[index] and binary_list[index] == 0:
                    move_to_gposition(index, binary_list)
                    total_cost += sorted_values[index]
                else:
                    continue
        return total_cost
