""" Flow generator module """
from typing import List, Protocol
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.asana import Asana
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.meditation import Meditation
from yogaflow.yoga.warmup import WarmUp


class Generator(Protocol): #pylint: disable=R0903
    """ Flow generator protocol
    If you need a new aogorhythm to generate yoga flows in the future,
    you can simply derive a new class from AbstractGenerator and write
    your code in there.
    """
    def generate(self, #pylint: disable=R0913
                 p_yoga_class: YogaClass,
                 p_pranayamas: List[Pranayama],
                 p_warmups: List[WarmUp],
                 p_asanas: List[Asana],
                 p_flows: List[YogaFlow],
                 p_meditations: List[Meditation]
                 ):
        """ Generates a new yoga flow
        You need to fill the public variables of p_yoga_class here
        """
