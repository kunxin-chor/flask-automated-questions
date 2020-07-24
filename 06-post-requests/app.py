from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.template.html')

@app.route('/', methods=['POST'])
def processHello():
    # complete this route here
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    return render_template('process-hello.template.html', fn=first_name, ln=last_name)

@app.route('/calculate')
def calculate():
    return render_template('calculate.template.html')

@app.route('/calculate', methods=['POST'])
def processCalculate():
    number1 = request.form['number1']
    number2 = request.form['number2']
    total = int(number1) + int(number2)
    return render_template('process-calculate.template.html', answer=total)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)