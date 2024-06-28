import math

def get_result(x):
    """Branin function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Branin function
    """

    return (x[1] - 5.1/(4*math.pi**2)*x[0]**2 + 5/math.pi*x[0] - 6)**2 + 10*(1 - 1/(8*math.pi))*math.cos(x[0]) + 10