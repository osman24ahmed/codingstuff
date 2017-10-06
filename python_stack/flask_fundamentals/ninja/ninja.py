from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',img="index")

@app.route('/ninja')
def ninjas():
    return render_template('index.html',img="ninjas")

@app.route('/ninja/<color>')
def leo(color):
    return render_template('index.html',color=color)




app.run(debug=True)