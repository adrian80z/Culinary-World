import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def all_recipes():
    return render_template("recipes.html", title="Home",
    cuisine_type = mongo.db.cousine_type.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

