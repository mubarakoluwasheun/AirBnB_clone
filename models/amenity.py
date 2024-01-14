#!/usr/bin/python3
""" The amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent the amenity class.
    
    Attribute:
        name (str): The name of the amenity
    """
    name = ""