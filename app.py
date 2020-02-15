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
    qty = db.Column(db.Ineger)

    # constructor
    # self is same as this
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# start the server
if __name__ == "__main__":
    app.run(debug=True)