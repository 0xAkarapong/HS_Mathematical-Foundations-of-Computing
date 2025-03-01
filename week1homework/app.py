from flask import Flask, render_template, request
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


app = Flask(__name__)

def bisection_method(f, a, b, tolerance, max_iterations=100):
    if f(a) * f(b) >= 0:
        return None, -1, [] 

    errors = []
    for i in range(max_iterations):
        c = (a + b) / 2
        error = abs(b - a) / 2
        errors.append(error)
        if abs(f(c)) < 1e-15 or error < tolerance:
            return c, i + 1, errors
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return None, max_iterations, errors

def newton_raphson_method(f, df, x0, tolerance, max_iterations=100):
    errors = []
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return None, -1, []

        x1 = x - fx / dfx
        error = abs(x1 - x)
        errors.append(error)
        if error < tolerance:
            return x1, i + 1, errors
        x = x1
    return None, max_iterations, errors

@app.route("/", methods=['GET', 'POST'])
def index():
    # Input Part
    if request.method == 'POST':
        try:
            function_str = request.form['function']
            a_str = request.form['a']
            b_str = request.form['b']
            tolerance_str = request.form['tolerance']

            # Convert a b and tolerance to float
            a = float(a_str)
            b = float(b_str)
            tolerance = float(tolerance_str)

            # Check if the input is valid
            if a >= b:
                return render_template('index.html', error="Invalid interval: 'a' must be less than 'b'.")
            if tolerance <= 0:
                return render_template('index.html', error="Invalid tolerance: Tolerance must be greater then zero")

            x = sp.symbols('x')

            try:
                f_sympy = sp.sympify(function_str)
                f = sp.lambdify(x, f_sympy, 'numpy')
                df_sympy = sp.diff(f_sympy, x)
                df = sp.lambdify(x, df_sympy, 'numpy')
            except (sp.SympifyError, TypeError, ValueError) as e:
                return render_template('index.html', error=f"Invalid function: {e}")

            try:
                f(a)  # Test evaluation at interval endpoints
                f(b)
                df(a)
                df(b)
            except (ValueError, TypeError, ZeroDivisionError) as e:
                return render_template('index.html', error=f"Function evaluation error at interval endpoints: {e}")

            # Algorithm Part
            newton_root, newton_iterations, newton_errors = newton_raphson_method(f, df, (a + b) / 2, tolerance)
            bisection_root, bisection_iterations, bisection_errors = bisection_method(f, a, b, tolerance)

            # Graph plotting
            plt.figure(figsize=(8, 6))
            plt.plot(newton_errors, label="Newton-Raphson")
            plt.plot(bisection_errors, label="Bisection")
            plt.xlabel("Iteration")
            plt.ylabel("Error (Log Scale)")
            plt.yscale("log")
            plt.title("Convergence Comparison")
            plt.grid(True)
            plt.legend()

            # Image Part
            img =  BytesIO()
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            return render_template('index.html', newton_root=newton_root, newton_iterations=newton_iterations, 
                    bisection_root=bisection_root, bisection_iterations=bisection_iterations, plot_url=plot_url,
                    a_str=a_str, b_str=b_str, tolerance=tolerance_str)
        except (ValueError, TypeError) as e:
            return render_template('index.html', error=f"Input error: Please enter valid numbers.  Details: {e}")
        except Exception as e:
             return render_template('index.html', error=f"An unexpected error occurred: {e}")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)