from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    args = request.args;

    return "Welcome "+ args["username"]