#!/usr/bin/python3
""" FileStorage class definition"""
import json
from models.base_model import BaseModel
from os.path import exists
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objclass_name = obj.__class__.__name__
        self.__objects["{}.{}".format(objclass_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict = self.__objects
        objdict = {obj: dict[obj].to_dict() for obj in dict.keys()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
