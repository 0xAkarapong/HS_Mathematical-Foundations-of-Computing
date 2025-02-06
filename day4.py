# Newton's method
import numpy as np

def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        dx = -f(x) / df(x)
        x = x + dx
        if abs(dx) < tol:
            break
    return x, i + 1, abs(dx) < tol

def f1(x):
    return x**2 - 5 * x

def df1(x):
    return 2 * x - 5

x0_1 = 0.0
tolerance_1 = 1e-6
max_iterations_1 = 100

root_1, iterations_1, converged_1 = newton(f1, df1, x0_1, tolerance_1, max_iterations_1)
print("Function 1:")
print(f"Root: {root_1}")
print(f"Iterations: {iterations_1}")
print(f"Converged: {converged_1}")


def f2(x):
    return np.sqrt(x)

def df2(x):
    return 1 / (2 * np.sqrt(x))

x0_2 = 1.0
tolerance_2 = 1e-6
max_iterations_2 = 100

root_2, iterations_2, converged_2 = newton(f2, df2, x0_2, tolerance_2, max_iterations_2)
print("\nFunction 2:")
print(f"Root: {root_2}")
print(f"Iterations: {iterations_2}")
print(f"Converged: {converged_2}")