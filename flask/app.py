from flask import Flask
from random import randrange

app = Flask(__name__)

@app.route('/number')
def number():
    return str(randrange(9))