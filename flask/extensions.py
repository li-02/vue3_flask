# flask-sqlalchemy
# To resolve circular references, we will create the extensions.py file to hold the db object.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
