
from flask import Flask, Response, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Food

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

################################################################################
def add_tag_to_db(title,food_type,quantity,description,key_words,user_id):
    """ update db with new food tag. """

    tag = Food(title=title, 
                    food_type=food_type,
                    quantity=quantity,
                    description=description,
                    key_words=key_words,
                    user_id=user_id
                )

    db.session.add(tag)
    db.session.commit()

    return tag

################################################################################
def find_tags(user_id, query_results):
    """ save the query to build nested dict."""

    tags = query_results

    return map_food_tag_details(tags)

################################################################################
def map_food_tag_details(queried_tags):
    """ build dictionary to pass to client as json."""

    tags = {
        tag.food_id: {
            'foodId': tag.food_id,
            'title': tag.title,
            'food_type': tag.food_type,
            'quantity': tag.quantity,
            'excerpt': ' '.join(tag.description.split()[:12]) + '...',
            'key_words': tag.key_words,
            'user_id': tag.user_id

        } for tag in queried_tags
    }

    return tags 









