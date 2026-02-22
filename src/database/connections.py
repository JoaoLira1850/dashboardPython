
from sqlalchemy import create_engine
from .config import settings

class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(settings.database_url)
        pass
    def get_engine(self):
        return self.engine