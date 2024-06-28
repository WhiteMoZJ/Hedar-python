import math

def get_result(x):
    """Ackley's function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Ackley's function
    """
    n = len(x)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += x[i]**2
        sum2 += math.cos(2*math.pi*x[i])
    return -20*math.exp(-0.2*math.sqrt(sum1/n)) - math.exp(sum2/n) + 20 + math.e
