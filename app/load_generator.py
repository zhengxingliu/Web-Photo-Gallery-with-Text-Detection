from flask import render_template, request, session, url_for, redirect, g, jsonify
from app import webapp
from app.config import db_config
import mysql.connector
import hashlib, random, os

from wand.image import Image
from app.text_detection import text_detection


def connect_to_database():
    return mysql.connector.connect(user=db_config['user'],
                                   password=db_config['password'],
                                   host=db_config['host'],
                                   database=db_config['database'])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db


@webapp.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

