#!/usr/bin/env python
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    cities = relationship('City', back_populates='places')
   
