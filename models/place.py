#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    city_id = Column(String(128), ForeignKey('cities.id'), nullable=False)
   
