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
app.config("SQLALCHEMY_TRACK_MODIFICATIONS") = False
# init database
db = SQLAlchemy(app)
# init marshmallow
ma = Marshmallow(app)

# start the server
if __name__ == "__main__":
    app.run(debug=True)