# models/__init__.py
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
