""" Meditation module """

class Meditation: #pylint: disable=R0903
    """ Meditation class
    Data source of this class is by default /data/meditation.json
    """
    def __init__(self, p_name: str = ""):
        self.name = p_name
