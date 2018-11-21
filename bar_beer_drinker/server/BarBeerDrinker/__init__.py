from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

import json

from BarBeerDrinker import database

app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_total():
    return jsonify(database.get_total())

@app.route("/api/bars",methods=["GET"])
def get_bars():
    return jsonify(database.get_bars())

@app.route("/api/bars/<name>",methods=["GET"])
def find_bars(name):
    try:
        if name is None:
            raise ValueError('Bar was not specified')
        bar = database.find_bars(name)
        if bar is None:
            return make_response("No bar with name was found",404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e),400)
    except Exception as e:
        return make_response(str(e),500)

@app.route("/api/bars/cheaper_than", methods =["POST"])
def find_beers():
    body = json.loads(request.data)
    max_price = body['maxPrice']
    return jsonify(database.filter_beers(max_price))