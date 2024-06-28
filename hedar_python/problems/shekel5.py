import math
import numpy as np

def get_result(x):
    """Shekel's foxholes function

    Args:
        x (list): list of input variables
        m (int): number of foxholes

    Returns:
        float: value of Shekel's foxholes function
    """

    a = np.array([[4, 4, 4, 4],
                  [1, 1, 1, 1],
                  [8, 8, 8, 8],
                  [6, 6, 6, 6],
                  [3, 7, 3, 7],
                  [2, 9, 2, 9],
                  [5, 5, 3, 3],
                  [8, 1, 8, 1],
                  [6, 2, 6, 2],
                  [7, 3.6, 7, 3.6]])
    c = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    result = 0

    for i in range(5):
        result += 1 / (np.dot(np.array(x) - a[i], np.array(x) - a[i]) + c[i])

    return -result