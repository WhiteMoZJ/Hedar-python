import math

def get_result(x):
    """Shubert function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Shubert function
    """
    s1 = 0
    s2 = 0
    for j in range(1, 6):
        s1 += j * math.cos((j + 1) * x[0] + j)
        s2 += j * math.cos((j + 1) * x[1] + j)
    return s1 * s2