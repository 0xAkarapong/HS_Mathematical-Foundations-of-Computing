import numpy as np
import matplotlib.pyplot as plt

def build_vandermonde_matrix(x_points):
    m = len(x_points)
    A = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            A[i, j] = x_points[i] ** j
    return A

def solve_sle(A, y_values):
    try:
        coefficients = np.linalg.solve(A, y_values)
        return coefficients
    except np.linalg.LinAlgError:
        print("Singular matrix: No unique solution exists.")
        return None

def interpolation_polynomial(x, coefficients):
    if coefficients is None:
        return np.nan
    m = len(coefficients)
    p = 0
    for j in range(m):
        p += coefficients[j] * x ** j
    return p

def lagrange_interpolation(x, x_points, y_values):
    total = 0
    n = len(x_points)
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        total += term
    return total

def run_interpolation_experiment(func, func_label, a, b, m):
    x_points = np.linspace(a, b, m)
    y_values = func(x_points)
    A = build_vandermonde_matrix(x_points)
    coefficients = solve_sle(A, y_values)
    
    x_plot = np.linspace(a, b, 200)
    f_values = func(x_plot)
    p_values = np.array([interpolation_polynomial(x, coefficients) for x in x_plot])
    lagrange_values = np.array([lagrange_interpolation(x, x_points, y_values) for x in x_plot])
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_plot, f_values, label=func_label, color='blue')
    plt.plot(x_plot, p_values, label='Vandermonde Interp.', linestyle='--', color='green')
    plt.plot(x_plot, lagrange_values, label='Lagrange Interp.', linestyle=':', color='magenta')
    plt.scatter(x_points, y_values, color='red', zorder=5, label='Interpolation Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Interpolation of {func_label} on [{a}, {b}] with m = {m}')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    a = 0.0
    b = 4.0
    m = 7

    run_interpolation_experiment(np.sin, "sin(x)", a, b, m)
    run_interpolation_experiment(lambda x: np.sin(3*x), "sin(3x)", a, b, m)
    run_interpolation_experiment(lambda x: np.sin(5*x), "sin(5x)", a, b, m)

if __name__ == "__main__":
    main()