from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "colty1"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=["POST"])
def submit_post():
    errors = False

    if len(request.form['name']) < 1:
        errors = True
        flash("Name can't be blank!")
    if len(request.form['comment']) < 1:
        errors = True
        flash("Please add comments!")
        print len(request.form)
    if len(request.form['comment']) > 120:
        errors = True
        flash("Comments can't be more than 120 characters")
    if errors:
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def showResult():
    return render_template('result.html')


app.run(debug=True)
