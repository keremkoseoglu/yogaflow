""" Warmup module """
from dataclasses import dataclass

@dataclass
class WarmUp: #pylint: disable=R0903
    """ Warmup model class
    Data source of this class is by default /data/warmup.json
    """
    name: str = ""
    description: str = ""
    location: str = ""
