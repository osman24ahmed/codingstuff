from flask import Flask, render_template, redirect, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'no no no'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods = ['POST'])
def result():
    errors=[]
    if len(request.form['email']) < 1:
        errors.append("please enter your email")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['password']) < 1:
        errors.append("please enter a passwod")
    if len(request.form['password']) < 8:
        errors.append('password must contain at least 8 characters')
    if len(request.form['first_name']) < 1:
        errors.append("please enter your first name")
    if not request.form['first_name'].isalpha():
        errors.append('First Name must only contain letters')
    if len(request.form['last_name']) < 1:
        errors.append("please enter your last name")
    if not request.form['last_name'].isalpha():
        errors.append('Last Name must only contain letters')
    if len(request.form['confirm_password']) < 1:
        errors.append("please confirm your password")
    if len(request.form['confirm_password']) < 8:
        errors.append('password must contain at least 8 characters')
    if not request.form['password'] == request.form['confirm_password']:
        errors.append('password dont match bro')
        
    if errors:
        print errors
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        return "thank you come again"
app.run(debug=True)