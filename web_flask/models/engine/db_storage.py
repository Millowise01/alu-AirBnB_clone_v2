#!/usr/bin/python3
"""
Module for DBStorage class.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """Interacts with MySQL database using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine."""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
        else:
            query_result = (
                self.__session.query(State).all()
                + self.__session.query(City).all()
                + self.__session.query(User).all()
                + self.__session.query(Place).all()
                + self.__session.query(Amenity).all()
                + self.__session.query(Review).all()
            )

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Add a new object to the session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the current session to ensure fresh data retrieval."""
        self.__session.remove()
