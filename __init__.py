from flask import Flask
#from flask_sqlalchemy import SQLAlchemy - for database


def create_app(test_config=None):

    app = Flask(__name__)

    #connect to the database
    #app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://24_webapp_000:100475297@mysql.lab.it.uc3m.es/24_webapp_000a"- for database

    # A secret for signing session cookies
    app.config["SECRET_KEY"] = "93220d9b340cf9a6c39bac99cce7daf220167498f91fa"

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main

    #db.init_app(app)- for database

    app.register_blueprint(main.bp)
    return app
