from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods = ['POST'])
def result():
    
    if len(request.form['name']) < 1:
        return "please enter your name"
    if len(request.form['comment']) < 1:
        return "please leave a comment"
    if len(request.form['comment']) > 120:
        return "please enter fewer text, no more than 120 characters"
    else:
        result = request.form
        return render_template('result.html', result=result)
app.run(debug=True)