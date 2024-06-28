def get_result(x):
    """dp:  Computes the value of the Powell test function.
    Args:
        x: Input vector.
    Returns:
        y: Output value.
    """

    n = len(x)
    s1 = 0

    for j in range(1, n):
        s1 += (j + 1) * (2 * x[j] ** 2 - x[j - 1]) ** 2

    return s1 + (x[0] - 1) ** 2
