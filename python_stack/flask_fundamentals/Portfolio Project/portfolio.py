from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def local():
    return render_template('index.html')

@app.route('/projects')
def pro():
    return render_template('projects.html')

@app.route('/about')
def aboutme():
    return render_template('about.html')
app.run(debug=True)