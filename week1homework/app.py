from flask import Flask, render_template, request
from sympy import symbols, sympify
import numpy as np

x = symbols('x')

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

def newton_raphson_method(f, a, b, tolerance, max_iterations=100):
    pass

def get_expression(expression):
    return sympify(expression)

@app.route("/")
def index():
    render_template('home.html')

@app.route("calculate", methods=['POST'])
def calculate():
    # Input Part
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
        return "Interval a must be less than b"
    if tolerance <= 0:
        return "Tolerance must be greater than 0"


if __name__ == "__main__":
    app.run(debug=True)