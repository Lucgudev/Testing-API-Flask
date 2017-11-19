from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)

from my_app.catalog.views.product_view import catalog
from my_app.catalog.views.user_view import auth_blueprint
app.register_blueprint(catalog)
app.register_blueprint(auth_blueprint)

db.create_all()
