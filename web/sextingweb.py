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
    __generate_pdf(url, output_path)
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

def __generate_pdf(url, output_path):
    options = {
        'page-size': 'A4',
        'margin-top': '1.27cm',
        'margin-right': '1.27cm',
        'margin-bottom': '1.27cm',
        'margin-left': '1.27cm',
        'encoding': "UTF-8",
    }
    pdfkit.from_url(url, output_path, options)

@app.route('/transform')
def transform():
    message = request.args.get('message', '')
    contacts_instructions = __transform(message)
    return render_template('instructions.html', contacts_instructions=contacts_instructions)

def __transform(message):
    all_instructions = Sexting(message, 11).process()

    instructions_by_contact = {}
    for i in all_instructions:
        if i.contact().name() not in instructions_by_contact:
            instructions_by_contact[i.contact().name()] = (i.contact(), [])
        instructions_by_contact[i.contact().name()][1].append(i)

    return instructions_by_contact.values()

