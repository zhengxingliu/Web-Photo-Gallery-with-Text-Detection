from flask import Flask

webapp = Flask(__name__)

#from app import main
from app import user
from app import photo
from app import load_generator


webapp.secret_key = 'bf7\xf3MP\xe1\x00}\xaf\xffk5\xeb\xb7\xe7o\xda\x05\x10\xcb\x0b\xff\x03'