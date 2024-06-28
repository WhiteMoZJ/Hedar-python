import math
import numpy as np


def get_result(x):
    """Hartmann 6 function.

    Args:
        x (list): input vector

    Returns:
        float: function value
    """
    alpha = np.array([1.0, 1.2, 3.0, 3.2])
    A = np.array([[10, 3, 17, 3.5, 1.7, 8],
                  [0.05, 10, 17, 0.1, 8, 14],
                  [3, 3.5, 1.7, 10, 17, 8],
                  [17, 8, 0.05, 10, 0.1, 14]])
    P = 10**-4 * np.array([[1312, 1696, 5569, 124, 8283, 5886],
                           [2329, 4135, 8307, 3736, 1004, 9991],
                           [2348, 1451, 3522, 2883, 3047, 6650],
                           [4047, 8828, 8732, 5743, 1091, 381]])

    outer_sum = 0
    for i in range(4):
        inner_sum = 0
        for j in range(6):
            xj = x[j]
            Aij = A[i, j]
            Pij = P[i, j]
            inner_sum += Aij * (xj - Pij)**2
        outer_sum += alpha[i] * math.exp(-inner_sum)

    return -outer_sum