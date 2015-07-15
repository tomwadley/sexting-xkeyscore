from web import app
from flask import render_template, request, url_for, redirect, session, flash
import re, json
from sexting.sexting import Sexting
from sexting.lib.contactloader import ContactLoader
from sexting.lib.tubedata import TubeData
from formencode.variabledecode import variable_decode

_tubedata = TubeData()

@app.route('/')
def message_input():
    message = session.get('message', '')
    return render_template('message_input.html', message=message, nav_data=__nav_data())

@app.route('/message', methods=['POST'])
def submit_message():
    message = request.form.get('message', '')
    if not __validate_message(message):
        return __invalid_message()

    session['message'] = message

    return redirect(url_for('contacts_input'))

@app.route('/contacts')
def contacts_input():
    message = session.get('message', '')
    if not __validate_message(message):
        return __invalid_message()

    contacts = session.get('contacts', [{}])
    contacts_json = json.dumps(contacts)
    return render_template('contacts_input.html', contacts_json=contacts_json, stations=_tubedata.all_stations(), nav_data=__nav_data())

@app.route('/contacts', methods=['POST'])
def submit_contacts():
    contacts = __decode_contacts(request.form)
    if not __validate_contacts(contacts):
        return __invalid_contacts()

    session['contacts'] = contacts

    return redirect(url_for('view_instructions'))

def __decode_contacts(form):
    contacts = []
    form_data = variable_decode(form)

    for key in form_data:
        if re.match('^c[0-9]+$', key):
            index = int(key[1:])
            contact = __decode_contact(form_data[key])
            if contact is not None:
                contacts.append((index, contact))

    contacts.sort(key=lambda t: t[0])
    return map(lambda t: t[1], contacts)

def __decode_contact(d):
    if 'name' not in d or not d['name'].strip():
        return None

    name = d['name']
    del d['name']

    __decode_checkbox(d, 'contactless')
    __decode_checkbox(d, 'twitter')

    if 'tubestation' in d and not _tubedata.is_valid_station(d['tubestation']):
        return None

    return {'name': name, 'data': d}

def __decode_checkbox(d, field):
    if field in d and d[field] == 'on':
        d[field] = True

@app.route('/instructions')
def view_instructions():
    message = session.get('message', '')
    contacts = session.get('contacts', [])
    start_hour = 11

    if not __all_data_provided(message, contacts):
        return __no_data()

    contacts_instructions = __transform(message, contacts, start_hour)
    return render_template('instructions.html', contacts_instructions=contacts_instructions, nav_data=__nav_data())

def __transform(message, contacts, start_hour):
    contacts = ContactLoader().all_from_dicts(contacts)
    all_instructions = Sexting(contacts, message, start_hour).process()

    instructions_by_contact = {}
    for i in all_instructions:
        if i.contact().name() not in instructions_by_contact:
            instructions_by_contact[i.contact().name()] = (i.contact(), [])
        instructions_by_contact[i.contact().name()][1].append(i)

    return instructions_by_contact.values()

def __nav_data():
    show_contacts = 'message' in session
    show_instructions = 'contacts' in session
    return {'show_contacts': show_contacts, 'show_instructions': show_instructions}

def __validate_message(message):
    return bool(message)

def __invalid_message():
    flash('You must enter a message!', 'warning')
    return redirect(url_for('message_input'))

def __validate_contacts(contacts):
    return bool(contacts)

def __invalid_contacts():
    flash('You must enter contact details!', 'warning')
    return redirect(url_for('contacts_input'))

def __all_data_provided(message, contacts):
    return __validate_message(message) and __validate_contacts(contacts)

def __no_data():
    return redirect(url_for('message_input'))

