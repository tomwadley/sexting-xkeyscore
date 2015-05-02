from web import app
from flask import render_template, request
from sexting.sexting import Sexting

@app.route('/')
def message_input():
    return render_template('message_input.html')

@app.route('/transform', methods=['POST'])
def transform():
    message = request.form['message']
    instructions = __transform(message)
    return render_template('instructions.html', instructions=instructions)

def __transform(message):
    instructions = Sexting(message, 11).process()
    return list(instructions)
