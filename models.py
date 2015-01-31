from app import db
from datetime import datetime

class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(80))
	username = db.Column(db.String(40))
	bio = db.Column(db.String(500))
	karma = db.Column(db.Integer)
	start_date = db.Column(db.DateTime)
	# questions is backref-ed by Questions class
	# answers is backref-ed by Answer class
	# comments is backref-ed by Comment class

	def __init__(self, name, email, username, 
				bio, karma=0, start_date=None):

		self.name = name
		self.email = email
		self.username = username
		self.bio = bio
		self.karma = 0

		if start_date is None:
			start_date = datetime.utcnow()
		self.start_date = start_date

	def __repr__(self):
		return '<User %r>' % self.username

	"""Flask Login Stuff"""
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


class Question(db.Model):

	"""self info: media, text, score, topics, postdate
	backref-ed info: comments, answers
	backref-ing: user
	"""
	id = db.Column(db.Integer, primary_key=True)
	media = db.Column(db.String(100))
	text = db.Column(db.String(1000))
	score = db.Column(db.Integer)
	# comments is backref-ed by Comment class
	# answers is backref-ed by Answer class

	# backref-ing to user class
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',
		backref=db.backref('questions', lazy='dynamic'))

	def __init__(self, media, text, score, user, start_date=None):

		self.media = media
		self.text = text
		self.score = score

		if start_date is None:
			start_date = datetime.utcnow()
		self.start_date = start_date

		self.user = user

	def __repr__(self):
		return '<Question %r>' % self.id


class Answer(db.Model):

	"""self info: media, text, score, topics, postdate
	backref-ed info: comments
	backref-ing: user, questions
	"""
	id = db.Column(db.Integer, primary_key=True)
	media = db.Column(db.String(100))
	text = db.Column(db.String(1000))
	score = db.Column(db.Integer)
	# comments is backref-ed by Comment class

	# backref-ing to user class
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',
		backref=db.backref('answers', lazy='dynamic'))

	def __init__(self, media, text, score, 
					user, question, start_date=None):

		self.media = media
		self.text = text
		self.score = score

		if start_date is None:
			start_date = datetime.utcnow()
		self.start_date = start_date

		self.user = user
		self.question = question

	def __repr__(self):
		return '<Answer %r>' % self.id

class Question_Comment(db.Model):

	"""self info: text, postdate
	backref-ed info: None
	backref-ing: question, user
	"""
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(1000))
	score = db.Column(db.Integer)

	# backref-ing to user class
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',
		backref=db.backref('question_comments', lazy='dynamic'))

	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	question = db.relationship('Question',
		backref=db.backref('questions', lazy='dynamic'))

	def __init__(self, text, score, user, question, start_date=None):

		self.text = text
		self.score = score

		if start_date is None:
			start_date = datetime.utcnow()
		self.start_date = start_date

		self.user = user
		self.question = question

	def __repr__(self):
		return '<Question_Comment %r>' % self.id


class Answer_Comment(db.Model):

	"""self info: text, postdate
	backref-ed info: None
	backref-ing: answer, user
	"""
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(1000))
	score = db.Column(db.Integer)

	# backref-ing to user class
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',
		backref=db.backref('answer_comments', lazy='dynamic'))

	answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
	answer = db.relationship('Answer',
		backref=db.backref('answers', lazy='dynamic'))

	def __init__(self, text, score, user, answer, start_date=None):

		self.text = text
		self.score = score

		if start_date is None:
			start_date = datetime.utcnow()
		self.start_date = start_date

		self.user = user
		self.answer = answer

	def __repr__(self):
		return '<Answer_Comment %r>' % self.id



