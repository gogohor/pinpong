from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nature_quiz')
def nature_quiz():
    return render_template('nature_quiz.html')

if __name__ == '__main__':
    app.run(debug=True)