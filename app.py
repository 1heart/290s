import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import (LoginManager, login_required,
					login_user, logout_user, current_user)

app = Flask(__name__)

# forms
WTF_CSRF_ENABLED = True
app.secret_key = 'password1337'


					# change this to postgresql later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_repo/info.db'
db = SQLAlchemy(app)

			# same here
SQLALCHEMY_DATABASE_URI = 'sqlite:///db_repo/info.db'

# login manager stuff
login_manager = LoginManager()
login_manager.init_app(app)

from models import *
from forms import *

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
	
	login_form = LoginForm()

	if request.method=='POST':

		print("user login request")



@app.route('/signup', methods=["GET", "POST"])

	signup_form = SignupForm()

	if request.method=='POST':

		print("new user being registered")

		user = User(signup_form.name.data,
					signup_form.email.data,
					signup_form.username.data,
					bio=None)


