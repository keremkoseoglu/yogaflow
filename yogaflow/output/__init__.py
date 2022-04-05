""" Output module """
from enum import Enum
from typing import List

class Output(Enum):
    """ Output (writer) enum """
    HTML = 1
    IMG_HTML = 2

def get_output_dict() -> List:
    """ Returns outputs """
    output = []
    for enum_entry in Output:
        entry = {"name": enum_entry.name,
                 "value": enum_entry.value}
        output.append(entry)
    return output
