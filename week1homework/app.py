from flask import Flask, render_template, request
from sympy import symbols, sympify
import numpy as np

x = symbols('x')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expression = request.form['expression']
        return render_template("home.html", expression=expression)

if __name__ == "__main__":
    app.run(debug=True)