#!/usr/bin/python3
"""Class of file storage"""

import uuid
from json import dumps, load, dump
from os.path import exists
from models import base_model, user, place, state, city, amenity, review

BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
name_class = ["BaseModel", "City", "State", "Place", "Amenity", "Review", "User"]


class FileStorage:
    """Store user input files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All initialization"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets  the obj with key in __objects"""
        class_name = obj.__class__.__name__
        id = obj.id
        clas_id = class_name + "." + id
        FileStorage.__objects[clas_id] = obj

    def save(self):
        """Saving file to storage"""
        userDictionary_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding='utf-8') as fileToReturn:
                dump(userDictionary_to_json, fileToReturn)

    def reload(self):
        """Deserializes the JSON file"""
        obj_dict = {}
        FileStorage.__object = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fileToLoad:
                obj_dict = load(fileToLoad)
                for key, value in obj_dict.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
        else:
            pass
