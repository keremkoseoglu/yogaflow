""" Abstract data reader module """
from abc import ABC, abstractmethod
from typing import List
from yogaflow.yoga.asana import Asana
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.meditation import Meditation


class AbstractReader(ABC):
    """ Abstract data reader class
    If you need to read yoga data from a different data source,
    you can simply derive a new class from this class and
    write your code there
    """

    @abstractmethod
    def get_asanas(self) -> List[Asana]:
        """ Returns a list of asanas from the data source """

    @abstractmethod
    def get_flows(self) -> List[YogaFlow]:
        """ Returns a list of flows from the data source """

    @abstractmethod
    def get_meditations(self) -> List[Meditation]:
        """ Returns a list of meditations from the data source """

    @abstractmethod
    def get_pranayamas(self) -> List[Pranayama]:
        """ Returns a list of pranayamas from the data source """

    @abstractmethod
    def get_yoga_classes(self) -> List[YogaClass]:
        """ Returns a list of yoga classes from the data source """
