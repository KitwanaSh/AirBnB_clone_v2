#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()



class BaseModel:
    """Defines the Base model  class.
    Attributes:
        id (sqlalchemy string): The basemodel id
        created_at (sqlalchemy datetime): The basemodel created time
        updated_at (sqlalchemy datetime): The basemodel updated time
    """
    
    id = Column(String(60), primary_key = True, nullable = False)
    created_at = Column(DateTime, nullable = False, default = datetime.utcnow())
    updated_at = Column(DateTime, nullable = False, default = datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            # from models import storage
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        """

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary
    
    def delete(self):
        """ Delete the current insatnce from the storage """
        models.storage.delete(self)
        
    def __str__(self):
        """ Returns a string representation of the instance """
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)