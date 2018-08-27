import os
from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap

from setting import DEBUG, API_TEMPERATURE_PORT, API_TRAIN_PORT, API_WEATHER_PORT


app = Flask(__name__)
app.config.update({'DEBUG': DEBUG, 'TEMPLATES_AUTO_RELOAD': True})
bootstrap = Bootstrap(app)


@app.route("/", methods=['GET'])
def index():
    html = render_template('index.html', api_ports={
        "temperature": API_TEMPERATURE_PORT,
        "train": API_TRAIN_PORT,
        "weather": API_WEATHER_PORT
    })
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
