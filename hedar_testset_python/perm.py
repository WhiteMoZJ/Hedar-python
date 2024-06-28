def get_result(x):
    """Perm function

    Args:
        x (list): List of input variables

    Returns:
        float: Value of the Perm function
    """

    b = 0.5
    result = 0
    for k in range(len(x)):
        inner_sum = 0
        for j in range(len(x)):
            inner_sum += (j ** (k + 1) + b) * (x[j] / (j + 1) ** k)
        result += inner_sum**2
    return result