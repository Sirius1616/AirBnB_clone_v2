#!/usr/bin/env python


class DBStorage:
    """New engine for the model, that implements interaction with the database"""

    def __init__(self, engine=None, session=None):
        self.__engine = engine
        self.__session = session