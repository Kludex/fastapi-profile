from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from fastapi_profile import config


class DBSession:
    def __init__(self, engine: Engine):
        self.conn = engine.connect()
        self.db = Session(bind=self.conn)

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()
        self.conn.close()
