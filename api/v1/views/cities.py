#!/usr/bin/python3
"""
"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.city import City
from models.state import State
from models import storage


@app_views.route('/api/v1/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """ Retrieves the list of all City objects of a State """
    states = storage.all("State").value
    state = [obj.to_dict() for obj in states if obj.id == state_id]
    if not state:
        abort(404)

    cities = [obj.to_dict() for obj in storage.all("City").values()
              if state_id == obj.state_id]
    return jsonify(cities)


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ Retrieves a City object """
    cities = [obj.to_dict() for obj in storage.all("City").values()
              if state_id == obj.state_id]
    if cities == []:
        abort(404)
    return jsonify(cities[0])


@app_views.route('/api/v1/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """ Deletes a City objec """
    cities = strorage.all("City").values()
    city_obj = [obj.dict() for obj in cities if obj.id == city_id]

    if city_obj == []:
        abort(404)

    city_obj.remove(city_obj[0])
    for obj in cities:
        if city_id == obj.id:
            storage.delete(obj)
            storage.save()
    return (jsonify({}), 200)


@app_views.route('/api/v1/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """ Creates a City """
    if not request.get_json:
        abort(400, 'NOT a JSON')
    if 'name' not in request.get_json:
        abort(400, 'Missing name')
    states = [obj.to_dict() for obj in storage.all("State").values()
              if obj.id == state_id]
    if not states:
        abort(404)

    new_city = City(name=request.json['name'], state_id=state_id)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/api/v1/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """ Updates a City object """
    city = storage.all("City").values()
    cities = [obj.to_dict() for obj in city
              if obj.id == city_id]
    if not cities:
        abort(404)
    if not request.get_json:
        abort(400, 'NOT a JSON')
    lists = []
    for obj in city:
        if obj.id == city_id:
            obj.name = request.json['name']
            lists.append(obj.to_dict())
    storage.save()
    return jsonify(city_obj[0], 200)
