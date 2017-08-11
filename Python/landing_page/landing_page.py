from flask import Flask, render_template, request, redirect
# from wtforms import StringField, Form

app = Flask(__name__)

@app.route('/')

def landing_page():
    return render_template('index.html')

@app.route('/ninjas', methods=['GET'])
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos', methods=['GET'])
def dojos():
    return render_template('dojos.html')

# class myForm(Form):
#     fn = StringField('fname')

@app.route('/dojos/new', methods=['POST'])
def dojos_new():
    # projectpath = request.form['fname']
    # return render_template('submitted.html') #DO NOT USE RENDER TEMPLATE IN POST REQUEST

@app.route('/submitted', methods=['GET'])
def submit():
    return render_template('submitted.html')
app.run(debug=True)