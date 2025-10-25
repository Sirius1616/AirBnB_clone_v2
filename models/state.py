#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String,
from storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states
    name = Column(String(128), nullable= False)
    
    cities = relationship('cities', back_populates='state', cascade = 'all', delete)
    
    
