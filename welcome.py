from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    args = request.args;

    if (args and "username" in args.keys()):
        return "Welcome "+ args["username"]
    else:
        return "Sample valid url: \?username=todd"