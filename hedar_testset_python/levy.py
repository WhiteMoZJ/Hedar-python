import math


def get_result(x):
    """Levy function.

    Args:
        x (list): input variables

    Returns:
        float: output value
    """

    n = len(x)
    z = list(range(n))

    for i in range(n):
        z[i] = 1 + (x[i]-1) / 4

    s = math.sin(math.pi * z[0]) ** 2
    for i in range(n-1):
        s += (z[i]-1) ** 2 * (1 + 10 * math.sin(math.pi * z[i] + 1) ** 2)

    return s + (z[n-1]-1) ** 2 * (1 + math.sin(2 * math.pi * z[n-1]) ** 2)