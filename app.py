from flask import Flask

app = Flask('hello_world')

@app.route("/")
def home():
    return "Hello World"