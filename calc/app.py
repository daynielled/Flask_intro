# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route("/add")
def add_nums():
    """Add a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = add(a,b)
    return str(total)

@app.route("/sub")
def sub_numns():
    """Subtract a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = sub(a,b)
    return str(total)

@app.route("/mult")
def mult_nums():
    """Multiply a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = mult(a,b)
    return str(total)

@app.route("/div")
def div_nums():
    """Divide a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = div(a,b)
    return str (total)



OPERATORS = {
     "add" : add,
     "sub" : sub,
     "mult" : mult,
     "div": div,
}

@app.route("/math/<operation>")
def do_math(operation):
    """Perform math operation of choice on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATORS[operation](a,b)
    return str(result)