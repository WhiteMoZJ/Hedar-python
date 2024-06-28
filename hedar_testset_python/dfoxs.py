import numpy as np

def get_result(n, nprob, factor):
    """dfoxs:  Generates starting point for optimization test problems.
    Args:
        n: Dimension of the problem.
        nprob: Problem number.
        factor: Scaling factor.
    Returns:
        x: Initial guess.
    """

    x = [0.0] * n

    if nprob in [1, 2, 3]:
        x = np.ones(n)
    elif nprob == 4:
        x = np.array([-1.2, 1])
    elif nprob == 5:
        x = np.array([-1])
    elif nprob == 6:
        x = np.array([3, -1, 0, 1])
    elif nprob == 7:
        x = np.array([0.5, -2])
    elif nprob == 8:
        x = np.ones(3)
    elif nprob == 9:
        x = np.array([0.25, 0.39, 0.415, 0.39])
    elif nprob == 10:
        x = np.array([0.02, 4000, 250])
    elif nprob == 11:
        x = 0.5 * np.ones(n)
    elif nprob == 12:
        x = np.array([0, 10, 20])
    elif nprob == 13:
        x = np.array([0.3, 0.4])
    elif nprob == 14:
        x = np.array([25, 5, -5, -1])
    elif nprob == 15:
        x = np.array([(k + 1) / (n + 1) for k in range(n)])
    elif nprob == 16:
        x = 0.5 * np.ones(n)
    elif nprob == 17:
        x = np.array([0.5, 1.5, 1, 0.01, 0.02])
    elif nprob == 18:
        x = np.array([1.3, 0.65, 0.65, 0.7, 0.6, 3, 5, 7, 2, 4.5, 5.5])
    elif nprob == 19:
        x = np.ones(n)
    elif nprob == 20:
        x = 0.5 * np.ones(n)
    elif nprob == 21:
        x = np.zeros(n)
        for i in range(1, n + 1):
            ss = 0
            for j in range(1, n + 1):
                ss += (np.sqrt(i / j) * (np.sin(np.log(np.sqrt(i / j)))**5 + np.cos(np.log(np.sqrt(i / j)))**5))
            x[i - 1] = -8.710996e-4 * ((i - 50)**3 + ss)
    elif nprob == 22:
        x = np.array([-0.3, -0.39, 0.3, -0.344, -1.2, 2.69, 1.59, -1.5])

    return x * factor
