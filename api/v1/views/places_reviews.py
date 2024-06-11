#!/usr/bin/python3
"""
"""
from flask import jsonify, abort, request
from models.review import Review
from models.place import Place
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def get_all_reviews(place_id):
    """ get reviews from a spcific place """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [obj.to_dict() for obj in place.reviews]
    return jsonify(reviews)


@app_views.route('reviews/<review_id>', strict_slashes=False)
def get_a_review(review_id):
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        return abort(404)


@app_views.route('reviews/<review_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_Review(review_id):
    amenity = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route('places/<place_id>/reviews',
                 methods=["POST"], strict_slashes=False)
def post_review(place_id):
    """ updates by id """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
