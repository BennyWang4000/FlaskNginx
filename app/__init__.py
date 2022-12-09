from flask import Flask
# from .api import api
from .home import home
import db
import api

app = Flask(__name__)

app.register_blueprint(home)
