from flask import Flask
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)

app.secret_key = "\xefO\x0c'\x92\xcd\xd7QC\xb7\x0b\xfb(\xbeC\x11B\xfas\x8c\x13\x07\xf1t"

import web.sextingweb
