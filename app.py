import os
from flask import Flask, render_template, request, redirect
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

@app.route('/signin', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
	login_form = LoginForm()

	if request.method=='POST' and login_form.validate():

		print("user login request")

		# look for user
		user = User.query.filter_by(username=login_form.username.data).first()

		if user and user.check_password(login_form.password.data):

			return redirect('/home')

		print('what the fk')

	return render_template('login.html',
							title='Welcome',
							login_form=login_form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
	signup_form = SignupForm()

	if request.method=='POST' and signup_form.validate():

		print("new user being registered")

		# create new user
		user = User(signup_form.name.data,
					signup_form.email.data,
					signup_form.username.data,
					signup_form.password.data,
					bio=None
					)

		# SHITTY ASS TEMPORARY FIX (IT SHOULD INITIALIZE)
		user.set_password(signup_form.password.data)

		# add to db
		db.session.add(user)
		db.session.commit()

		return redirect('/home')

	return render_template('signup.html',
							title='Join Us!',
							signup_form=signup_form)
