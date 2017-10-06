from flask import Flask, render_template,
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', add="index")

@app.route('/ninja')
def ninja():
    return render_template('index.html', add="ninja1")


@app.route('/ninja/<color>')
def ninjas(color):
    return render_template('index.html', color=color)

app.run(debug=True)


