""" Meditation module """
from dataclasses import dataclass

@dataclass
class Meditation: #pylint: disable=R0903
    """ Meditation class
    Data source of this class is by default /data/meditation.json
    """
    name: str = ""
