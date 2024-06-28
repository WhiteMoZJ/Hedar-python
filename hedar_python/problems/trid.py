def get_result(x):
    """Trid function

    Args:
        x (list): List of input variables

    Returns:
        float: Value of the Trid function
    """

    return sum([(x[i] - 1)**2 for i in range(len(x))]) - sum([x[i]*x[i-1] for i in range(len(x))])