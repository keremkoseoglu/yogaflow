""" Yoga database module """
from typing import List
from yogaflow.reader import Reader
from yogaflow.yoga import yoga_class

class YogaDatabase:
    """ Yoga database class """
    def __init__(self, reader: Reader):
        self._reader = reader
        self.classes = reader.get_yoga_classes()
        self.pranayamas = reader.get_pranayamas()
        self.warmups = reader.get_warmups()
        self.asanas = reader.get_asanas()
        self.flows = reader.get_flows(self.asanas)
        self.meditations = reader.get_meditations()

    @property
    def yoga_class_list(self) -> List:
        """ Returns yoga classes as a list """
        output = []
        for yc_entry in self.classes:
            output.append(yc_entry.name)
        return output

    def get_yoga_class_by_name(self, name: str) -> yoga_class.YogaClass:
        """ Returns the given yoga class"""
        for yc_entry in self.classes:
            if yc_entry.name == name:
                return yc_entry
        return None
