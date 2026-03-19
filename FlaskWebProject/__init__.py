"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix  # ✅ Added for Azure HTTPS support

app = Flask(__name__)
app.config.from_object(Config)

# ✅ Required for Azure App Service (fixes HTTP → HTTPS issue behind proxy)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# TODO: Add any logging levels and handlers with app.logger
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views