import math

def get_result(x):
    """Powell function

    Args:
        x (list): list of input variables

    Returns:
        float: value of Powell function
    """

    n = len(x)
    n /= 4
    fvec = [0] * n

    for i in range(1, n+1):
        fvec[4*i-4] = x[4*i-4] + 10*x[4*i-3]
        fvec[4*i-3] = math.sqrt(5)*(x[4*i-2] - x[4*i-1])
        fvec[4*i-2] = (x[4*i-3] - 2*x[4*i-2])**2
        fvec[4*i-1] = math.sqrt(10)*(x[4*i-4] - x[4*i-1])

    return sum([f**2 for f in fvec])

