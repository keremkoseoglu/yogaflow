""" Pranayama module """
from enum import Enum
from dataclasses import dataclass


class PranayamaCategory(Enum):
    """ Pranayama categories """
    undefined = 0
    cleansing = 1
    stimulant = 2
    cooling = 3
    harmony = 4
    refreshing = 5
    binding = 6
    enlightening = 7


class PranayamaLocation(Enum):
    """ Pranayama locations """
    undefined = 0
    opener = 1
    closer = 2


@dataclass
class Pranayama: #pylint: disable=R0903
    """ Pranayama model class
    Data source of this class is by default /data/pranayama.json
    """
    name: str = ""
    category: PranayamaCategory = PranayamaCategory.undefined
    opener: bool = False
    closer: bool = False
