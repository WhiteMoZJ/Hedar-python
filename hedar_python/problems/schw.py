import math

def get_result(x):
    """Schwefel's function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Schwefel's function
    """
    return 418.9829 * len(x) - sum([xi * math.sin(math.sqrt(abs(xi))) for xi in x])
