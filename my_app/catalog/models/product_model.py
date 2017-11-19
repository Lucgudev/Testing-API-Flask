from my_app import db

class Product(db.Model):
    __tablename__ = "tb_product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float(asdecimal=True))
    description = db.Column(db.String(255))
    owner_id = db.Column(db.Integer)

    def __init__(self, name, price, description, owner_id):
        self.name = name
        self.price = price
        self.description = description
        self.owner_id = owner_id

    def __repr__(self):
        return '<Product %d>' % self.id
