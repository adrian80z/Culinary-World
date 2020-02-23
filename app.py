import os
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import bcrypt

from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def all_recipes():
    return render_template(
        "recipes.html", title="Home", recipes=mongo.db.recipes.find()
    )


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({"name": request.form["username"]})
        existing_email = users.find_one({"email": request.form["email"]})

        if existing_user is None:
            if existing_email is None:
                hashpass = bcrypt.hashpw(
                    request.form["pass"].encode("utf-8"), bcrypt.gensalt()
                )
                users.insert(
                    {
                        "name": request.form["username"],
                        "password": hashpass,
                        "email": request.form["email"],
                    }
                )
                session["username"] = request.form["username"]
                return redirect(url_for("index"))

            return "That username already exists!"
        return "That email already exists!"

    return render_template("registration.html")


@app.route("/add_recipe")
def add_recipe():
    return render_template(
        "add_recipe.html", title="Add Recipe", cuisine_type=mongo.db.cuisine_type.find()
    )


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(
        {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "author": request.form.get("author"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
        }
    )
    return redirect(url_for("all_recipes"))


@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine_categories = mongo.db.cuisine_type.find()
    return render_template(
        "recipe_details.html", recipes=recipe_details, cuisine_type=cuisine_categories
    )


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine_categories = mongo.db.cuisine_type.find()
    return render_template(
        "edit_recipe.html",
        recipes=recipe_details,
        cuisine_type=cuisine_categories,
        recipe_id=recipe_id,
    )


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update(
        {"_id": ObjectId(recipe_id)},
        {
            "recipe_name": request.form.get("recipe_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "author": request.form.get("author"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
        },
    )
    return redirect(url_for("recipe_details", recipe_id=recipe_id))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("all_recipes"))


@app.route("/find_recipe", methods=["GET", "POST"])
def find_recipe():
    if request.method == "POST":

        # get search word
        search_word = request.form.get("search")

        # create the index
        mongo.db.recipes.create_index([("$**", "text")])

        # search with the search word that came through the search bar
        query = mongo.db.recipes.find({"$text": {"$search": search_word}})
        recipe = [recipe for recipe in query]

        # send recipes to page
        return render_template("recipes.html", recipes=recipe, query=search_word)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

