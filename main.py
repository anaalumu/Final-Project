import datetime
import dateutil.tz

from flask import Blueprint, render_template
from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("homePage.html")

@bp.route("/recipes")
def index():
    return render_template("recipe.html")

@bp.route("/userregister")
def index():
    return render_template("user.html")

