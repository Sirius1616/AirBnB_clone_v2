#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, relationship, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=True)
    place_id = Column(String(60), nullable=False, ForeignKey='places.id')
    user_id = Column(String(60), nullable=False, ForeignKey='user.id')
    place = relationship('Place', back_populates='review')
    users = relationship('User', back_populates='reviews')


