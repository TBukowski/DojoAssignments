from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_secret'

@app.route('/')
def index():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

    return render_template('index.html')

@app.route('/ninja')
def add_two():
    session['counter'] += 1

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()

    return redirect(url_for('index'))

app.run(debug=True)