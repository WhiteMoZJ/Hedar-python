from hedar_python.problems import *
import numpy as np

"""
68 problem test example
"""

problems2d = [0, 4, 5, 6, 7, 8, 9, 11, 15, 16, 17, 23, 24, 28, 29, 38, 42, 46, 53, 54, 58, 64]


def get_problems_option(n):
    """
    reference to: http://www-optima.amp.i.kyoto-u.ac.jp/member/student/hedar/Hedar_files/TestGO_files/Page364.htm
    """
    global problem, bounds, globalmin
    if n == 0:
        globalmin = 0
        problem = ackley
        bounds = [-15 * np.ones([2, 1]), 30 * np.ones([2, 1])]
    elif n == 1:
        globalmin = 0
        problem = ackley
        bounds = [-15 * np.ones([5, 1]), 30 * np.ones([5, 1])]
    elif n == 2:
        globalmin = 0
        problem = ackley
        bounds = [-15 * np.ones([10, 1]), 30 * np.ones([10, 1])]
    elif n == 3:
        globalmin = 0
        problem = ackley
        bounds = [-15 * np.ones([20, 1]), 30 * np.ones([20, 1])]
    elif n == 4:
        globalmin = 0
        problem = beale
        bounds = [-4.5 * np.ones([2, 1]), 4.5 * np.ones([2, 1])]
    elif n == 5:
        globalmin = 0
        problem = bh1
        bounds = [-80 * np.ones([2, 1]), 125 * np.ones([2, 1])]
    elif n == 6:
        globalmin = 0
        problem = bh2
        bounds = [-80 * np.ones([2, 1]), 125 * np.ones([2, 1])]
    elif n == 7:
        globalmin = 0
        problem = bh3
        bounds = [-80 * np.ones([2, 1]), 125 * np.ones([2, 1])]
    elif n == 8:
        globalmin = 0
        problem = booth
        bounds = [-10 * np.ones([2, 1]), 10 * np.ones([2, 1])]
    elif n == 9:
        globalmin = 0
        problem = branin
        bounds = [[-5, 10], [0, 15]]
    elif n == 10:
        globalmin = 0
        problem = colville
        bounds = [-8 * np.ones([4, 1]), 12.5 * np.ones([4, 1])]
    elif n == 11:
        globalmin = 0
        problem = dp
        bounds = [-10 * np.ones([2, 1]), 10 * np.ones([2, 1])]
    elif n == 12:
        globalmin = 0
        problem = dp
        bounds = [-10 * np.ones([5, 1]), 10 * np.ones([5, 1])]
    elif n == 13:
        globalmin = 0
        problem = dp
        bounds = [-10 * np.ones([10, 1]), 10 * np.ones([10, 1])]
    elif n == 14:
        globalmin = 0
        problem = dp
        bounds = [-10 * np.ones([20, 1]), 10 * np.ones([20, 1])]
    elif n == 15:
        globalmin = -1
        problem = easom
        bounds = [-100 * np.ones([2, 1]), 100 * np.ones([2, 1])]
    elif n == 16:
        globalmin = 3
        problem = gold
        bounds = [[-2, 2], [-2, 2]]
    elif n == 17:
        globalmin = 0
        problem = griewank
        bounds = [-480 * np.ones([2, 1]), 750 * np.ones([2, 1])]
    elif n == 18:
        globalmin = 0
        problem = griewank
        bounds = [-480 * np.ones([5, 1]), 750 * np.ones([5, 1])]
    elif n == 19:
        globalmin = 0
        problem = griewank
        bounds = [-480 * np.ones([10, 1]), 750 * np.ones([10, 1])]
    elif n == 20:
        globalmin = 0
        problem = griewank
        bounds = [-480 * np.ones([20, 1]), 750 * np.ones([20, 1])]
    elif n == 21:
        globalmin = -3.86278214782076
        problem = hart3
        bounds = [[0, 1], [0, 1], [0, 1]]
    elif n == 22:
        globalmin = -3.32236801141551
        problem = hart6
        bounds = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
    elif n == 23:
        globalmin = -1.0316284535
        problem = hump
        bounds = [[-5, 5], [-5, 5]]
    elif n == 24:
        globalmin = 0
        problem = levy
        bounds = [-10 * np.ones([2, 1]), 10 * np.ones([2, 1])]
    elif n == 25:
        globalmin = 0
        problem = levy
        bounds = [-10 * np.ones([5, 1]), 10 * np.ones([5, 1])]
    elif n == 26:
        globalmin = 0
        problem = levy
        bounds = [-10 * np.ones([10, 1]), 10 * np.ones([10, 1])]
    elif n == 27:
        globalmin = 0
        problem = levy
        bounds = [-10 * np.ones([20, 1]), 10 * np.ones([20, 1])]
    elif n == 28:
        globalmin = 0
        problem = matyas
        bounds = [-8 * np.ones([2, 1]), 12.5 * np.ones([2, 1])]
    elif n == 29:
        globalmin = -1.80130341008983
        problem = mich
        bounds = [0 * np.ones([2, 1]), np.pi * np.ones([2, 1])]
    elif n == 30:
        globalmin = -4.687658179
        problem = mich
        bounds = [0 * np.ones([5, 1]), np.pi * np.ones([5, 1])]
    elif n == 31:
        globalmin = -9.66015
        problem = mich
        bounds = [0 * np.ones([10, 1]), np.pi * np.ones([10, 1])]
    elif n == 32:
        globalmin = 0
        problem = perm
        bounds = [-4 * np.ones([4, 1]), 4 * np.ones([4, 1])]
    elif n == 33:
        globalmin = 0
        problem = powell
        bounds = [-4 * np.ones([4, 1]), 5 * np.ones([4, 1])]
    elif n == 34:
        globalmin = 0
        problem = powell
        bounds = [-4 * np.ones([12, 1]), 5 * np.ones([12, 1])]
    elif n == 35:
        globalmin = 0
        problem = powell
        bounds = [-4 * np.ones([24, 1]), 5 * np.ones([24, 1])]
    elif n == 36:
        globalmin = 0
        problem = powell
        bounds = [-4 * np.ones([48, 1]), 5 * np.ones([48, 1])]
    elif n == 37:
        globalmin = 0
        problem = powersum
        bounds = [0 * np.ones([4, 1]), 5 * np.ones([4, 1])]
    elif n == 38:
        globalmin = 0
        problem = rast
        bounds = [-4.1 * np.ones([2, 1]), 6.4 * np.ones([2, 1])]
    elif n == 39:
        globalmin = 0
        problem = rast
        bounds = [-4.1 * np.ones([5, 1]), 6.4 * np.ones([5, 1])]
    elif n == 40:
        globalmin = 0
        problem = rast
        bounds = [-4.1 * np.ones([10, 1]), 6.4 * np.ones([10, 1])]
    elif n == 41:
        globalmin = 0
        problem = rast
        bounds = [-4.1 * np.ones([20, 1]), 6.4 * np.ones([20, 1])]
    elif n == 42:
        globalmin = 0
        problem = rosen
        bounds = [-5 * np.ones([2, 1]), 10 * np.ones([2, 1])]
    elif n == 43:
        globalmin = 0
        problem = rosen
        bounds = [-5 * np.ones([5, 1]), 10 * np.ones([5, 1])]
    elif n == 44:
        globalmin = 0
        problem = rosen
        bounds = [-5 * np.ones([10, 1]), 10 * np.ones([10, 1])]
    elif n == 45:
        globalmin = 0
        problem = rosen
        bounds = [-5 * np.ones([20, 1]), 10 * np.ones([20, 1])]
    elif n == 46:
        globalmin = 0
        problem = schw
        bounds = [-500 * np.ones([2, 1]), 500 * np.ones([2, 1])]
    elif n == 47:
        globalmin = 0
        problem = schw
        bounds = [-500 * np.ones([5, 1]), 500 * np.ones([5, 1])]
    elif n == 48:
        globalmin = 0
        problem = schw
        bounds = [-500 * np.ones([10, 1]), 500 * np.ones([10, 1])]
    elif n == 49:
        globalmin = 0
        problem = schw
        bounds = [-500 * np.ones([20, 1]), 500 * np.ones([20, 1])]
    elif n == 50:
        globalmin = -10.1531996790582
        problem = shekel5
        bounds = [[0, 10], [0, 10], [0, 10], [0, 10]]
    elif n == 51:
        globalmin = -10.4029405668187
        problem = shekel7
        bounds = [[0, 10], [0, 10], [0, 10], [0, 10]]
    elif n == 52:
        globalmin = -10.5364098166920
        problem = shekel10
        bounds = [[0, 10], [0, 10], [0, 10], [0, 10]]
    elif n == 53:
        globalmin = -186.730908831024
        problem = shub
        bounds = [[-10, 10], [-10, 10]]
    elif n == 54:
        globalmin = 0
        problem = sphere
        bounds = [-4.1 * np.ones([2, 1]), 6.4 * np.ones([2, 1])]
    elif n == 55:
        globalmin = 0
        problem = sphere
        bounds = [-4.1 * np.ones([5, 1]), 6.4 * np.ones([5, 1])]
    elif n == 56:
        globalmin = 0
        problem = sphere
        bounds = [-4.1 * np.ones([10, 1]), 6.4 * np.ones([10, 1])]
    elif n == 57:
        globalmin = 0
        problem = sphere
        bounds = [-4.1 * np.ones([20, 1]), 6.4 * np.ones([20, 1])]
    elif n == 58:
        globalmin = 0
        problem = sum2
        bounds = [-8 * np.ones([2, 1]), 12.5 * np.ones([2, 1])]
    elif n == 59:
        globalmin = 0
        problem = sum2
        bounds = [-8 * np.ones([5, 1]), 12.5 * np.ones([5, 1])]
    elif n == 60:
        globalmin = 0
        problem = sum2
        bounds = [-8 * np.ones([10, 1]), 12.5 * np.ones([10, 1])]
    elif n == 61:
        globalmin = 0
        problem = sum2
        bounds = [-8 * np.ones([20, 1]), 12.5 * np.ones([20, 1])]
    elif n == 62:
        globalmin = -50
        problem = trid
        bounds = [-36 * np.ones([6, 1]), 36 * np.ones([6, 1])]
    elif n == 63:
        globalmin = -50
        problem = trid
        bounds = [-100 * np.ones([10, 1]), 100 * np.ones([10, 1])]
    elif n == 64:
        globalmin = 0
        problem = zakh
        bounds = [-5 * np.ones([2, 1]), 10 * np.ones([2, 1])]
    elif n == 65:
        globalmin = 0
        problem = zakh
        bounds = [-5 * np.ones([5, 1]), 10 * np.ones([5, 1])]
    elif n == 66:
        globalmin = 0
        problem = zakh
        bounds = [-5 * np.ones([10, 1]), 10 * np.ones([10, 1])]
    elif n == 67:
        globalmin = 0
        problem = zakh
        bounds = [-5 * np.ones([20, 1]), 10 * np.ones([20, 1])]

    return problem, bounds, globalmin
