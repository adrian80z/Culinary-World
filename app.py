import os
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import bcrypt
from functools import wraps

from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

#env variables
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)


# middleware for login required 
# https://medium.com/@devsudhi/how-to-create-a-middleware-in-flask-4e757041a6aa
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def all_recipes():
    return render_template(
        "recipes.html", title="Home", recipes=mongo.db.recipes.find()
    )


@app.route("/index")
def index():
    if "username" in session:
        return render_template("recipes.html", recipes=mongo.db.recipes.find())
    else:
        return render_template("login.html", title="Login")


#user registration
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({"name": request.form["username"]})
        existing_email = users.find_one({"email": request.form["email"]})

        # if username or email is not in collection insert it else display appropriate flash message
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

            flash("Email already exist!")
            return redirect(url_for("register"))
        flash("Username already exist!")
        return redirect(url_for("register"))
    return render_template("registration.html", title="Registration")


#user login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({"name": request.form.get("username")})

        if login_user:
            if (
                bcrypt.hashpw(request.form["pass"].encode("utf-8"), login_user["password"])
                == login_user["password"]
            ):
                session["username"] = request.form["username"]
                flash("You were successfully logged in")
                return redirect(url_for("all_recipes"))

    return render_template("login.html", title="Login")


#user logout
@app.route("/logout")
def logout():
    # remove the username from the session
    session.pop("username", None)
    flash("You were successfully logged out")
    return redirect(url_for("all_recipes"))


#add recipe
@app.route("/add_recipe")
@login_required
def add_recipe():
    return render_template(
        "add_recipe.html", title="Add Recipe", cuisine_type=mongo.db.cuisine_type.find(), levels = mongo.db.level.find()
    )


#insert recipe
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
    flash("Recipe sucessfuly added")
    return redirect(url_for("all_recipes"))


#display recipe using id
@app.route("/recipes/<recipe_id>")
def recipe_details(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine_categories = mongo.db.cuisine_type.find()
    return render_template(
        "recipe_details.html", recipes=recipe_details, cuisine_type=cuisine_categories
    )


#edit recipe using id
@app.route("/edit_recipe/<recipe_id>")
@login_required
def edit_recipe(recipe_id):
    recipe_details = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine_categories = mongo.db.cuisine_type.find()
    difficulty_level = mongo.db.level.find()
    return render_template(
        "edit_recipe.html",
        recipes=recipe_details,
        cuisine_type=cuisine_categories,
        recipe_id=recipe_id,
        levels=difficulty_level
    )


#update recipe using id
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
    flash("Recipe sucessfuly updated")
    return redirect(url_for("recipe_details", recipe_id=recipe_id))


#delete recipe using id
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe sucessfuly deleted")
    return redirect(url_for("all_recipes"))


#search recipe 
@app.route("/find_recipe", methods=["GET", "POST"])
def find_recipe():
    if request.method == "POST":

        # get search word
        search_word = request.form.get("search")

        # create the index
        mongo.db.recipes.create_index([("$**", "text")])

        # search with the search word that came through the search bar
        query = mongo.db.recipes.find({"$text": {"$search": search_word}})
        recipes_counter = query.count()
        recipe = [recipe for recipe in query]

        # send results to page
        return render_template("results.html", recipes=recipe, query=search_word, total = recipes_counter)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)

