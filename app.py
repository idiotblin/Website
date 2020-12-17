from flask import Flask
from random import randint
import requests, json

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
def task1_i_will_not():
    s = "<li>I will not waste time</li>\n" * 100
    return f'<ul id=blackboard>{s}</ul>'


@app.route('/task2/avito/<city>/<category>/<ad>/')
def task2_avito(city, category, ad):
    s = f'''<h1>debug info</h1>
    <p>city={city} category={category} ad={ad}</p>
    <h1>{ad.replace('_', ' ')}</h1>
    <p>{city} {category} {ad}</p>
    '''
    return s


@app.route('/task2/cf/profile/<username>/')
def task2_cf(username):
    info = json.loads(requests.get(f'https://codeforces.com/api/user.info?handles={username}').text)
    if info['status'] != 'OK':
        return 'User not found'
    else:
        s = f'''<table id=stats border="1">
        <tr>
        <td>User</td>
        <td>Rating</td>
        </tr>
        <tr>
        <td>{username}</td>
        <td>{info["result"][0]["rating"]}</td>
        </tr>
        </table>'''
        return s


def numIntoWords(num):
    a = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    b = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    c = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    ans = ""
    if num == 0:
        ans += "zero"
    ans += a[num // 100]
    if num >= 100:
        ans += " hundred "
    num -= num // 100 * 100
    if num >= 20:
        ans += b[num // 10] + " "
        num -= num // 10 * 10
    elif num >= 10:
        ans += c[num - 10] + " "
        num = 0
    ans += a[num] + " "
    return ans.strip()


@app.route('/task2/num2words/<int:num>/')
def task2_num(num):
    if 0 <= num < 1000:
        res = {"status": "OK", "number": num, "isEven": num % 2 == 0, "words": numIntoWords(num)}
    else:
        res = {"status": "FAIL"}
    return f'{json.dumps(res)}'
