#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.DBStorage import DBStorage

storage = FileStorage()
storage.reload()
