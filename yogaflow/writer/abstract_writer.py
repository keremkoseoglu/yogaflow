""" Abstract output generator module """
from abc import ABC, abstractmethod
from yogaflow.yoga.yoga_class import YogaClass


class AbstractWriter(ABC): #pylint: disable=R0903
    """ Abstract file writer class
    In case you need to generate a different output in the future;
    you can simply derive a new class and use in your project.
    """

    @abstractmethod
    def write(self, generated_class: YogaClass):
        """ Generates the desired output """
