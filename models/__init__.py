#!/usr/bin/python3
"""__init__ to create instance of a unique file storage"""
from models.engine.file_storage import Filestorage


storage = Filestorage()
storage.reload()