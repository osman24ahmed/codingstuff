from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'passwordIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print 'got post info'

    session['name'] = request.form['name']
    session ['email'] = request.form['email']
    print request.form['name']
    print request.form['email']
    return redirect('/show')

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template('user.html')

@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])

@app.route('/process')
def process():
    if request.form['action'] == 'register':
       
    elif request.form['action'] == 'login':
       


app.run(debug=True)