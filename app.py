import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def all_recipes():
    return render_template(
        "recipes.html", title="Home", recipes=mongo.db.recipes.find()
    )


@app.route("/add_recipe")
def add_recipe():
    return render_template(
        "add_recipe.html", title="Add Recipe", cuisine_type=mongo.db.cousine_type.find()
    )


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("all_recipes"))


@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cousine_categories = mongo.db.cousine_type.find()
    return render_template(
        "recipe_details.html", recipes=recipe_details, cuisine_type=cousine_categories
    )


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cousine_categories = mongo.db.cousine_type.find()
    return render_template(
        "edit_recipe.html", recipes=recipe_details, cuisine_type=cousine_categories
    )


@app.route("/update_recipe/<recipe_id>")
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'cuisine_name' : request.form.get('cuisine_name'),
        'difficulty' : request.form.get('difficulty'),
        'serves' : request.form.get('serves'),
        'prep_time' : request.form.get('prep_time'),
        'author': request.form.get('author'),
        'image_url' : request.form.get('image_url),
        'description' : request.form.get('description'),
        'ingredients' : request.form.get('ingredients'),
        'step_one' : request.form.get('step_one')
    })
    return redirect(url_for('all_recipes'))



@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("all_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

