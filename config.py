# import redis

# SESSION_REDIS = redis.from_url()

from os import environ, path, system

import redis
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,".env"))


FLASK_APP = environ.get("FLASK_APP")
FLASK_DEBUG = environ.get("FLASK_DEBUG")
SECRET_KEY = "testSecretKey"
SQLALCHEMY_DATABASE_URI = environ.get("MYSQL_CONFIG")


# REDIS_URI = environ.get("REDIS_URI")
# SESSION_TYPE = "redis"
SESSION_REDIS = redis.Redis(host="localhost", port=6379, db=0)