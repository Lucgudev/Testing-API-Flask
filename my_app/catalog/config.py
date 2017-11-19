import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'keramenstruasi')
