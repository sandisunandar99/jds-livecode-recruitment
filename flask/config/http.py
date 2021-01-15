from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from helpers import mysql_alchemy
import routes

cors = CORS()
compress = Compress()

def createApp(configuration):
    app = Flask(__name__)

    # register route blueprint
    app.register_blueprint(routes.index.bp)
    app.register_blueprint(routes.employe.bp)

    # load configuration
    app.config.from_object(configuration)

    # init app
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    compress.init_app(app)
    mysql_alchemy.init_app(app)

    return app
