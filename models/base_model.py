#!/usr/bin/pyhon3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def _init_(self, *args, **kwargs):
        """initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 
'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '_class_':
                    setattr(self, key, value)

    def _str_(self):
        """returns class name, id and attribute dictionary
        """
        class_name = "[" + self._class.__name_ + "]"
        dct = {k: v for (k, v) in self._dict_.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """updates last update time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datemtimes converted to strings
        """
 new_dict = {}

        for key, values in self._dict_.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['_class'] = self.__class.__name_

        return new_dict

