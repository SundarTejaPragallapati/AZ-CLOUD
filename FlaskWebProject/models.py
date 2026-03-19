"""
Database models.
"""

from datetime import datetime
from FlaskWebProject import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from azure.storage.blob import BlobServiceClient
from flask import current_app


# ======================================================
# USER MODEL
# ======================================================

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))

    # ---- Password methods ----
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# ---- Required for Flask-Login ----
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# ======================================================
# POST MODEL
# ======================================================

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(64))
    body = db.Column(db.Text)
    image_path = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # --------------------------------------------------
    # SAVE POST + IMAGE TO AZURE BLOB STORAGE
    # --------------------------------------------------
    def save_changes(self, form, image_file, user_id, new=False):

        self.title = form.title.data
        self.author = form.author.data
        self.body = form.body.data

        # ---- Upload image if provided ----
        if image_file and image_file.filename != "":

            blob_service = BlobServiceClient.from_connection_string(
                current_app.config["BLOB_CONNECTION_STRING"]
            )

            blob_client = blob_service.get_blob_client(
                container=current_app.config["BLOB_CONTAINER"],
                blob=image_file.filename
            )

            blob_client.upload_blob(image_file, overwrite=True)

            self.image_path = image_file.filename

        if new:
            db.session.add(self)

        db.session.commit()