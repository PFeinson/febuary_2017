from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"



gold = 0
activities = ""
ranNum = 0

@app.route("/")
def index():
    if "gold" not in session:
        session['gold'] = gold
    if "activities" not in session:
        session['activities'] = activities
    #content = {'gold': session['gold'], 'activities': session['activities']} 
    return render_template("index.html", gold=session['gold'], activities=session['activities'])
@app.route("/process_money", methods=['POST'])
def create_user(gold=gold):
    if "gold" not in session:
        session['gold'] = gold
    if "activities" not in session:
        session['activities'] = activities
        
    if request.form['action'] == "farm":
        ranNum = random.randint(9, 21)
        session['gold'] = session['gold'] + ranNum
        session['activities'] += "<p class = 'green'>" + "Earned " + str(ranNum) + " gold. You have a total of " + str(session['gold']) + "</p>"
    elif request.form['action'] == "cave":
        ranNum = random.randint(4, 11)
        session['gold'] = session['gold'] + ranNum
        session['activities'] += "<p class = 'green'>" + "Earned " + str(ranNum) + " gold. You have a total of " + str(session['gold']) + "</p>"
    elif request.form['action'] == "house":
        ranNum = random.randrange(1, 6)
        session['gold'] = session['gold'] + ranNum
        session['activities'] += "<p class = 'green'>" + "Earned " + str(ranNum) + " gold. You have a total of " + str(session['gold']) + "</p>"
    elif request.form['action'] == "casino":
        ranNum = random.randrange(0, 11)
        if (ranNum % 2 == 0):
            ranNum = random.randrange(0, 50)
            session['gold'] = session['gold'] + ranNum
            session['activities'] += "<p class = 'green'>" + "Earned " + str(ranNum) + " gold. You have a total of " + str(session['gold']) + "</p>"
        else:
            ranNum = random.randrange(0, 50)
            session['gold'] = session['gold'] - ranNum
            session['activities'] += "<p class = 'red'>" + "Lost " + str(ranNum) + " gold. You have a total of " + str(session['gold']) + "</p>"
    
    
    activities = session['activities']
    gold = session['gold']
    return redirect("/")

@app.route("/reset")
def reset():
    session['gold'] = 0
    session['activities'] = ""
    return redirect("/")

app.run(debug=True)