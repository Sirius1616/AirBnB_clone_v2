#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, 


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states
    name = Column(String(128), nullable=False)
    if storage == 'db':
        cities = relationship('City', back_populates='state', cascade='all', delete)
    else:
        @property
        def cities(self):
            all_cities = storage.all(City).values()

            return [city for city in all_cities if city.state_id == self.id
    
