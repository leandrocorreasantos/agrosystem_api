import logging


class LoggerService:
    def __init__(self, name: str = "app"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                    '[$(asctime)s] %(levelname)s %(filename)s:%(fileno)s in %(name)s: %(message)s'
                    )
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)
    
    def error(self, message: str):
        self.logger.error(message)
    
    def debug(self, message: str):
        self.logger.debug(message)
