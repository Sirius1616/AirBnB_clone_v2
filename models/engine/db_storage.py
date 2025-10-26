#!/usr/bin/env python


class DBStorage:
    """New engine for the model, that implements interaction with the database"""

    def __init__(self):
        self.__engine = None
        self.__session = None
        