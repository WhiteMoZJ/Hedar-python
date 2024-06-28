def get_result(x):
    """Matyas function

    Args:
        x (list): List of x values

    Returns:
        float: Result of the Matyas function
    """

    return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]
