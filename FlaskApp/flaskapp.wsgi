#!/usr/bin/python
import os
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
secrets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../secrets/flask.txt'))
with open(secrets_path, 'r') as f:
  application.secret_key = f.readline()
