#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        o_c_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(o_c_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        object_dict = FileStorage.__objects
        dict_object = {obj: object_dict[obj].to_dict() for obj in object_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_object, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                dict_object = json.load(f)
                for obj in dict_object.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
