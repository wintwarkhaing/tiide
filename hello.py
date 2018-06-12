from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/tiide")
def tiide():
    return "Welcome to Computere University!"

