
from flask import Flask, Response, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Food

def min_max_latlong(latitude, longitude, radius):
    """ To create boundary for querying rectangle. """

    # latitude and longitude gathered from user position (var pos)
    # radius from input form (5, 10 or 20 miles)

    min_latitude = latitutde - radius
    min_longitude = longitude - radius
    max_latitude = latitutde + radius
    max_longitude = longitude + radius

    rectangle_coords = [min_latitude, min_longitude, max_latitude, max_longitude]

    return rectangle_coords

################################################################################################

def add_tag_to_db(user_id,latitutde,longitude,food_type,quantity,description,key_words):
    """ update db with new food tag. """

    tag = Food(user_id=user_id, 
                    latitutde=latitutde,
                    longitude=longitude,
                    food_type=food_type,
                    quantity=quantity,
                    description=description,
                    key_words=key_words
                )

    db.session.add(tag)
    db.session.commit()

    return tag






