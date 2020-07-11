""" Yoga class module """
from typing import List
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.yoga_style import YogaStyle
from yogaflow.yoga.asana import AsanaDifficulty, AsanaStance
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.meditation import Meditation
from yogaflow.yoga.warmup import WarmUp


class YogaClass:  #pylint: disable=R0902, R0903
    """ Yoga class class
    This is the main output of the yoga flow generation.

    In other words; yogaflow.generator.abstract_generator is expected
    to fill an instance of YogaClass.

    Default generator implementation can be found under
    yogaflow.generator.primal_generator.
    """

    def __init__(self,
                 p_name="Undefined",
                 p_style=YogaStyle.undefined,
                 p_difficulty=AsanaDifficulty.undefined,
                 p_duration=0,
                 p_asana_duration=0,
                 p_opening_pranayamas: List[Pranayama] = None,
                 p_warmups: List[WarmUp] = None,
                 p_asanas: List[YogaFlow] = None,
                 p_closing_pranayamas: List[Pranayama] = None,
                 p_meditation: Meditation = None,
                 p_sequence: List[AsanaStance] = None
                 ):  #pylint: disable=R0913

        self.name = p_name
        self.style = p_style
        self.difficulty = p_difficulty
        self.duration = p_duration
        self.asana_duration = p_asana_duration

        if p_opening_pranayamas is None:
            self.opening_pranayamas = []
        else:
            self.opening_pranayamas = p_opening_pranayamas

        if p_warmups is None:
            self.warmups = []
        else:
            self.warmups = p_warmups

        if p_asanas is None:
            self.asanas = []
        else:
            self.asanas = p_asanas

        if p_closing_pranayamas is None:
            self.closing_pranayamas = []
        else:
            self.closing_pranayamas = p_closing_pranayamas

        if p_sequence is None:
            self.sequence = []
        else:
            self.sequence = p_sequence

        self.meditation = p_meditation
