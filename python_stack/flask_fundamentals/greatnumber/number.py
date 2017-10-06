from flask import Flask, render_template, session, request, redirect
import random
app= Flask(__name__)
app.secret_key='asdf'


@app.route('/')
def index():
    if 'secret' not in session:
        session['secret']=random.randrange(1,101)
    return render_template('/index.html')
    
@app.route('/guess', methods=['POST'])
def guess():
   
    guess = int(request.form['guess'])
    secret = session['secret']
    
    if guess < secret:
        result = 'Too Low'
    elif guess > secret:
        result = 'Too High'
    else:
        result = 'you win!'

    session['result'] = result
    return redirect('/')

 

app.run(debug=True)