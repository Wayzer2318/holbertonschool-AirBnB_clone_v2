#!/usr/bin/python3
""" engine storage """
from models.base_model import BaseModel
import json


class FileStorage:
    """ file storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ saves filestorage to json file """
        ndict = {}

        for key, value in FileStorage.__objects.items():
            ndict[key] = value.to_dict()
        
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ndict, f)

    def reload(self):
        """ deserializes the json file """
        try:
            with open(FileStorage.__file_path, "r",
                      encoding='utf-8') as read_file:
                type(self).__objects = json.load(read_file)
            for key, value in type(self).__objects.items():
                obj = eval(type(self).__objects[key]['__class__'])(**value)
                type(self).__objects[key] = obj

        except FileNotFoundError:
            pass
