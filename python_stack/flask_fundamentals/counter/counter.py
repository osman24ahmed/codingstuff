from flask import Flask, render_template,session, redirect, request
app = Flask(__name__)
app.secret_key="dd"

# if session.counter:
#     session.counter+=1
# else:
#     session.counter 
#     session.counter = 0

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] += 0
   
    session['counter'] += 1    
    return render_template('index.html',counter=session['counter'])

@app.route('/add')
def add2():

    if not 'counter' in session:
        session['counter'] += 0
    
    session['counter'] += 2
    return redirect ('/')

@app.route('/reset')
def reset():
    if 'counter' in session:
        session['counter']=0
    return redirect('/')

    
app.run(debug=True)