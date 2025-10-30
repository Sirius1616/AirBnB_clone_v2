#!/usr/bin/env python
from sqlalchemy import create_engine
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """New engine for the model, that implements interaction with the database"""
    
    __engine = None
    __session = None

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}, pool_pre_ping=True')

        if os.getenv('HBNB_ENV') = 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querries all content of the database based in the classname"""
        if cls == None:
            obj = []

        for _classes in self.classes.values():
            obj.extend(self.__session.querry(_classes).all())

        else:
            self.__session.querry(cls).all()

    


