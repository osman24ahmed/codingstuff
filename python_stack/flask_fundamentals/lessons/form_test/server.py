from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Thisis Secret'
@app.route('/users/<username>', methods=['POST'])
def show_user_profile(username):
    print username
    return render_template('user.html')

@app.route('/show')
def show_user():
    return render_template('user.html', name ='jat', email ='klajs@gmail.com')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print 'Got Post Info'
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    name = request.form['name']
    email = request.form['email']
    return redirect('/')
app.run(debug=True)

