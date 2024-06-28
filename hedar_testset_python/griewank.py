import math

def get_result(x):
    """Griewank's function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Griewank's function
    """
    n = len(x)
    sum1 = 0
    prod1 = 1
    for i in range(n):
        sum1 += x[i]**2
        prod1 *= math.cos(x[i]/math.sqrt(i+1))
    return 1 + sum1/4000 - prod1