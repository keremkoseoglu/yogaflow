""" Yoga database module """
from yogaflow.reader.abstract_reader import AbstractReader

class YogaDatabase:
    """ Yoga database class """
    def __init__(self, reader: AbstractReader):
        self._reader = reader
        self.classes = reader.get_yoga_classes()
        self.pranayamas = reader.get_pranayamas()
        self.warmups = reader.get_warmups()
        self.asanas = reader.get_asanas()
        self.flows = reader.get_flows(self.asanas)
        self.meditations = reader.get_meditations()
