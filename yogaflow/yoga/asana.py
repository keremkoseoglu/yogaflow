""" Asana module """
from enum import Enum
from typing import List
from yogaflow.yoga.yoga_style import YogaStyle


class AsanaDifficulty(Enum):
    """ Asana difficulties """
    undefined = 0
    beginner = 1
    intermediate = 2
    advanced = 3


def is_difficulty_higher(supposedly_low: AsanaDifficulty, supposedly_high: AsanaDifficulty) -> bool:
    """ Compares two asanas and tells if the second one is more difficult than the first one """
    output = False
    if supposedly_low == AsanaDifficulty.undefined:
        if supposedly_high != AsanaDifficulty.undefined:
            output = True
    elif supposedly_low == AsanaDifficulty.beginner:
        if supposedly_high in (AsanaDifficulty.intermediate, AsanaDifficulty.advanced):
            output = True
    elif supposedly_low == AsanaDifficulty.intermediate:
        if supposedly_high == AsanaDifficulty.advanced:
            output = True
    elif supposedly_low == AsanaDifficulty.advanced:
        output = False
    return output


def str_to_asana_difficulty(name: str) -> AsanaDifficulty:
    """ Converts a string to asana difficulty enum """
    if name == AsanaDifficulty.beginner.name:
        return AsanaDifficulty.beginner
    if name == AsanaDifficulty.intermediate.name:
        return AsanaDifficulty.intermediate
    if name == AsanaDifficulty.advanced.name:
        return AsanaDifficulty.advanced
    return AsanaDifficulty.undefined


class AsanaStance(Enum):
    """ Asana stance definitions """
    undefined = 0
    standing = 1
    seated = 2
    lying = 3


def str_to_asana_stance(name: str) -> AsanaStance:
    """ Convers a string to asana stance enum """
    if name == AsanaStance.standing.name:
        return AsanaStance.standing
    if name == AsanaStance.seated.name:
        return AsanaStance.seated
    if name == AsanaStance.lying.name:
        return AsanaStance.lying
    return AsanaStance.undefined


class Asana: #pylint: disable=R0903
    """ Asana model class
    Data source of this class is by default /data/asana.json
    """
    def __init__(self,
                 p_name: str = "Undefined",
                 p_difficulty: AsanaDifficulty = AsanaDifficulty.undefined,
                 p_stance: AsanaStance = AsanaStance.undefined,
                 p_styles: List[YogaStyle] = None):

        self.name = p_name
        self.difficulty = p_difficulty
        self.stance = p_stance
        if p_styles is None:
            self.styles = []
        else:
            self.styles = p_styles
