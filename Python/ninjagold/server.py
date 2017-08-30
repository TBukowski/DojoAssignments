import random
from datetime import datetime
from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_secret'

@app.route('/')
def index():
    if 'ninja_gold' not in session:
        session['ninja_gold'] = 0
        session['jobs'] = [] #made an empty list to store ninja's gold transaction
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():#put session['jobs'] in a variable?

    date =datetime.now().strftime('%Y/%m/%d %X %p')
    if request.form['building'] == 'farm':
        gold = random.randint(10, 20)
        session['ninja_gold'] += gold
        session['jobs'].append("Earned {} gold from the {}! ({})".format(str(gold), 'farm', date))
    if request.form['building'] == 'cave':
        gold = random.randint(5, 10)
        session['ninja_gold'] += gold
        session['jobs'].append("Earned {} gold from the {}! ({})".format(str(gold), 'farm', date))

    if request.form['building'] == 'house':
        gold = random.randint(2, 5)    
        session['ninja_gold'] += gold
        session['jobs'].append("Earned {} gold from the {}! ({})".format(str(gold), 'farm', date))

    if request.form['building'] == 'casino':
        gold = random.randint(-50, 50)    
        session['ninja_gold'] += gold
        if gold > 0:
            session['jobs'].append("Earned {} gold from the {}! ({})".format(str(gold), 'farm', date))

        else:
            session['jobs'].append("Earned {} gold from the {}! ({})".format(str(gold), 'farm', date))

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('ninja_gold')
    session.pop('jobs')
    return redirect(url_for('index'))

app.run(debug=True)