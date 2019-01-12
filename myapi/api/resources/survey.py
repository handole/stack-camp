from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from myapi.models import Survey, SurveyQuestion
from myapi.extensions import ma, db
fro myapi.commons.pagination import paginate
fro marshmallow import fields

class SurveyQuestionSchema(ma.ModelSchema):
	class Meta:
		model = SurveyQuestion
		sqla_question = db.session
		include_fk = True

class SurveySchema(ma.ModelSchema):
	class Meta:
		model = Survey
		sqla_question = db.session
		include_fk = True
	survey_questions = ma.Nested(SurveyQuestionSchema, many=True)

class SurveyResource(Resource):
	method_decorators = [jwt_required]

	def get(self, survey_id):
		scema = SurveySchema()
		survey = Survey.query.filter_by(id=survey_id).first()
		survey.survey_questions
		return {"survey": schema.dump(survey).data}