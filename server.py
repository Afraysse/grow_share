"""
GrowShare

(c) Annie Fraysse, 2016

"""

import os
import csv
import json

from jinja2 import StrictUndefined 

from flask import Flask, render_template, flash, redirect, request, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension 

from model import connect_to_db, db, User, Food

# Import SQLAlchemy exception error to use in try/except
from sqlalchemy.orm.exc import NoResultFound

# Import search function from library to query for information in database
from sqlalchemy_searchable import search 

# Import helper functions from helper.py
import helper

# creates a flask app
app = Flask(__name__)

# requirement for flask session and debug toolbar
app.secret_key = "BCA"

# raise error in jinja if undefined 
app.jinja_env.undefined = StrictUndefined

####################################################

@app.route('/', methods=['GET'])
def index():
    """ Homepage with login/registration. """

    current_session = session.get('current_user', None)
    return render_template("landing.html")


@app.route('/login', methods=['POST'])
def login():
    """ Processes login. """

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("User not found! Please register!")
        return redirect('/')

    if user.password != password:
        flash("Incorrect password! Please try again.")
        return redirect('/')

    session["current_user"] = {
            "first_name": user.first_name,
            "user_id": user.user_id,
        }
    
    return redirect("/dashboard")


@app.route('/register', methods=['POST'])
def register():
    """ get form variables from registration form. """

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    signup_email = request.form.get("signup_email")
    signup_password = request.form.get("signup_password")
    

    # check to ensure signup email doesn't already exist
    # if email does not exist, create new user
    # if email does exist, flash message to ask for a login 

    try:
        db.session.query(User).filter(User.email == signup_email).one()

    except NoResultFound:
        new_user = User(first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=signup_email,
                        password=signup_password
                        )

        db.session.add(new_user)
        db.session.commit()

   # add same info to session similar to login route 

        session["current_user"] = {
            "first_name": new_user.first_name,
            "user_id": new_user.user_id,
        }

        return redirect('/dashboard')

        # return redirect("/dashboard/%s" % new_user.user_id)

    flash("Opps! We already have that email on record. Please login!", "Danger Will Robinson!")

    return redirect('/')


@app.route('/dashboard', methods=['GET'])
def render_profile():
    """ Renders dashboard. """ 

    # .all() returns a list 
    # no .all() returns a sql alchemy object
    food_tags = db.session.query(Food).order_by(Food.food_type)

    total_tags = len(food_tags.all())
    recent_tags = food_tags.limit(5).all()

    return render_template('dashboard.html', total_tags=total_tags,
                                                recent_tags=recent_tags)

@app.route('/tags-geolocation.json', methods=['GET', 'POST'])
def nearby_tags():
    """ Query and post for nearby tags in reference to geolocation."""

    min_lat = request.form.get('minLat');
    min_lng = request.form.get('minLng');
    max_lat = request.form.get('maxLat');
    max_lng = request.form.get('maxLng');

    query_results = Food.query.filter(Food.latitude >= min_lat,
                                        Food.latitude <=max_lat,
                                        Food.longitude >= min_lng,
                                        Food.longitude <= max_lng).order_by(Food.food_id.desc()).all()

    user_id = session.get('user_id')
    tag_dict = helper.find_tags(user_id, query_results)

    return jsonify(tag_dict)

@app.route('/new-post.json', methods=['POST'])
def new_post_db():

    title = request.form.get('food_title')
    food_type = request.form.get('food_type')
    quantity = request.form.get('quantity')
    description = request.form.get('description')
    key_words = request.form.get('key_words')
    user_id = session["current_user"]["user_id"]

    tag = helper.add_tag_to_db(title,food_type,quantity,description,key_words,user_id)

    print tag 

    new_tag = {
        'food_id': tag.food_id,
        'title': tag.title,
        'food_type': tag.food_type,
        'quantity': tag.quantity,
        'excerpt': ' '.join(tag.description.split()[:15]) + '...',
        'key_words': tag.key_words,
        'user_id': tag.user_id
    }

    return jsonify(new_tag)


# @app.route('/JSON_food_tags', methods=["GET", "POST"])
# def q_tags():

#     latitude = request.form.get('latitude') #from maps.js
#     longitude = request.form.get('longitude') #from maps.js
#     radius = request.form.get('radius') #from dashboard.html --> user input: distance


# @app.route('/JSON_food_coords', methods=['GET', 'POST'])
# def query_foods():

#     food_type = request.form.get("food_type") #from dashboard.html
#     key_words = request.form.get("key_words") #from dashboard.html
#     latitude = request.form.get("latitude") #from maps.js
#     longitude = request.form.get("longitude") #from maps.js
#     radius = request.form.get("distance") #from dashboard.html

#     # rectangle_coords = [min_latitude, min_longitude, max_latitude, max_longitude]
#     coords = helper.min_max_latlong(latitude, longitude, radius)

#     # queried_foods is a list of objects
#     queried_foods = Food.query.filter(food_type=food_type)

#     # latitude=coords[0], latitude=coords[2],longitude=coords[1], longitude=coords[3]

#     foods_found = {
#         Food.food_id: {
#             'title': Food.title,
#             'food_type': Food.food_type,
#             'description': Food.description,
#             'posted_date': Food.posted_date,
#             'latitude': Food.latitude,
#             'longitude': Food.longitude,
#             'username': Food.user.username
#         } 

#         for food in queried_foods
#     }

#     return jsonify(foods_found)

# @app.route('/new_tag.json', methods=["POST"])
# def handle_add_tag():
#     """ Add a new tag to the db."""

#     latitude = request.form.get('latitude'),
#     longitude = request.form.get('longitude'),
#     food_type = request.form.get('food_type'),
#     quantity = request.form.get('quantity'),
#     description = request.form.get('description'),
#     key_words = request.form.get('key_words')

#     user_id = session.get('user_id')

#     tag = helper.add_tag_to_db(user_id,latitude,longitude,food_type,quantity,description,key_words)

#     print tag 

#     new_tag = {
#         "user_id": tag.user_id,
#         "tagId": tag.tag_id,
#         "latitude": tag.latitude,
#         "longitude": tag.longitude,
#         "food_type": tag.food_type,
#         "quantity": tag.quantity,
#         "description": tag.description,
#         "key_words": tag.key_words
#     }

#     return jsonify(new_tag)


################################################################################################


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run()












