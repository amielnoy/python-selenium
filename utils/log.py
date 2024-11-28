import logging
from logging.handlers import TimedRotatingFileHandler

class LoggerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        self.logger = logging.getLogger('LoggerSingleton')
        self.logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # File handler with daily rotation
        file_handler = TimedRotatingFileHandler('app.log', when='midnight', interval=1, backupCount=7)
        file_handler.setLevel(logging.DEBUG)

        # Formatter for both handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    @staticmethod
    def get_logger():
        return LoggerSingleton().logger

# Example usage
logger = LoggerSingleton.get_logger()
logger.info("This is an info message.")
logger.error("This is an error message.")
