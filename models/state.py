#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,
from storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    t_storage = getenv('HBNB_TYPE_STORAGE')

    __tablename__ = 'states
    name = Column(String(128), nullable= False)

    if t_storage == 'DB':
        cities = relationship('cities', backref='state', cascade = 'all, delete, delete-orphan')
    
    else:
        @property
        """Return list of city instances with state_id equal to current State"""
        def cities(self):
            from models.city import cities

            city_list = []
            for city in models.storage.all(City).value():
                if cities.state_id == self.id:
                    city_list.append(city)
            return city_list

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


    
