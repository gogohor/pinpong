from flask import Flask,render_template,session,request,redirect,url_for
from db_scripts import get_quises

def index():
    if request.method == "GET":
        quizz = get_quises()
        return render_template("index.html", quizz=quizz)
    else:
        session["quiz.id"] = request.form.get('quiz')
        session["qustion_id"] = 0
        return redirect(url_for("test"))

def test():
    if request.method == "POST":
        session["qustion_id"] += 1
    question = ""
    answer = ["запитання"]
    return render_template('test.html',question=question,answer=answer)

app = Flask (__name__,template_folder='', static_folder='')

app.add_url_rule("/","index",index)

app.add_url_rule("/index","index",index,methods=["POST","GET"])

app.add_url_rule("/test","test",test,methods=["POST","GET"])


app.run()