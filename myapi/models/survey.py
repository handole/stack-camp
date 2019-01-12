from myapi.extensions import db
from .user import User

class Survey(db.Model):
	__table__ = 'survey'

	id = db.Column(db.Integer, primary_key=True, index=True)
	description = db.Column(db.String(250), index=True)
	startdate = db.Column(db.DateTime)
	enddate = db.Column(db.DateTime)
	status = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	questions = db.relationship('Question', backref='questions', lazy='dynamic')
	response = db.Column(db.String(250), index=True)

	def __repr__(self):
		return "<Survey {}".format(self.description)


class Question(db.Model):
	__table__ = "question"
	id = db.Column(db.Integer, primary_key=True, index=True)
	survey_id =db.Column(db.Integer, db.ForeignKey('survey.id'))
	question_type = db.Column(db.String(100), index=True)
	question = db.Column(db.String(250), index=True)


class OfferedAnswer(db.Model):
	__table__ = 'offeredanswer'
	id = db.Column(db.Integer, primary_key=True, index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	response = db.Column(db.String(250), index=True)


class Answer(db.Model):
	__table__ = 'answer'
	id = db.Column(db.Integer, primary_key=True, index=True)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	answering = db.Column(db.String(250), index=True)