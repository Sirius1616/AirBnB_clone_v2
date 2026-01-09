#!/usr/bin/env python
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,ForeignKey, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    users = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    reviews = relationship('Review', back_populates='places')
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Integer, nullable=False, default=0)
    longitude = Column(Integer, nullable=False, default=0)



   
