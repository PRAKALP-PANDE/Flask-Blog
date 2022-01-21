from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def emp():
    return "this is landing page"

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)