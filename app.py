import os
from flask import Flask
from flask_pymongo import PyMongo

from os import path
if path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)