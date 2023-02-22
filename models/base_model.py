#!/usr/bin/python3
""" base model """
from datetime import datetime
import uuid


class BaseModel:
    """ base model class """

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs["created_at"] = datetime.strptime(str(kwargs['created_at']),
                                                     "%Y-%m-%dT%H:%M:%S.%f")

            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
