#!/usr/bin/python3

""" Base class """


import json


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_disctionaries """
        if list_dictionaries is None:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as f:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in
                    list_objs])
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            json_string = []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        else:
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as f:
                contents = cls.from_json_string(f.read())
                return [cls.create(**d) for d in contents]

        except FileNotFoundError:
            return []
