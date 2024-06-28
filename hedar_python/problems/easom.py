import math


def get_result(x):
    """Easom function

    Args:
        x (list): List of input values

    Returns:
        float: Output value
    """
    return -math.cos(x[0]) * math.cos(x[1]) * math.exp(-((x[0] - math.pi) ** 2 + (x[1] - math.pi) ** 2))