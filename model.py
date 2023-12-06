from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    recipes = db.relationship('Recipes', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    bookmarks = db.relationship('Bookmarks', back_populates='user')
    photos = db.relationship('Photos', back_populates='user')

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship('User', back_populates='recipes')
    quantified_ingredients = db.relationship('QuantifiedIngredients', back_populates='recipes')
    steps = db.relationship('Steps', back_populates='recipes')
    ratings = db.relationship('Rating', back_populates='recipes')
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    n_person = db.Column(db.Integer, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    bookmarks = db.relationship('Bookmarks', back_populates='recipes')
    photos = db.relationship('Photos', back_populates='recipes')

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    quantified_ingredients = db.relationship('QuantifiedIngredients', back_populates='ingredients')

class QuantifiedIngredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    unit_measurement = db.Column(db.String, nullable=False)
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable=False)
    ingredients = db.relationship('Ingredients', back_populates='quantified_ingredients')
    recipes_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    recipes = db.relationship('Recipes', back_populates='quantified_ingredients')

class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    sequence_number = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipes', back_populates='steps')

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='ratings')
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipes = db.relationship('Recipes', back_populates='ratings')

class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='bookmarks')
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipes', back_populates='bookmarks')

class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='photos')
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipes', back_populates='photos')
    file_extension = db.Column(db.String(10), nullable=False)

