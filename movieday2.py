import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sqrt(x)

def bisection(a, b, iterations=1000, tolerance=1e-6):
    if f(a) * f(b) >= 0:
        return None

    for _ in range(iterations):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return None