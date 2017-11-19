from my_app import db, app
import hashlib
import jwt

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()

    def encode_token(self, email):
        try:
            payload = {
                'sub': email,
            }
            return jwt.encode(payload, 'keramenstruasi', algorithm = 'HS256')
        except Exception as e:
            return e

    def decode_token(token):
        try:
            payload = jwt.decode(token, 'keramenstruasi', algorithms = 'HS256')
            return payload['sub']
        except jwt.InvalidTokenError:
            return 'invalid token'
