from flask import Flask
from .api import api
from .home import home

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(api)
