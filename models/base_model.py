#!/usr/bin/python3
""" Writing a base model for class attributes"""

import uuid
from datetime import datetime
from uuid import uuid4
import models
import json

format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Basemodel class"""
    def __init__(self, *args, **kwargs):
        """Database initialization"""
        if args is not None and  len(args) > 0:
            pass
        if **kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """Defining a dictionary"""
        userDictionary = {}
        for key, value in self.__dict__.items():
             if key in ['created_at', 'updated_at']:
                 userDictionary[key] = item
        userDictionary['__class__'] = self.__class__.__name__
        userDictionary['created_at'] = self.created_at.isoformat()
        userDictionary['updated_at'] = self.updated_at.isoformat()
        return userDictionary

    def __str__(self):
        """Return a string defination of entered items"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """ Save definition """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
