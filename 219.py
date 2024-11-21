from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/names')
def names():
    return "Vladi, Elior, tal (the favorite)"

app.run()

