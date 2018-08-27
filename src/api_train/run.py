import json
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

from setting import DEBUG, VERSION, DB_HOST, DB_PORT


app = Flask(__name__)
app.config.update({'DEBUG': DEBUG})
CORS(app)


@app.route("/api", methods=['GET'])
def get_api_info():
    return jsonify({
        "version": VERSION
    }), 200


@app.route("/api/departure/<departure_id>", methods=['GET'])
def get_departure_detail(departure_id=None):
    client = MongoClient(DB_HOST, DB_PORT)
    db = client["train"]
    collection = db["departure" if departure_id is None else "departure/%s" % departure_id]
    data = []
    for post in collection.find():
        post["_id"] = str(post["_id"])
        data.append(post)
    return jsonify(data), 200


@app.route("/api/departure", methods=['GET'])
def get_departure_master():
    return get_departure_detail()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
