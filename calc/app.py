from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_response():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a,b))

@app.route('/sub')
def sub_response():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a,b))

@app.route('/mult')
def mult_response():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a,b))

@app.route('/div')
def div_response():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a,b))

operation_functions = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def math_operation_response(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operation_functions.get(operation)(a,b))
    


