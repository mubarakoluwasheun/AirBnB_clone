#!/usr/bin/python3
"""used to create instance of a unique file storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
