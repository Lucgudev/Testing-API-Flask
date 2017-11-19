import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.catalog.models.product_model import Product
from my_app.catalog.models.user_model import User

catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


class ProductView(MethodView):

    def get(self, id=None, page=1):
        header = request.headers.get('Authorization')
        payload = User.decode_token(header)

        try:
            data = User.query.filter_by(email=payload).first()
            print(data.email)
            print(payload)
            if (data.email == payload):
                if not id:
                    products = Product.query.paginate(page, 10).items
                    res = {}
                    index = 0
                    for product in products:
                        res[index] = {
                            'id':product.id,
                            'name': product.name,
                            'price': str(product.price),
                            'description' : product.description,
                            'owner_id' : product.owner_id,
                        }
                        index = 1 + index
                else:
                    product = Product.query.filter_by(id=id).first()
                    if not product:
                        abort(404)
                    res = {
                        'id':product.id,
                        'name': product.name,
                        'price': str(product.price),
                        'description' : product.description,
                        'owner_id' : product.owner_id,
                    }
            else:
                return jsonify({'message': {
                    'error':'unauthorized',
                }})

            return jsonify(res)
        except Exception as e:
            return jsonify({'message': {
                'error':'unauthorized',
            }})

    def post(self):

        header = request.headers.get('Authorization')
        payload = User.decode_token(header)

        try:
            data = User.query.filter_by(email=payload).first()

            print(data.email)
            print(payload)

            can_push = True
            name = request.form.get('name')
            price = request.form.get('price')
            desc = request.form.get('description')
            if(name == None):
                name = "Name must not empty"
                can_push = False
            if(price == None):
                price = "Price must not empty"
                can_push = False
            if (desc == None):
                desc = "No description"
            product = Product(name, price, desc, data.id)
            if (can_push == True):
                db.session.add(product)
                db.session.commit()
            return jsonify({'message': {
                'id' : product.id,
                'name': product.name,
                'price': str(product.price),
                'description' : product.description

            }})
        except Exception as e:
            return jsonify({'message': {
                'error':'unauthorized',
            }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        deleted_id = id
        products = Product.query.filter_by(id=deleted_id).first()
        db.session.delete(products)
        db.session.commit()
        # Delete the record for the provided id.
        return jsonify({
        'message':'success delete',
        })

    def search(self, name):
        product_name = name
        products = Product.query.filter_by(name = product_name).first()
        res = {}
        for product in products:
            res[product.id] = {
                'name': product.name,
                'price': str(product.price),
                'description' : product.description,
            }
        return jsonify(res)

product_view =  ProductView.as_view('product_view')
app.add_url_rule(
    '/product/', view_func=product_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/product/<int:id>', view_func=product_view, methods=['GET', 'DELETE']
)

app.add_url_rule(
    '/product/search/<int:name>', view_func=product_view, methods=['GET']
)
