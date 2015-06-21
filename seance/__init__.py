from flask import Flask
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)

import seance.seanceweb
