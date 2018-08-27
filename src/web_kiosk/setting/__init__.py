import os


DEBUG = bool(os.getenv("DEBUG", False))

API_TEMPERATURE_PORT = os.getenv("API_TEMPERATURE_PORT", 80)
API_TRAIN_PORT = os.getenv("API_TRAIN_PORT", 80)
API_WEATHER_PORT = os.getenv("API_WEATHER_PORT", 80)
