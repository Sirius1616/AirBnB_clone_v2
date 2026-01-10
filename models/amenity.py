#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity model that describes the resources or facilities available in the apartment"""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place = relationship('Place', secondary='place_amenity', back_populates='amenities')


