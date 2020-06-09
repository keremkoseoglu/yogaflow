""" Yoga flow module """
from copy import deepcopy
from typing import List
from yogaflow.yoga.asana import Asana, AsanaDifficulty, is_difficulty_higher
from yogaflow.yoga.yoga_style import YogaStyle, get_all_yoga_styles


class YogaFlow:
    """ Yoga flow class
    This class describes a predefined yoga flow.
    Source of this class is by default /data/flow.json
    """

    def __init__(self,
                 p_name="Undefined",
                 p_asanas: List[Asana] = None
                 ):
        self.name = p_name

        if p_asanas is None:
            self.asanas = []
        else:
            self.asanas = p_asanas

    def get_compatible_styles(self) -> List[YogaStyle]:
        """ Returns a list of yoga styles where this particular flow can be used """
        output = []
        if len(self.asanas) > 0:
            output = get_all_yoga_styles()
            for asana in self.asanas:
                expected_styles = deepcopy(output)
                for expected_style in expected_styles:
                    if expected_style not in asana.styles:
                        output.remove(expected_style)
        return output

    def get_highest_difficulty(self) -> AsanaDifficulty:
        """ Returns the difficulty of the most difficult asana in the flow """
        output = AsanaDifficulty.undefined
        for asana in self.asanas:
            if is_difficulty_higher(output, asana.difficulty):
                output = asana.difficulty
        return output
