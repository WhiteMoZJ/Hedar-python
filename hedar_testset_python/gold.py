import math


def get_result(x):
    """Goldstein and Price function

    Args:
        x (list): input vector

    Returns:
        float: function value
    """

    x1 = x[0]
    x2 = x[1]

    term1 = 1 + (x1 + x2 + 1)**2 * (19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2)
    term2 = 30 + (2*x1 - 3*x2)**2 * (18 - 32*x1 + 12*x1**2 + 48*x2 - 36*x1*x2 + 27*x2**2)

    return term1 * term2