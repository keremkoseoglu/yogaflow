""" Data reader module """
from typing import List, Protocol
from yogaflow.yoga.asana import Asana
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.meditation import Meditation


class Reader(Protocol):
    """ Data reader protocol
    If you need to read yoga data from a different data source,
    you can simply derive a new class from this class and
    write your code there
    """
    def get_asanas(self) -> List[Asana]:
        """ Returns a list of asanas from the data source """

    def get_flows(self, asanas: List[Asana]) -> List[YogaFlow]:
        """ Returns a list of flows from the data source """

    def get_meditations(self) -> List[Meditation]:
        """ Returns a list of meditations from the data source """

    def get_pranayamas(self) -> List[Pranayama]:
        """ Returns a list of pranayamas from the data source """

    def get_yoga_classes(self) -> List[YogaClass]:
        """ Returns a list of yoga classes from the data source """
