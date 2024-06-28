def get_result(x):
    """Power sum function
    Args:
        x (list): input value

    Returns:
        float: output value
    """

    n = len(x)
    b = [8, 18, 44, 114]
    s = 0

    for i in range(n):
        sm = 0
        for j in range(4):
            sm += x[j] ** (i+1)

        s += (sm - b[i]) ** 2

    return s