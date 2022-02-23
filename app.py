from flask import Flask  # Used to Start the app with app = Flask(__name__)
from flask import request, redirect  # request is used to read passed parameters, redirect does what it sounds like
from flask import url_for  # a tool to read out the path of functions (example index())
from markupsafe import escape  # used to protect from injection scripts by converting into string before execution
from config import env  # set environment variable based on where the application is running
# from flask_talsiman import Talisman  # another way to secure SSL, recommended by the flask documentation, needs study

app = Flask(__name__)
app.env = env  # set app environment to the config environment
# Talisman(app)


@app.before_request
def before_request():  # this function checks env, if dev allows http (for testing with postman)
    if app.env == "Development":
        return
    if request.is_secure:
        return

    url = request.url.replace("http://", "https://", 1)
    code = 301
    return redirect(url, code=code)



@app.route("/")
def index():
    return "Welcome to the index page!"


@app.route("/hi")
def who():
    return "Who are you?"


@app.route("/hi/")
def greet():
    username = request.args.get('username', default='default value', type=str)
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
    with open('example-text-test.txt') as f:
        lines = f.readlines()  # comes back as a list which is why we join with spaces between on the line below
    return ' '.join(lines)


def do_the_get():
    return 'This is a get test after a 3.10.2 update'


with app.test_request_context():  # could be used in a index page for route options maybe?
    print(url_for('index'))
    print(url_for('who'))
    print(url_for('greet', username='John Doe'))
    print(url_for('whatever'))
