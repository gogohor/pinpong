from flask import Flask,session
from quizz_sql import get_question
from random import randint
def index():
    session['counter'] = random(randint(1,2))
    return '<h1><a href = "/test">Start Test</a></h1>'

def test():
    data = get_question(1,2)
    return f"<h1><a href = '/'>{str(data)} </a></h1>"

def result():
    return ''

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwert123"

app.add_url_rule('/',"home",index)
app.add_url_rule('/test',"test",test)
app.add_url_rule('/result',"result",result)

app.run()