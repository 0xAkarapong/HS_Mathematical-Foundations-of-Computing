import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from sympy import Symbol, lambdify, parse_expr

def solve_sle(x_values, y_values) :
    n = len(x_values)
    A = np.zeros((n, n))
    for i in range(n) :
        for j in range(n) :
            A[i, j] = x_values[i] ** j

    coefficents = np.linalg.solve(A, y_values)
    return np.poly1d(coefficents[::-1]) #revert

def lagrange_interpolation(x_values, y_values   ) :
    return lagrange(x_values, y_values)

def parametric_interpolation(x_values, y_values) :
    t_values = np.arange(len(x_values))
    x_poly = lagrange(t_values, x_values)
    y_poly = lagrange(t_values, y_values)
    return x_poly, y_poly

def plot_polynomials(polynomials, x_values, y_values, interval, labels) :
    plt.figure(figsize=(12, 8))
    plt.scatter(x_values, y_values, color='black', label='Original Points', zorder=5)
    x_plot = np.linspace(interval[0], interval[1], 400)
    for i, poly in enumerate(polynomials):
        if isinstance(poly, tuple):  # Parametric case
            t_plot = np.linspace(0, len(x_values) - 1, 400)  # t for parametric
            plt.plot(poly[0](t_plot), poly[1](t_plot), label=labels[i])
        else:
            plt.plot(x_plot, poly(x_plot), label=labels[i])

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interpolation Polynomials')
        plt.legend()
        plt.grid(True)
        plt.show()

def calculate_polynomial_value(polynomials, x, labels):
    print(f"Values at x = {x}:")
    for i, poly in enumerate(polynomials):
        if isinstance(poly, tuple):  # Parametric
            t_values = np.arange(len(x_values))
            closest_t_index = np.argmin(np.abs(poly[0](t_values) - x))
            closest_t = t_values[closest_t_index]

            print(
                f"  {labels[i]}:  x(t) ≈ {poly[0](closest_t):.4f}, y(t) ≈ {poly[1](closest_t):.4f}  (using approximate t ≈ {closest_t:.4f})")


        else:
            print(f"  {labels[i]}: {poly(x):.4f}")

def main():
    """Main function to handle user input and run the interpolation."""

    print("Interpolation Experimentation Tool")

    # Input Method Selection
    while True:
        input_method = input("Choose input method: (1) Function, (2) File: ")
        if input_method in ('1', '2'):
            break
        print("Invalid input method. Please enter 1 or 2.")

    # Input Processing
    if input_method == '1':  # Function Input
        while True:
            try:
                function_str = input("Enter the function (e.g., x*np.sin(x) - x**2 + 1): ")
                x_sym = Symbol('x')
                function_expr = parse_expr(function_str, local_dict={'x': x_sym, 'np': np})
                function = lambdify(x_sym, function_expr, "numpy") # Convert to a callable function
                break
            except (SyntaxError, TypeError, NameError) as e:
                print(f"Invalid function expression: {e}.  Please use valid Python/NumPy syntax.")
                print("Example of a valid expression: x*np.sin(x) - x**2 + 1")


        while True:
            try:
                interval_str = input("Enter the interval [a, b] (e.g., 0, 2): ")
                interval = tuple(map(float, interval_str.split(',')))
                if len(interval) != 2 or interval[0] >= interval[1]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid interval.  Enter two numbers separated by a comma, with a < b.")

        while True:
            try:
                degree = int(input("Enter the polynomial degree: "))
                if degree < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid degree. Please enter a non-negative integer.")

        # Generate points from the function
        num_points = degree + 1
        x_values = np.linspace(interval[0], interval[1], num_points)
        y_values = function(x_values)

    else:  # File Input
        while True:
            filename = input("Enter the filename of the points (e.g., points.txt): ")
            try:
                with open(filename, 'r') as file:
                    points = []
                    for line in file:
                        x, y = map(float, line.strip().split(','))
                        points.append((x, y))
                x_values, y_values = zip(*points)  # Unzip into separate x and y lists
                x_values = np.array(x_values)
                y_values = np.array(y_values)
                
                if len(x_values) < 2:
                    raise ValueError("At least two points are required.")
                break
            except (FileNotFoundError, ValueError) as e:
                print(f"Error reading file: {e}.  Ensure the file exists and contains comma-separated pairs of numbers.")

        interval = (min(x_values), max(x_values)) # Plotting range based on points in file.

    #  Method Selection
    print("Select interpolation methods:")
    print("1. Solve SLE")
    print("2. Lagrange")
    print("3. Parametric (Lagrange)")

    while True:
        methods_str = input("Enter the methods to use (comma-separated, e.g., 1,2): ")
        try:
            selected_methods = list(map(int, methods_str.split(',')))
            if not all(1 <= m <= 3 for m in selected_methods):
                raise ValueError
            break
        except ValueError:
            print("Invalid method selection. Enter numbers between 1 and 3, separated by commas.")
    
    labels = []
    polynomials = []
    if 1 in selected_methods:
        polynomials.append(solve_sle(x_values, y_values))
        labels.append("SLE")
    if 2 in selected_methods:
        polynomials.append(lagrange_interpolation(x_values, y_values))
        labels.append("Lagrange")
    if 3 in selected_methods:
        polynomials.append(parametric_interpolation(x_values, y_values))
        labels.append("Parametric (Lagrange)")

    # Plotting
    plot_polynomials(polynomials, x_values, y_values, interval, labels)

    # Value Calculation
    while True:
        try:
            x_input = input("Enter an x value to evaluate the polynomials (or 'q' to quit): ")
            if x_input.lower() == 'q':
                break
            x = float(x_input)
            if not interval[0] <= x <= interval[1]:
                print(f"Warning: x = {x} is outside the interpolation interval {interval}.")

            calculate_polynomial_value(polynomials, x, labels)
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")



if __name__ == "__main__":
    main()