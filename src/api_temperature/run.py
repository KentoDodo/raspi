import threading
from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from setting import DEBUG, VERSION
from util.dht11_run import dht11_run
from util.ds18b20 import read_temp
from util.temp_handler import get_from_temp


app = Flask(__name__)
app.config.update({'DEBUG': DEBUG})
bootstrap = Bootstrap(app)
CORS(app)


@app.route("/", methods=['GET'])
def index():
    html = render_template('index.html')
    return html


@app.route("/api", methods=['GET'])
def get_api_info():
    return jsonify({
        "version": VERSION
    }), 200


@app.route("/api/temperature", methods=['GET'])
def get_temperature():
    data = get_from_temp()
    data["temperature2"] = read_temp()
    return jsonify(data), 200


if __name__ == "__main__":
    th1 = threading.Thread(target=dht11_run)
    th1.start()
    app.run(host='0.0.0.0', port=80)
