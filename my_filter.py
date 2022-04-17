from typing import Iterable
from types import FunctionType


def my_filter(function: FunctionType, iterable: Iterable) -> Iterable:
    """
    A function called my_filter that behaves just like the filter function.
    :param function: The function on which the filter will operate.
    :param iterable: Iterable on which the function will pass.
    :return: Iterable of all the parameters for which the function returns True.
    """
    for item in iterable:
        if function(item):
            yield item


if __name__ == '__main__':
    def is_mature(age):
        return age >= 18


    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = my_filter(is_mature, ages)
    print(tuple(mature_ages))
