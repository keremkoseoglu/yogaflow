""" Yoga class module """
from typing import List
from dataclasses import dataclass
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.yoga_style import YogaStyle
from yogaflow.yoga.asana import AsanaDifficulty, AsanaStance
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.meditation import Meditation
from yogaflow.yoga.warmup import WarmUp

@dataclass
class YogaClass:  #pylint: disable=R0902, R0903
    """ Yoga class class
    This is the main output of the yoga flow generation.

    In other words; yogaflow.generator.abstract_generator is expected
    to fill an instance of YogaClass.

    Default generator implementation can be found under
    yogaflow.generator.primal_generator.
    """
    name: str = "Undefined"
    style: YogaStyle = YogaStyle.undefined
    difficulty: AsanaDifficulty = AsanaDifficulty.undefined
    duration: int = 0
    asana_duration: int = 0
    opening_pranayamas: List[Pranayama] = None
    warmups: List[WarmUp] = None
    asanas: List[YogaFlow] = None
    closing_pranayamas: List[Pranayama] = None
    meditation: Meditation = None
    sequence: List[AsanaStance] = None

    def __post_init__(self):
        if self.opening_pranayamas is None:
            self.opening_pranayamas = []

        if self.warmups is None:
            self.warmups = []

        if self.asanas is None:
            self.asanas = []

        if self.closing_pranayamas is None:
            self.closing_pranayamas = []

        if self.sequence is None:
            self.sequence = []
