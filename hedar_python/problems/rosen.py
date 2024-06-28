def get_result(x):
    """Rosenbrock function

    Args:
        x (list): List of input variables

    Returns:
        float: Value of the Rosenbrock function
    """

    return sum([100*(x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x)-1)])