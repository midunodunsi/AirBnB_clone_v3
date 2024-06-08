#!/usr/bin/python3
"""
module index
- app_views router
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """ returns count of objects"""
    dic = {}
    obj = ["amenities", "cities", "places", "reviews", "states", "users"]
    for key in obj:
        dic[key] = storage.count(key)
    return jsonify(dic)
