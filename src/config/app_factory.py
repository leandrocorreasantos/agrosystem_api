from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from src.config.config import Config


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://postgres:postgres@db:5432/app_db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db = SQLAlchemy()

    db.init_app(app)

    app.config.from_object(Config)

    return app, db

