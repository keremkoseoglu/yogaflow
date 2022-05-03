""" Abstract output generator module """
from abc import ABC, abstractmethod
import os
from typing import Protocol
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.config import get as get_config

class Writer(Protocol):
    """ Abstract file writer class
    In case you need to generate a different output in the future;
    you can simply derive a new class and use in your project.
    """
    def write(self, generated_class: YogaClass):
        """ Generates the desired output """

class AbstractWriter(ABC, Writer): #pylint: disable=R0903
    """ Abstract file writer class
    In case you need to generate a different output in the future;
    you can simply derive a new class and use in your project.
    """
    @abstractmethod
    def write(self, generated_class: YogaClass):
        """ Generates the desired output """

    def _display_file(self, file_path: str):
        config = get_config()
        if "CUSTOM_BROWSER" in config:
            if config["CUSTOM_BROWSER"] != "":
                chrome_cmd = f"open {config['CUSTOM_BROWSER']}" \
                             f" --args {file_path}"
                os.system(chrome_cmd)
                return
        os.system(f"open {file_path}")
