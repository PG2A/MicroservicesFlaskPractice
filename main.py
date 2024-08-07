import dataclasses
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask.json import JSONEncoder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return obj.to_dict()
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

#@dataclasses
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image
        }

#@dataclasses
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
