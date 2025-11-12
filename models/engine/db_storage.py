#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base



class DBStorage:
    """New engine for the model, that implements interaction with the database"""
    
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)

        if getenv('HBNB_ENV') == 'test':
           Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name."""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'User': User, 'Place': Place, 'State': State,
            'City': City, 'Review': Review
        }

        objects = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls and hasattr(cls, '__tablename__'):
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            for clss in classes.values():
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds object to the current database session"""
        self.__session.add(obj)

    
    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()



