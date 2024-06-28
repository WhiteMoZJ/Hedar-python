import math

def get_result(x):
    """Michalewicz function

    Args:
        x (list): list of variables

    Returns:
        float: function value
    """

    m = 10
    result = 0
    for i in range(len(x)):
        result += math.sin(x[i]) * math.sin((i+1) * x[i]**2 / math.pi)**(2*m)
    return -result