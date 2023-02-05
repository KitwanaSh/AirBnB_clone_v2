#!/usr/bin/python3
""" This is the main file storage for the clone
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}
    clsdict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "State": State, "User": User}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls = cls if not isinstance(cls, str) else self.clsdict.get(cls)
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = self.clsdict[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """to delete obj from __objects if it's inside"""
        if obj is not None:
            ob = f"{type(obj).__name__}.{obj.id}"
            if ob in self.__objects:
                del self.__objects[ob]

    def close(self):
        """deserializing the JSON file to objects
        """
        self.reload()
