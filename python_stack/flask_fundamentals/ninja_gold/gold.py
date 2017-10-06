from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime
app= Flask(__name__)
app.secret_key='kljsda'

@app.route('/')
def index():
    if not 'activities' in session:
        session['activities'] = []

    if not 'gold' in session:
        session['gold']=0
    return render_template('index.html',)
    # if not 'counter' in session:
    #     session['counter'] += 0
    # session['counter'] += 1    
    # return render_template('index.html',counter=session['counter'])

# @app.route('/process_money', methods=['POST'])
# def process():
#     return render_template('index.html')

@app.route('/process_money',methods=['POST','GET'])
def farm():  

    timestamp = datetime.now().strftime('%m/%d/%Y %-I:%M%p')

    if request.form['building']== 'farm':
       new_gold = random.randrange(10,21)
       info = "Earned {} from the farm ({})".format(new_gold,timestamp)
        
    if request.form['building'] =='cave':
       new_gold = random.randrange(5,10)
       info =  "Earned {} from the cave ({})".format(new_gold,timestamp)

    if request.form['building'] =='house':
       new_gold = random.randrange(2,6)
       info = "Earned {} from the house ({})".format(new_gold,timestamp)

    if request.form['building'] =='casino':
        new_gold = random.randrange(-51,51)
        if new_gold < 0:
            info = "Entered a casino and lost {} golds...Ouch ({})".format(new_gold,timestamp)
        else:
            info = "Earned {} from the casino ({})".format(new_gold,timestamp)
    
    session['activities'].insert(0,info,)
    
    session['gold']+=new_gold
    print session['gold']
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    




app.run(debug=True)
