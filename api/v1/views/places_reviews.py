#!/usr/bin/python3
"""
"""
from flask import jsonify, abort, request
from models.review import Review
from models.place import Place
from models import storage
from api.v1.views import app_views


@app_views.route('/api/v1/places/<place_id>/reviews', strict_slashes=False)
def get_reviews(place_id):
    reviews_list = []
    places = storage.all(Place).values()
    place = [obj.to_dict() for obj in places if obj.id == place_id]
    if place == []:
        return abort(404)
    return jsonify(place[0].reviews())


@app_views.route('/api/v1/reviews/<review_id>', strict_slashes=False)
def get_a_review(review_id):
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        return abort(404)
