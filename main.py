from flask import Flask, Response, jsonify, make_response, render_template, Blueprint
from flask_pymongo import PyMongo
import sys

import app
from app import app


if __name__ == "__main__":
    app.run(host="127.0.0.1", port='8001')
