from flask import Flask, render_template,request,flash,session,redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def defaultpage():
    return render_template("index.html")

@app.route('/result',methods=['POST'])
def resultpage():
    if len(request.form['name'])<1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comment'])<1 or len(request.form['comment'])>120:
        flash("Comment cannot be empty and longer than 120 characters!")
        return redirect('/')
    data=[]
    data.append(request.form['name'])
    data.append(request.form['location'])
    data.append(request.form['language'])
    data.append(request.form['comment'])
    # data={}
    # data['name']=request.form['name']
    # data['location']=request.form['location']
    # data['language']=request.form['language']
    # data['comment']=request.form['comment']
    print data
    # return render_template('result.html')
    return render_template('result.html',info=data)

app.run(debug=True)                       # Run the app in debug mode.
