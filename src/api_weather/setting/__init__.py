import os


DEBUG = bool(os.getenv("DEBUG", False))
VERSION = os.getenv("VERSION", None)
API_WEATHER_PORT = int(os.getenv("API_WEATHER_PORT", 80))

TEMP_DIR_PATH = "temp"
