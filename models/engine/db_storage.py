#!/usr/bin/python3
""" Defines the database storage """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session


class DBStorage:
    """ Shows the the database storage engine
    Arguments:
        __init__: Create the MySQL engine
        all: Query the whole databse
        new: Add a new object
        save: Commit all the changes of the current database session
        ...: And much more
    """
    
    __engine = None
    __session = None
    
    def __init__(self):
        """ Create the engine  with self.__engine """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                     format(getenv("HBNB_MYSQL_USER"),
                                           getenv("HBNB_MYSQL_PWD"),
                                           getenv("HBNB_MYSQL_HOST"),
                                           getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """ Query on the current database session """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(ob).__name__, ob.id): ob for ob in objs}

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)
    
    def save(self):
        """ Commit the change made in the current database session """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__seesion.delete(obj)
    
    def reload(self):
        """ Create all tables in the database again
            Create the current database session again
        """
        Base.metadata.create_all(self.__engine)
        session_mk = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_mk)
        self.__session = Session()
        
    def close(self):
        """ Close the sqlalchemy database session """
        self.__session.close()
        