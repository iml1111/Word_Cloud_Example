# routes.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')

a = 1

if __name__ == '__main__':
	app.run(debug = True)