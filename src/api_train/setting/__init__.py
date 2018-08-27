import os


DEBUG = bool(os.getenv("DEBUG", False))
VERSION = os.getenv("VERSION", None)

DB_HOST = os.getenv("DB_HOST", None)
DB_PORT = int(os.getenv("DB_PORT", None))
