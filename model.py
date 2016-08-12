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
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String, nullable=False)

    search_vector = db.Column(TSVectorType('first_name', 'last_name'))

    def __repr__(self):

        return "<User user_id={} email={}>".format(self.user_id, self.email)

    # for new users to insert into user table 
    @classmethod
    def add_new_user(cls, first_name, last_name, email, age, password=None):

        new_user = cls(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        age=age,
                        password=password)

        db.session.add(new_user)
        db.session.commit()

class Connections(db.Model):
    """ Establishes relationship between users. """

    __tablename__ = 'connection'

    connection_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    control_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    connector_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    user = db.relationship("User",
                            primaryjoin="User.user_id == Connections.control_id",
                            backref=db.backref("Connections",
                                                order_by=connection_id))

    def __repr__(self):

        return ("Connection between control_id: \
                %s and connector_id: %s>") % (self.control_id,
                                            self.connector_id)

    @classmethod
    def add_connection(cls, control_id, connector_id):

        new_connection = cls(control_id=control_id, connector_id=connector_id)
        db.session.add(new_connection)
        db.session.commit()

class Locations(db.Model):
    """ Stores location information. """

    __tablename__ = 'location'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):

        return ("<Location %s: latitude:" + 
                "%s longitude: %s>") % (self.location_id, self.latitude, 
                                        self.longitude)

# NOTE: need to add helper functions to update 

class Food(db.Model):
    """ Stores food available. """

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'), nullable=False)
    food_type = db.Column(db.String(50), nullable=False)
    organic = db.Column(db.Boolean, nullable=False)
    pick_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    # for sharing with other users:
    shared_with = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=True)

    def __repr__(self):

        return "<Food food_id={} food_type={} quantity={}>".format(self.food_id,
                                                                    self.food_type,
                                                                    self.quantity)

class Messaging(db.Model):
    """ Stores updated food available. """

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    recipiant_id = db.Column(db.Integer, nullable=False)
    message_sent = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, nullable=False)

    def __repr__(self):

        return ("<Message id: %s, sender_id: %s, recipiant_id: %s>") % (self.message_id,
                                                                        self.sender_id,
                                                                        self.recipiant_id)
# NOTE: need to add helper functions 

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

