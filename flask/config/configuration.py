import os
from datetime import timedelta

from dotenv import load_dotenv, find_dotenv

# Load environment
load_dotenv(find_dotenv())

# get absolute path static directory in root project
log_folder = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'log'))

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DB = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

class Configuration(object):
    # Basic
    DEBUG = os.getenv("DEBUG") == "True"
    PORT = int(os.getenv("PORT", 5000))

    URI = "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
        DB_USER=MYSQL_USER, DB_PASSWORD=MYSQL_PASSWORD, DB_HOST=MYSQL_HOST, DB_PORT=MYSQL_PORT, DB_NAME=MYSQL_DB)

    # MYSQL
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_RECORD_QUERIES = True

    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("MYSQL_TRACK_MODIFICATIONS")
