import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# forms
WTF_CSRF_ENABLED = True
app.secret_key = 'password1337'


					# change this to postgresql later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_repo/info.db'
db = SQLAlchemy(app)

			# same here
SQLALCHEMY_DATABASE_URI = 'sqlite:///db_repo/info.db'

from models import *

@app.route('/')
def index():
    return render_template('index.html')
