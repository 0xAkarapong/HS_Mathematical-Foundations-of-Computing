from flask import Flask, render_template, request
from sympy import symbols, sympify
import numpy as np

x = symbols('x')

app = Flask(__name__)

def bisection_method():
    pass

def newton_raphson_method():
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


if __name__ == "__main__":
    app.run(debug=True)