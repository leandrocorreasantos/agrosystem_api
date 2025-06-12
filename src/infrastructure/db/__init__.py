from src.config.app_factory import create_app


_, db = create_app()

Base = db.Model
# from .models import d b # noqa
