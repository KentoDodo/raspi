import threading, json
from flask import Flask, jsonify
from flask_cors import CORS

from setting import DEBUG, VERSION
from util.jma_radar import JmaRadar
from util.temp_handler import get_from_temp


app = Flask(__name__)
app.config.update({'DEBUG': DEBUG})
CORS(app)


@app.route("/api", methods=['GET'])
def get_api_info():
    return jsonify({
        "version": VERSION
    }), 200


@app.route("/api/jma_radar", methods=['GET'])
def get_jma_radar():
    return jsonify(get_from_temp()), 200


if __name__ == "__main__":
    JmaRadar(area=JmaRadar.AREA_KANTO).get_latest_start()
    app.run(host='0.0.0.0', port=80)
