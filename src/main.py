from src.config.app_factory import create_app
from src.config.config import Config
from src.api.controllers.cultura_controller import cultura_bp
from src.api.controllers.produtor_controller import produtor_bp
from src.api.controllers.propriedade_controller import propriedade_bp
from src.api.controllers.safra_controller import safra_bp


def create_flask_app():
    app, _ = create_app()
    app.register_blueprint(cultura_bp)
    app.register_blueprint(produtor_bp)
    app.register_blueprint(propriedade_bp)
    app.register_blueprint(safra_bp)
    return app

if __name__=='__main__':
    app = create_flask_app()
    app.run(host=Config.HOST, debug=Config.DEBUG)
