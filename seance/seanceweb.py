from seance import app
from flask import render_template, request, url_for, redirect
import os, errno, uuid, subprocess, shutil
from sexting.sexting import Sexting
import pdfkit

_contacts_file = 'contacts.json'

@app.route('/')
def message_input():
    return render_template('message_input.html')

@app.route('/print', methods=['POST'])
def transform_and_print():
    message = request.form['message']
    request_id = str(uuid.uuid4())

    print "Request ID: {0}, Message: {1}".format(request_id, message)

    url = url_for('transform', _external=True, message=message, start_hour=11)

    output_path = __get_output_path(request_id + '.pdf')
    __backup_contacts(request_id)
    __generate_pdf(url, output_path)
    subprocess.Popen(['lpr', output_path])

    return redirect(url_for('message_input'))

def __backup_contacts(request_id):
    shutil.copy(_contacts_file, __get_output_path(request_id + '.json'))

def __get_output_path(filename):
    output_dir = 'output'
    try:
        os.makedirs(output_dir)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(output_dir):
            pass
        else:
            raise
    return os.path.join(output_dir, filename)

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
    start_hour = request.args.get('startHour', 11)

    contacts_instructions = __transform(message, start_hour)
    return render_template('instructions.html', contacts_instructions=contacts_instructions)

def __transform(message, start_hour):
    all_instructions = Sexting(_contacts_file, message, start_hour).process()

    instructions_by_contact = {}
    for i in all_instructions:
        if i.contact().name() not in instructions_by_contact:
            instructions_by_contact[i.contact().name()] = (i.contact(), [])
        instructions_by_contact[i.contact().name()][1].append(i)

    return instructions_by_contact.values()

