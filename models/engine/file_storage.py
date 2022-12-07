#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object from the list of objects if it exists.
        If obj is None, the method does nothing.
        """
        if obj is not None:
            # check if the object is in the list of objects
            if obj in self.__objects.values():
                # delete the object from the list of objects
                del self.__objects[obj.id]
                # save the changes to the JSON file
                self.save()

    def all(self, cls=None):
        """
        Returns a list of all objects in the storage.
        If cls is specified, the list will only contain objects of the given 
        class.
        """
        # if no class is specified, return a list of all objects
        if cls is None:
            return list(self.__objects.values())

        # if a class is specified, return a list of objects of that class
        else:
            # create an empty list for objects of the given class
            obj_list = []
            # iterate over the objects in the storage
            for obj in self.__objects.values():
                # check if the object is an instance of the given class
                if isinstance(obj, cls):
                    # add the object to the list
                    obj_list.append(obj)

            return obj_list

