"""
cost file that will handle task
"""


def cost(number_of_items):
    """
     cost method
     """
    list_of_items = []
    for item in range(0, number_of_items):
        element = int(input("enter the cost of items"))
        list_of_items.append(element)
        item += 1
    total_cost = sum(list_of_items)
    return total_cost
