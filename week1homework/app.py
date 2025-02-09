from flask import Flask, render_template, request
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

app = Flask(__name__)

def bisection_method(f, a, b, tolerance, max_iterations=100):
    if f(a) * f(b) >= 0:
        return None, 0, []
    
    errors = list()
    for i in range(max_iterations):
        c = (a + b) / 2
        error = abs(b - a) / 2
        errors.append(error)
        if f(c) == 0 or (b - a) / 2 < tolerance:
            return c, i, errors
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, max_iterations, errors

def newton_raphson_method(f, x0, tolerance, max_iterations=100):
    errors = list()
    for i in range(max_iterations):
        x1 = x0 - f(x0) / f(x).diff(x).subs(x, x0)
        error = abs(x1 - x0)
        errors.append(error)
        if error < tolerance:
            return x1, i, errors
        x0 = x1
    return x1, max_iterations, errors

@app.route("/")
def index():
    render_template('index.html')

@app.route("calculate", methods=['POST'])
def calculate():
    # Input Part
    if request.method == 'POST':
        function_str = request.form['function']
        a_str = request.form['interval_a']
        b_str = request.form['interval_b']
        tolerance_str = request.form['tolerance']

        # Convert a b and tolerance to float
        a = float(a_str)
        b = float(b_str)
        tolerance = float(tolerance_str)
        del a_str, b_str, tolerance_str

        # Check if the input is valid
        if b >= a:
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
        plt.figure(figsize=(8, 6)
        plt.plot(newton_errors, label="Newton-Raphson")
        plt.plot(bisection_errors, label="Bisection")
        plt.xlabel("Iteration")
        plt.ylabel("Error (Log Scale)")
        plt.yscale("log")
        plt.title("Convergence Comparison")
        plt.grid(True)

        # Image Part
        img =  BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')


    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)