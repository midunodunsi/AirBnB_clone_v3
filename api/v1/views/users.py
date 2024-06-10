#!/usr/bin/python3
"""
"""
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    '''
        Retrieve all user objects
    '''
    user_list = []
    users = storage.all('User').values()
    for value in users:
        user_list.append = (value.to_dict())
    return jsonify(user_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''
        Retrieve one user object
    '''
    try:
        user = storage.get(User, user_id)
        return jsonify(user.to_dict())
    except Exception:
        return abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''
        Delete a User object
    '''
    try:
        user = storage.get(User, user_id)
        storage.delete(user)
        strorage.save()
        return jsonify({}), 200
    except Exception:
        return abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    '''
        Create a user object
    '''
    if not request.json:
        return abort(400, 'Not a JSON')
    if 'email' not in request.json:
        return abort(400, 'Missing email')
    if 'password' not in request.json:
        return abort(400, 'Missing password')
    new_user = request.get_json()

    user = User(**new_user)
    user.save()
    return (jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id=None):
    '''
        Update a user object
    '''
    obj_users = storage.get(User, user_id)
    if obj_user is None:
        return abort(404)
    if not request.json:
        return abort(400, 'Not a JSON')
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'email', 'updated_at']:
            setattr(obj_user, key, value)
    obj_user.save()
    return (jsonify(obj_user.to_dict()), 200)
