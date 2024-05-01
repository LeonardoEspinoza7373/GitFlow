from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Proyecto Basico'

@app.route('/suma/<int:a>/<int:b>')
def suma(a: int, b: int):
    return a + b