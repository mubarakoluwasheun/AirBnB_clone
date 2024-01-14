#!/usr/bin/python3
"""Defines the class for BaseModel."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The base model class for the project"""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.
        
        Args:
            *args (any): Takes any number of positional Arguments (Unused).
            **kwargs (dict): key and value pair of attributes.
        """
        
        time_form = "%Y-%m-%dT%H:%M:%S>%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)               
                else:
                     self.__dict__[k] = v    
        else:
                    models.storage.new(self)

def __str__(self):
    """
    Returns the str representation of the BaseModel instance in a format
    """
    class_name = self.__class__.__name__
    return f"[{class_name}] ({self.id}) {self.__dict__}"

def save(self):
    """ updates the public instance attribute
    updated_at with the current datetime
    """
    self.updated_at = datetime.now()
    models.storage.save()

def to_dict(self):
    """
    returns a dictionary containing all
    keys/values of __dict__ of the instance
    """
    ret_dict = self.__dict__.copy()
    ret_dict["__class__"] = self.__class__.__name__
    ret_dict["created_at"] = self.created_at.isoformat()
    ret_dict["updated_at"] = self.updated_at.isoformat()
    return ret_dict