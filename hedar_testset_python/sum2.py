def get_result(x):
    """Sum Squares function

    Args:
        x (list): List of x values

    Returns:
        float: Result of the Sum Squares function
    """

    n = len(x)
    s = 0
    for j in range(n):
        s += (j+1) * x[j]**2

    return s