#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
with open('../secrets/flask.txt', 'r') as f:
  application.secret_key = f.readline()
