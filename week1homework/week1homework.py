from flask import Flask
import sympy as sym
from pygments.lexers import templates

app = Flask(__name__)

@app.route("/")
def index():
    return templates.render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)