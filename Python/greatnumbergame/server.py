import random
from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_secret'

@app.route('/')
def index():
    if 'randnum' not in session:
        session['randnum'] = random.randint(1, 101)
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    guess = int(request.form['guess'])
    if guess < session['randnum']:
        session['guess'] = 'too_low'
    elif guess > session['randnum']:
        session['guess'] = 'too_high'
    else:
        session['guess'] = 'correct'

    # print 'You guessed:', request.form['guess']
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

app.run(debug=True)
