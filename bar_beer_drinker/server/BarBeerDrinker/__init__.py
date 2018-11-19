from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect

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
            return
