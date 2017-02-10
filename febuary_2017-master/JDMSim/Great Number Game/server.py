import random
from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)
app.secret_key='my_secret'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randrange(0, 101)
    print session['num']
    return render_template('index.html')

@app.route('/numberIN', methods=['POST'])
def compare_number():
    session['guess']= int(request.form['guess'])
    if session['guess'] > session['num']:
        session['res']='high'
    elif session['guess'] < session['num']:
        session['res']='low'
    elif session['guess'] == session['num']:
        session['res']='per'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
    

app.run(debug=True)    