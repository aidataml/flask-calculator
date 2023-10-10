# Put your app in here.
from flask import Flask, request
from operations import mult, div, add, sub
app = Flask(__name__)

@app.route("/mult")
def do_mult():
    """Multiply: a * b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide: a / b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

@app.route("/add")
def do_add():
    """Add: a + b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract: a - b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

operators = {"mult": mult, "div": div, "add": add, "sub": sub}

@app.route("/math/<oper>")
def do_math(oper):
    """Multiply, divide, add or subtract a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


