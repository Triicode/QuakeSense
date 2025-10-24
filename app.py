import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "devsecret")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# configure the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'earthquakes.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path.replace(os.sep, '/')}"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 300, "pool_pre_ping": True}

db.init_app(app)

# Import routes after app initialization
from routes import *  # noqa: F401, F403

# (Commented out to avoid overwriting existing DB)
# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
