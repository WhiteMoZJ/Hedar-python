def get_result(x):
    """Zakharov function

    Args:
        x (list): List of input variables

    Returns:
        float: Value of the Zakharov function
    """

    sum1 = sum([i**2 for i in x])
    sum2 = sum([0.5*i*(j+1) for j, i in enumerate(x)])

    return sum1 + sum2**2 + sum2**4