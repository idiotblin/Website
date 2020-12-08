from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
@app.route('/haba')
def hello_world():
    s = '''Hello, Haba!
           Hello, Arsen!
           Hello, Karim!'''
    out = "<pre>{}</pre>".format(s)
    return out


@app.route('/task1/random')
def solve1():
    r = randint(1, 5)
    s = "Haba's mark is " + str(r)
    out = "<pre>{}</pre>".format(s)
    return out
