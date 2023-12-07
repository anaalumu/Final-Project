import datetime
import dateutil.tz

from flask import Blueprint, render_template
from . import model

bp = Blueprint("main", __name__)

@bp.route("/profile")
def index():
    user = model.User(1, "mary@example.com", "mary")
    recipes = [
        model.Recipe(1, user, "Gingerbread Cookies", "static/recipe1.jpg"),
        model.Recipe(2, user, "Stuffed Chicken", "static/recipe2.jpg"),
        model.Recipe(3, user, "Panetone", "static/recipe3.jpg")      

    ]
    return render_template("main/index.html", recipes = recipes)

@bp.route("/profile")
def profile():
    user = model.User(1, "mary@example.com", "mary")
    return render_template("main/profile.html", user = user)

@bp.route("/userlogin")
def userlogin():
    return render_template("main/userlogin.html")

@bp.route("/userregister")
def userregister():
    return render_template("main/userregister.html")

@bp.route("/create_recipe")
def create_recipe():
    return render_template("main/create_recipe.html")

