import os


DEBUG = bool(os.getenv("DEBUG", False))
VERSION = os.getenv("VERSION", None)

GPIO_PIN_DHT11 = 22

TEMP_DIR_PATH = "temp"
