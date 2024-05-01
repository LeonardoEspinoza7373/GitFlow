from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'hello world'

@app.route('/suma/<int:a>/<int:b>')
def suma(a: int, b: int):
    nums = a + b
    return f"La suma es: {str(nums)}"