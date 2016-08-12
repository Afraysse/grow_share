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

from model import connect_to_db, db, User, Connections, Food, Locations, Messaging

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

    current_session = session.get('user_id', None)
    return render_template("landing.html")


@app.route('/login', methods=['POST'])
def login():
    """ Processes login. """

    login_email = request.form.get("email")
    login_password = request.form.get("password")

    # try to see if credentials put in work
    # if incorrect, ask to try again 
    # if correct, log in user and store to session and grab friend information 
    try:
        current_user = db.session.query(User).filter(User.email == login_email,
                                                    User.password == login_password).one()

    except NoResultFound:
        flash("We can't seem to find you! Please try again.", "Danger Will Robinson!")
        return redirect('/')

    # Acquire current user's friend information to display in badges on page

    # received_friend_requests, sent_friend_requests = get_friend_requests(current_user.user_id)
    # receieved_request_count = len(received_friend_requests)
    # sent_request_count = len(sent_friend_requests)
    # total_request_count = receieved_request_count + sent_request_count

    # a nested dictionary stores more to the session than simply the user_id

    session["current_user"] = {
        "first_name": current_user.first_name,
        "user_id": current_user.user_id,
        # "receieved_request_count": receieved_request_count,
        # "sent_request_count": sent_request_count,
        # "total_request_count": total_request_count
    }

    # flash("Hello {}. You have successfully logged in!").format(current_user.first_name)
    
    return redirect("/dashboard")


@app.route('/register', methods=['POST'])
def register():
    """ get form variables from registration form. """

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    description = request.form.get("description")
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
                        email=signup_email,
                        description=description,
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

    return render_template('dashboard.html')


# @app.route('/dashboard', methods=['POST'])
# def user_profile():

#     pass


################################################################################################


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run()












