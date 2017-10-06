from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    if color == "purple":
        return render_template('')
    elif color == "blue":
        return render_template('')
    elif color == "red":
        return render_template('')
    elif color == "orange":
        return render_template('')
    return render_template('april.html')
    


app.run(debug=True)