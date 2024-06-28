def get_result(x):
    """Colville function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Colville function
    """

    return (100*(x[0]**2 - x[1])**2 + (1 - x[0])**2 + 90*(x[3] - x[2])**2 +
            (1 - x[2])**2 + 10.1*((x[1] - 1)**2 + (x[3] - 1)**2) + 19.8*(x[1] - 1)*(x[3] - 1))