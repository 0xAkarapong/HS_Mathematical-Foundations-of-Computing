import numpy as np
import matplotlib.pyplot as plt

def f_x(x):
    return np.sin(x)

def build_vandermonde_matrix(x_points):
    m = len(x_points)
    A = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            A[i, j] = x_points[i]**j
    return A

def solve_sle(A, y_values):
    try:
        coefficients = np.linalg.solve(A, y_values)
        return coefficients
    except np.linalg.LinAlgError:
        print("Singular matrix: No unique solution exists.")
        return None

def interpolation_polynomial(x, coefficients, x_points):
    if coefficients is None:
        return np.nan
    m = len(coefficients)
    p_x = 0
    for j in range(m):
        p_x += coefficients[j] * x**j
    return p_x

def main():
 
    a = 0.0  # Start of interval
    b = np.pi # End of interval
    m = 5     # Number of interpolation points

    print("Input:")
    print(f"Function: F(x) = sin(x) (you can change f_x function)")
    print(f"Interval: [a, b] = [{a}, {b}]")
    print(f"Number of points: m = {m}")


    x_points = np.linspace(a, b, m)
    print("\n1) Calculate x_i points:")
    print(f"x_points = {x_points}")


    y_values = f_x(x_points)
    print("\n2) Calculate y_i = F(x_i):")
    print(f"y_values = {y_values}")


    A = build_vandermonde_matrix(x_points)
    print("\n3) Build SLE (Vandermonde Matrix A):")
    print("A =")
    print(A)

    coefficients = solve_sle(A, y_values)
    if coefficients is not None:
        print("\nSolve SLE and get coefficients:")
        print(f"Coefficients (a_0, a_1, ..., a_{m-1}) = {coefficients}")


        x_plot = np.linspace(a, b, 100) 
        f_x_values_plot = f_x(x_plot)
        p_x_values_plot = [interpolation_polynomial(x, coefficients, x_points) for x in x_plot]

        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, f_x_values_plot, label='F(x) = sin(x)')
        plt.plot(x_plot, p_x_values_plot, label=f'P_{m-1}(x) (Interpolation Polynomial)')
        plt.scatter(x_points, y_values, color='red', label='Interpolation Points (x_i, y_i)') 
        plt.title('Function Approximation using Interpolation Polynomial')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("\nCould not plot due to singular matrix.")


if __name__ == "__main__":
    main()