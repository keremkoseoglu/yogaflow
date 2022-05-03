""" JSON data reader module """
import json
import os
from typing import List
from yogaflow.reader import Reader
from yogaflow.yoga.asana import Asana, str_to_asana_difficulty, \
    str_to_asana_stance, str_to_bend_direction, str_to_face_direction
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.yoga_style import YogaStyle, str_to_yoga_style
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.meditation import Meditation
from yogaflow.yoga.warmup import WarmUp
from yogaflow import config


class JsonReader(Reader):
    """ JSON data reader class
    Reads data from JSON files.
    Sample JSON files can hopefully be found under /data
    """
    def __init__(self):
        self._config = config.get()

    def get_asanas(self) -> List[Asana]:
        """ Reads the asana JSON file from the disk and returns a list """
        output = []
        path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["ASANA_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(path) as asana_file:
            asana_json = json.load(asana_file)
        for asa in asana_json:
            asana = Asana(
                name=asa["name"],
                difficulty=str_to_asana_difficulty(asa["difficulty"]),
                stance=str_to_asana_stance(asa["stance"]),
                bend_direction=str_to_bend_direction(asa["bend"]),
                face_direction=str_to_face_direction(asa["face"]))
            for stance in asa["styles"]:
                asana.styles.append(YogaStyle(str_to_yoga_style(stance)))
            output.append(asana)
        return output

    def get_flows(self, asanas: List[Asana]) -> List[YogaFlow]:
        """ Reads the flow JSON file from the disk and returns a list """
        output = []
        path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["FLOW_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(path) as flow_file:
            flow_json = json.load(flow_file)
        for flow_line in flow_json:
            yoga_flow = YogaFlow(p_name=flow_line["name"])
            for asana in flow_line["asanas"]:
                found = False
                for candidate in asanas:
                    if candidate.name == asana:
                        yoga_flow.asanas.append(candidate)
                        found = True
                        break
                assert found
            output.append(yoga_flow)
        return output

    def get_meditations(self) -> List[Meditation]:
        """ Reads the meditation JSON file from the disk and returns a list """
        output = []
        path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["MEDITATION_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(path) as meditation_file:
            meditation_json = json.load(meditation_file)
        for meditation_line in meditation_json:
            output.append(Meditation(meditation_line))
        return output

    def get_pranayamas(self) -> List[Pranayama]:
        """ Reads the pranayama JSON file from the disk and returns a list """
        output = []
        path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["PRANAYAMA_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(path) as pranayama_file:
            pranayama_json = json.load(pranayama_file)
        for cat in pranayama_json:
            for pra in cat["pranayamas"]:
                pranayama = Pranayama(name=pra,
                                      category=cat["category"],
                                      opener=cat["opener"],
                                      closer=cat["closer"])
                output.append(pranayama)
        return output

    def get_warmups(self) -> List[WarmUp]: # pylint: disable=R0201
        """ Reads the warmup JSON file from the disk and returns a list """
        output = []
        path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["WARMUP_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(path) as warmup_file:
            warmup_json = json.load(warmup_file)
        for warmup_line in warmup_json:
            output.append(WarmUp(name=warmup_line["name"],
                                 description=warmup_line["description"],
                                 location=warmup_line["location"]))
        return output

    def get_yoga_classes(self) -> List[YogaClass]:
        """ Reads the yoga class JSON file from the disk and returns a list """
        output = []
        json_file_path = os.path.join(
            self._config["DATA_DIR_PATH"],
            self._config["CLASS_FILE"] + "." + self._config["DATA_FILE_EXTENSION"])
        with open(json_file_path) as class_file:
            json_data = json.load(class_file)
        for json_class in json_data:
            yoga_class = YogaClass(style=str_to_yoga_style(json_class["style"]),
                                   difficulty=str_to_asana_difficulty(json_class["difficulty"]),
                                   name=json_class["name"],
                                   duration=json_class["duration"],
                                   asana_duration=json_class["asana_duration"])
            for sequence_name in json_class["sequence"]:
                stance = str_to_asana_stance(sequence_name)
                yoga_class.sequence.append(stance)
            output.append(yoga_class)
        return output
