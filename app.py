from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os       # work with files

# init app
app = Flask(__name__)
# find the path to save the file
basedir = os.path.abspath(os.path.dirname(__file__))
# accress to the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
# prevent the warming message
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# init database
db = SQLAlchemy(app)
# init marshmallow
ma = Marshmallow(app)

#product class or model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    # constructor
    # self is same as this
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# product schema
class ProductSchema(ma.Schema):
    # display these data to the client
    class Meta:
        fields = ("id", "name", "description", "price", "qty")

# init schema
product_schema = ProductSchema()
# one to many relationship
products_schema = ProductSchema(many = True)

#create a product route
@app.route("/product", methods=["POST"])
def add_product():
    # get the data from the client
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(name, description, price, qty)

    # save the new product to the database
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# start the server
if __name__ == "__main__":
    app.run(debug=True)