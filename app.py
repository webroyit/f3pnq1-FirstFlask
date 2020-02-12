from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os       # work with files

app = Flask(__name__)

# route
@app.route("/", methods=["GET"])
def get():
    return jsonify({ "data": "It works"})

# start the server
if __name__ == "__main__":
    app.run(debug=True)