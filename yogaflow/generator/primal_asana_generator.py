""" Helper module of primal generator to generate asanas
Since we will be needing a lot of private variables and methods,
I thought it would be a good idea to put them under a separate
module """
from typing import List
from random import randint
from enum import Enum
from copy import copy
from yogaflow import config
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.asana import Asana, is_difficulty_higher, AsanaStance, BendDirection
from yogaflow.yoga.yoga_flow import YogaFlow


class AssetType(Enum):
    """ Defines an asset type """
    UNDEFINED = 0
    ASANA = 1
    FLOW = 2


class AsanaSection:
    """ Defines a section of a class """
    def __init__(self, stance: AsanaStance, remainig_duration: int = 0):
        self.stance = stance
        self.remaining_duration = remainig_duration
        self.flow = YogaFlow(p_name=stance)


class PrimalAsanaGenerator:
    """ Primal asana generator class
    This is intended to be the only class in this module
    """

    def __init__(self):
        self._yoga_class = YogaClass()
        self._asanas = List[Asana]
        self._flows = List[YogaFlow]
        self._config = config.get()
        self._sections = List[AsanaSection]

    def generate(self,
                 p_yoga_class: YogaClass,
                 p_asanas: List[Asana],
                 p_flows: List[YogaFlow]):
        """ Main generation method """
        self._yoga_class = p_yoga_class
        self._build_flow_list(p_flows)
        self._build_asana_list(p_asanas)

        self._reset_sections()
        self._generate_section_flows()
        self._put_section_flows_to_output()

    def _reset_sections(self):
        asana_duration = self._yoga_class.duration
        for percentage in self._config["SECTION_PERCENTAGE"]:
            duration_length = self._yoga_class.duration * self._config["SECTION_PERCENTAGE"][percentage] / 100 # pylint: disable=C0301
            asana_duration -= duration_length
        if asana_duration < 0:
            asana_duration = 0

        self._sections = []
        for part in self._yoga_class.sequence:
            self._sections.append(AsanaSection(part))

        for section in self._sections:
            section.remaining_duration = asana_duration / len(self._sections)

    def _generate_section_flows(self):
        for section in self._sections:
            while section.remaining_duration > 0:
                asset_type = AssetType.UNDEFINED

                usable_asanas = PrimalAsanaGenerator._filter_asanas_by_stance(
                    self._asanas,
                    section.stance)

                usable_flows = PrimalAsanaGenerator._filter_flows_by_stance(
                    self._flows,
                    section.stance)

                if len(usable_flows) <= 0 and len(usable_asanas) <= 0:
                    asset_type = AssetType.UNDEFINED
                elif len(usable_flows) <= 0 and len(usable_asanas) > 0:
                    asset_type = AssetType.ASANA
                elif len(usable_flows) > 0 and len(usable_asanas) <= 0:
                    asset_type = AssetType.FLOW
                elif randint(0, 1) == 0:
                    asset_type = AssetType.ASANA
                else:
                    asset_type = AssetType.FLOW

                if asset_type == AssetType.ASANA:
                    self._append_random_asana(section, usable_asanas)
                elif asset_type == AssetType.FLOW:
                    self._append_random_flow(section, usable_flows)
                else:
                    return

    def _put_section_flows_to_output(self):
        for section in self._sections:
            self._yoga_class.asanas.append(section.flow)

    def _build_flow_list(self, flows: List[YogaFlow]):
        self._flows = []
        for flow in flows:
            if is_difficulty_higher(self._yoga_class.difficulty, flow.get_highest_difficulty()):
                continue
            if self._yoga_class.style not in flow.get_compatible_styles():
                continue
            self._flows.append(flow)

    def _build_asana_list(self, asanas: List[Asana]):
        self._asanas = []
        for asana in asanas:
            if is_difficulty_higher(self._yoga_class.difficulty, asana.difficulty):
                continue
            if self._yoga_class.style not in asana.styles:
                continue
            self._asanas.append(asana)

    def _append_random_asana(self,
                             section: AsanaSection,
                             usable_asanas: List[Asana],
                             counter_pose: bool = True):
        asana_index = randint(0, len(usable_asanas)-1)
        asana = usable_asanas[asana_index]
        section.flow.asanas.append(asana)
        section.remaining_duration -= self._yoga_class.asana_duration
        self._asana_is_used(asana.name)

        if counter_pose:
            if asana.bend_direction == BendDirection.forward:
                self._append_random_bend_asana(section, usable_asanas, BendDirection.back)
            if asana.bend_direction == BendDirection.back:
                self._append_random_bend_asana(section, usable_asanas, BendDirection.forward)

    def _append_random_bend_asana(self,
                                  section: AsanaSection,
                                  usable_asanas: List[Asana],
                                  direction: BendDirection):
        usable_asanas_in_direction = []
        for asana in usable_asanas:
            if asana.bend_direction == direction:
                usable_asanas_in_direction.append(asana)
        if len(usable_asanas_in_direction) <= 0:
            return
        self._append_random_asana(section, usable_asanas_in_direction, counter_pose=False)

    def _append_random_flow(self, section: AsanaSection, usable_flows: List[YogaFlow]):
        flow_index = randint(0, len(usable_flows)-1)
        flow = usable_flows[flow_index]
        asanas = copy(flow.asanas)
        for asana in asanas:
            section.flow.asanas.append(asana)
            section.remaining_duration -= self._yoga_class.asana_duration
            self._asana_is_used(asana.name)

    def _asana_is_used(self, asana_name: str):
        deletable_asana_indices = []
        deletable_flow_indices = []

        asana_index = -1
        for asana in self._asanas:
            asana_index += 1
            if asana.name == asana_name:
                deletable_asana_indices.append(asana_index)

        flow_index = -1
        for flow in self._flows:
            flow_index += 1
            for asana in flow.asanas:
                if asana.name == asana_name:
                    deletable_flow_indices.append(flow_index)
                    break

        deletable_asana_indices.sort(reverse=True)
        deletable_flow_indices.sort(reverse=True)

        for asana_index in deletable_asana_indices:
            self._asanas.pop(asana_index)

        for flow_index in deletable_flow_indices:
            self._flows.pop(flow_index)

    @staticmethod
    def _filter_asanas_by_stance(asanas: List[Asana], stance: AsanaStance) -> List[Asana]:
        output = []
        for asana in asanas:
            if asana.stance == stance:
                output.append(asana)
        return output

    @staticmethod
    def _filter_flows_by_stance(flows: List[YogaFlow], stance: AsanaStance) -> List[YogaFlow]:
        output = []
        for flow in flows:
            asana_match = False
            for asana in flow.asanas:
                if asana.stance == stance:
                    asana_match = True
                    break
            if asana_match:
                output.append(flow)
        return output
        