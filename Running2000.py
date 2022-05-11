from time import process_time
from collections.abc import Callable
from typing import Generic, TypeVar


T = TypeVar('T')


def timer(f:Callable, *params:Generic[T])-> float:
    """
    The timer function will measure how long a function f ran when the sent parameters are passed to it.
    :param f: The measured function.
    :param params: The parameters sent.
    :return: The function will return the duration of the execution of the function f on the params parameters
    """
    starting_time = process_time()
    f(params)
    finishing_time = process_time()
    return finishing_time - starting_time


if __name__ == '__main__':
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
