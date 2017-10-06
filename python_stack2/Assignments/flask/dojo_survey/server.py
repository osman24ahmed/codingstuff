from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods =["POST"])
def result():
    name = request.form['name']
    dojo = request.form['dojo']
    fav = request.form['fav']
    comment = request.form['comment']
    print name, dojo, fav, comment

    return render_template('result.html', name=name,dojo=dojo, fav=fav, comment=comment )

app.run(debug=True)