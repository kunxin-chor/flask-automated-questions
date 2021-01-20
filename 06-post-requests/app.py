from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.template.html')

@app.route('/', methods=['POST'])
def processHello():
    # complete this route here
    pass

@app.route('/calculate')
def calculate():
    return render_template('calculate.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)