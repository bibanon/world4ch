#!/usr/bin/python3
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)		# using SQLAlchemy for database management

from app import views, models