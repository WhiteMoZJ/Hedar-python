import math
import numpy as np


def get_result(x):
    """Hartmann 3 function

    Args:
        x (list): input vector

    Returns:
        float: function value
    """

    alpha = np.array([1.0, 1.2, 3.0, 3.2])

    A = np.array([[3.0, 10, 30],
                  [0.1, 10, 35],
                  [3.0, 10, 30],
                  [0.1, 10, 35]])

    P = 10**-4 * np.array([[3689, 1170, 2673],
                           [4699, 4387, 7470],
                           [1091, 8732, 5547],
                           [381, 5743, 8828]])
    result = 0

    for i in range(4):
        result += alpha[i] * math.exp(-np.dot(A[i], (x - P[i])**2))

    return -result
