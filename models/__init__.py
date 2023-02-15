#!/usr/bin/python3
"""Module to initialize this new package"""

from models.engine.file_storage import FileStorage

"""Initialize the Storage from the File"""
storage = FileStorage()
storage.reload()
