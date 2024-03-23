from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__, template_folder='', static_folder='')

news = ['kdsfins', 'qwmdsffodsf', 'qwe121233', 'qwe123']
news_id = ['0','1','2','3']

data = [
    {
        "id": '0',
        "title": 'News',
        "content": "contetnt"
    },
    {
        "id": '1',
        "title": 'News 2',
        "content": "contetnt 2"
    }
]

@app.route("/")
def index():
    return render_template('sing-in.html', news=data)


@app.route("/home/<id>")
def home(id):
    
    for news in data:
        if news['id'] == id:
            return render_template('news.html', showed_news=news, ids=news_id)

    
    return redirect('/')


@app.route("/auth/sign-in", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect('/profile')
        else:
            session['inccorect_pass'] = True
            return redirect(url_for('signIn'))
            
    print(request.method, session['inccorect_pass'])
    if ('inccorect_pass' in session.keys()  ):
        return render_template('sign-in.html', incorrect_password=session['inccorect_pass'])
    
    return render_template('sign-in.html', incorrect_password=False)

@app.route("/auth/sign-up")
def signUp():
    return render_template('sign-in.html')

app.secret_key = 'secret'

app.run(debug=True)
