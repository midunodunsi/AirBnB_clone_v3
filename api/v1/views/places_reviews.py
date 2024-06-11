#!/usr/bin/python3
"""
"""
from flask import jsonify, abort, request
from models.review import Review
from models.place import Place
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/api/v1/places/<place_id>/reviews', strict_slashes=False)
def get_reviews(place_id):
    place = storage.get(Place, place_id)
    if place:
        obj = []
        review_save = storage.all(Review)
        for key, value in review_save.items():
            if value.place_id == str(place_id):
                obj.append(value.to_dict())
        return jsonify(obj)
        
    else:


@app_views.route('/api/v1/reviews/<review_id>', strict_slashes=False)
def get_a_review(review_id):
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        return abort(404)


@app_views.route('/api/v1/reviews/<review_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_Review(review_id):
    amenity = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route('/api/v1/places/<place_id>/reviews', methods=["POST"], strict_slashes=False)
def post_review(place_id):
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    data = request.get_json()

    if 'user.id' not in data:
        return abort(400, 'Missing user_id')
    if 'text' not in data:
        return abort(400, 'Missing text')

    places = storage.all(Place).values()
    place = [obj.to_dict() for obj in places if obj.id == place_id]
    if place == []:
        return abort(404)

    Users = storage.all(User).values()
    user_id = data['user.id']
    user_list = [obj.to_dict() for obj in places if obj.id == user_id]
    if user_list == []:
        return abort(404)

    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201
