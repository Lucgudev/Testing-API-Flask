from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS


file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
CORS(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from my_app.catalog.views.product_view import catalog
from my_app.catalog.views.user_view import auth_blueprint
app.register_blueprint(catalog)
app.register_blueprint(auth_blueprint)

db.create_all()
