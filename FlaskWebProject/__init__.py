"""
The flask application package.
"""

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix  # Azure HTTPS support

# -------------------------------------------------
# Create Flask app
# -------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# -------------------------------------------------
# Fix HTTPS issues behind Azure reverse proxy
# -------------------------------------------------
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# -------------------------------------------------
# PRODUCTION LOGGING — REQUIRED FOR AZURE LOG STREAM
# -------------------------------------------------
if not app.debug:
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.info("CMS app startup")

# -------------------------------------------------
# Extensions
# -------------------------------------------------
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# -------------------------------------------------
# Import routes
# -------------------------------------------------
import FlaskWebProject.views