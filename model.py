""" 
GrowShare is a web app for sharing locally grown and sourced food.
"""

from flask_sqlalchemy import SQLAlchemy 

import datetime 

# for search engine, uses the library SQLAlchemy-searchable 

from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType  

db = SQLAlchemy()

make_searchable()

############################################################
# db tables for model.py

class User(db.Model):
    """ Contains user information. """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):

        return "<User user_id={} email={}>".format(self.user_id, self.email)

    # for new users to insert into user table 
    @classmethod
    def add_new_user(cls, first_name, last_name, email, age, password=None):

        new_user = cls(first_name=first_name,
                        username=username,
                        last_name=last_name,
                        email=email,
                        password=password)

        db.session.add(new_user)
        db.session.commit()

    def to_dict(self):
        return {
        'user_id': self.user_id,
        'name': '%s %s' % (self.first_name, self.last_name),
        'email': self.email,
        'age': self.age
        }


class Food(db.Model):
    """ Stores food available. """

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    food_type = db.Column(db.String(50), nullable=False)
    # pick_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.String, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    # posted_date = db.Column(db.DateTime, nullable=False)
    # active = db.Column(db.Boolean, nullable=False, default=True)
    key_words = db.Column(db.String, nullable=True)

    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    # Define Foods relationship to User 
    user = db.relationship("User", backref=db.backref("foods", order_by=user_id))

    def __repr__(self):

        return "<Food food_id={} food_type={} quantity={}>".format(self.food_id,
                                                                    self.food_type,
                                                                    self.quantity)


####################################################################################

def connect_to_db(app):
    """ Connect to the database in Flask app. """

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///growshare'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

