from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def menu():
    s = "<li><a href='/task1/random/'>/task1/random/</a></li>\n" \
        "<li><a href='/task1/i_will_not/'>/task1/i_will_not/</a></li>"
    return f'<ul id=menu>{s}</ul>'


@app.route('/haba/')
def hello_world():
    s = ['Hello, Haba!',
         'Hello, Arsen!',
         'Hello, Karim!']
    out = "<pre>{}</pre>".format("\n".join(s))
    return out


@app.route('/task1/random/')
def task1_random():
    r = randint(1, 5)
    s = "Haba's mark is " + str(r)
    out = "<pre>{}</pre>".format(s)
    return out


@app.route('/task1/i_will_not/')
def task1_iWillNot():
    s = "<li>I will not waste time</li>\n" * 100
    return f'<ul id=blackboard>{s}</ul>'
