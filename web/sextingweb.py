from web import app
from flask import render_template, request, url_for, redirect
import os, errno, uuid
from sexting.sexting import Sexting
import pdfkit
import subprocess

@app.route('/')
def message_input():
    return render_template('message_input.html')

@app.route('/print', methods=['POST'])
def transform_and_print():
    message = request.form['message']
    url = url_for('transform', _external=True, message=message)
    output_path = __get_output_path()
    print "Generating pdf ({0}) from {1}".format(output_path, url)
    pdfkit.from_url(url, output_path)
    subprocess.Popen(['lpr', output_path])
    return redirect(url_for('message_input'))

def __get_output_path():
    output_dir = 'output'
    try:
        os.makedirs(output_dir)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(output_dir):
            pass
        else:
            raise
    return os.path.join(output_dir, str(uuid.uuid4()) + '.pdf')

@app.route('/transform')
def transform():
    message = request.args.get('message', '')
    instructions = __transform(message)
    return render_template('instructions.html', instructions=instructions)

def __transform(message):
    instructions = Sexting(message, 11).process()
    return list(instructions)

