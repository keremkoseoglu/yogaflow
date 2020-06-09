""" Yoga style module """
from enum import Enum
from typing import List


class YogaStyle(Enum):
    """ Yoga style enum """
    undefined = 0
    hatha = 1
    yin = 2
    chair = 3


def get_all_yoga_styles() -> List[YogaStyle]:
    """ Returns a list of all yoga styles in the enum """
    return [YogaStyle.hatha, YogaStyle.yin, YogaStyle.chair]


def str_to_yoga_style(name: str) -> YogaStyle:
    """ Converts a string to yoga style enum """
    if name == YogaStyle.chair.name:
        return YogaStyle.chair
    if name == YogaStyle.hatha.name:
        return YogaStyle.hatha
    if name == YogaStyle.yin.name:
        return YogaStyle.yin
    return YogaStyle.undefined
