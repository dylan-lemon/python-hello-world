from flask import Flask
from flask import request
from flask import url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the index page!"


@app.route("/hi/")
def who():
    return "Who are you?"


@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {escape(username)}!"


@app.route("/autoDeployTest/")
def deployed():
    return "This was added after saving"


@app.route("/caleb/")
def whatever():
    return "Hi Caleb"


@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return do_the_post()
    else:
        return do_the_get()


def do_the_post():
    return 'This is a post test'


def do_the_get():
    return 'This is a get test'


with app.test_request_context():  # could be used in a index page for route options maybe?
    print(url_for('index'))
    print(url_for('who'))
    print(url_for('greet', username='John Doe'))
    print(url_for('whatever'))
