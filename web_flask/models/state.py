#!/usr/bin/python3
"""
Module for State class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """Represents a state in the database."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Return list of City objects linked to this State (FileStorage only)."""
            from models import storage
            from models.city import City

            return [
                city for city in storage.all(City).values() if city.state_id == self.id
            ]
