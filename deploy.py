# -*- coding: utf-8 -*-
__author__ = 'itmard'

from flask import Flask
from flask import request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.ext.mongoengine import MongoEngine
from mongoengine import Document, StringField
from mongoengine import ValidationError, DoesNotExist
from wtforms import Form
from wtforms.fields import StringField as FormStringField
import wtforms_json



class User(Document):
    username = StringField()
    token = StringField()


class LoginFrom(Form):
    username = FormStringField()
    password = FormStringField()


application = Flask(__name__)
application.config['MONGODB_SETTINGS'] = dict(DB='test_login', HOST='127.0.0.1', PORT=27017)
db = MongoEngine(application)
wtforms_json.init()

@application.errorhandler(400)
def bad_request_error(error):
    return '', 400

@application.errorhandler(401)
def unauthorized_error(error):
    return '', 401

@application.errorhandler(403)
def forbidden_error(error):
    return '', 403

@application.errorhandler(404)
def not_found_error(error):
    return '', 404

@application.errorhandler(405)
def method_not_allowed_error(error):
    return '', 405

@application.errorhandler(500)
def internal_server_error(error):
    return '', 500

try:
    u = User.objects.get(username='itmard')
except (ValidationError, DoesNotExist):
    u = User(username='itmard')
    u.save()


@application.route('/login/', methods=['POST'])
def login():
    form = LoginFrom.from_json(request.json)
    if form.validate():
        if form.username.data == 'itmard' and form.password.data == '123123':
            s = Serializer('confident_key!', expires_in=86400)  # 24H
            u = User.objects.get(username='itmard')
            token = s.dumps({'user': u.username})
            return token
        return 'User and Password not OK', 401


@application.route('/test/')
def test_token():
    token = request.headers.get('TOKEN')
    if token:
        s = Serializer('confident_key!', expires_in=86400)  # 24H
        try:
            token_data = s.loads(token)
        except:
            return 'BAD SIG', 401

        username = token_data.get('user')
        if username:
            try:
                u = User.objects.get(username=username)
                return u.username, 200
            except (ValidationError, DoesNotExist):
                return 'NO USER', 401

    return 'NO ACCESS', 401
