""" Warmup module """

class WarmUp: #pylint: disable=R0903
    """ Warmup model class
    Data source of this class is by default /data/warmup.json
    """

    def __init__(self, p_name: str = "", p_description: str = "", p_location: str = ""):
        self.name = p_name
        self.description = p_description
        self.location = p_location
