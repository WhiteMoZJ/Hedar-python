import math


def get_result(x):
    """Rastrigin function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Rastrigin function
    """

    n = len(x)
    s = 0

    for i in range(n):
        s += x[i]**2 - 10 * math.cos(2 * math.pi * x[i])

    return 10 * n + s