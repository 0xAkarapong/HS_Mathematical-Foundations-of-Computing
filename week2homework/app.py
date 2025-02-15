import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.interpolate import lagrange

def solve_sle_interpolation(x_values, y_values) :
    n = len(x_values)
    A = np.zeros((n, n))
    for i in range(n) :
        for j in range(n) :
            A[i, j] = x_values[i] ** j

    coefficents = np.linalg.solve(A, y_values)
    return np.poly1d(coefficents[::-1]) #revert

def lagrange_interpolation(x_values, y_values   ) :
    return lagrange(x_values, y_values)

def parabola_interpolation(x_values, y_values) :
    t_values = np.arange(len(x_values))
    x_poly = lagrange(t_values, x_values)
    y_poly = lagrange(t_values, y_values)
    return x_poly, y_poly

def plot_polynomial(x_values, y_values) :
    pass

def get_function_input() :
    pass

def get_file_input() :
    pass