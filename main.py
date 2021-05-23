from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(debug=True)
