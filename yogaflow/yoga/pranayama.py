""" Pranayama module """
from enum import Enum


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


class Pranayama: #pylint: disable=R0903
    """ Pranayama model class
    Data source of this class is by default /data/pranayama.json
    """

    def __init__(self,
                 p_name="",
                 p_category=PranayamaCategory.undefined,
                 p_opener=False,
                 p_closer=False):
        self.name = p_name
        self.category = p_category
        self.opener = p_opener
        self.closer = p_closer
