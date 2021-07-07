"""
cost file that will handle task
"""


class KS:
    """
       Knapsack class
    """

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, data):
        self.data = data

    def cost(self, _, items_wanted_tobe_put, binary_list):
        """
         cost function
        """
        total_cost = 0
        for index, _ in enumerate(items_wanted_tobe_put):
            weight, value = self.data[:, 0], self.data[:, 1]
            if weight in items_wanted_tobe_put[index] and binary_list[index] == 1:
                total_cost += value[index]
            else:
                continue
        return total_cost
