def get_result(x):
    """Booth function.

    Args:
        x (list): List of input variables.

    Returns:
        float: Value of the Booth function.
    """

    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2