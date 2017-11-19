import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.catalog.models.user_model import User
import hashlib

auth_blueprint = Blueprint('auth', __name__)

class UserView(MethodView):
    def post(self):
        can_push = True
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')

        if (name == None):
            name = "Name must not empty"
            can_push = False
        if (password == None):
            password = "Password must not empty"
            can_push = False
        if (email == None):
            email = "Email must not empty"
            can_push == True
        user = User(name, password, email)
        if (can_push == True):
            db.session.add(user)
            db.session.commit()
        return jsonify({'message': {
            'id' : user.id,
            'name': user.name,
            'email': user.email,
        }})

class Login(MethodView):
    def post(self):
        try:
            password = request.form.get('password')
            email = request.form.get('email')

            user_data = User.query.filter_by(email = email).first()
            if (user_data.password == hashlib.md5(password.encode('utf-8')).hexdigest() and email == user_data.email):
                print('test')
                token = user_data.encode_token(user_data.email)
                print('token: ', token)
                return jsonify({'message': {
                    'id' : user_data.id,
                    'name': user_data.name,
                    'email': user_data.email,
                    'token': token.decode(),
                }})
            else:
                return jsonify({'error': {
                    'message':'password is incorrect',
                }})
        except Exception as e:
            return jsonify({'error': {
                'message':'email not found',
            }})


user_view =  UserView.as_view('user_view')
login = Login.as_view('login')
app.add_url_rule(
    '/register/', view_func=user_view, methods=['POST']
)

app.add_url_rule(
    '/login/', view_func=login, methods=['POST']
)
