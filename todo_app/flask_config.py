import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        self.LOG_LEVEL = os.environ.get('LOG_LEVEL')
        if self.LOG_LEVEL == None :
            self.LOG_LEVEL = "INFO"