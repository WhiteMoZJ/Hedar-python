def get_result(x):
    """Beale's function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Beale's function
    """
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2