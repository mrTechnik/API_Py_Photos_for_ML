from flask import Flask
from helpers.sqlalchemyclass import db
import yaml as y


# create Flask application
app = Flask("app")
# upload config.yaml
with open("config.yaml", "r") as f:
    config = y.safe_load(f)

# Init path for photo containing
app.config["UPLOAD_FOLDER"] = config['path']
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
