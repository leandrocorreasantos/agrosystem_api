import os


class Config:
    DEBUG=os.environ.get("DEBUG", False)
    HOST=os.environ.get("HOST", "0.0.0.0")
    PORT=os.environ.get("PORT", "5000")
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
