from flask import Flask
import pymongo

app = Flask(__name__)

from setserver import routes
