""" Default yoga flow generator module """
import copy
from random import randint
from typing import List
from yogaflow.generator.abstract_generator import AbstractGenerator
from yogaflow.generator.primal_asana_generator import PrimalAsanaGenerator
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.asana import Asana
from yogaflow.yoga.yoga_flow import YogaFlow
from yogaflow.yoga.pranayama import Pranayama, PranayamaLocation
from yogaflow.yoga.meditation import Meditation
from yogaflow.yoga.warmup import WarmUp


class PrimalGenerator(AbstractGenerator): #pylint: disable=R0903
    """ Default yoga flow generator class """
    def __init__(self):
        self._yoga_class = YogaClass()
        self._pranayamas = List[Pranayama]
        self._warmups = List[WarmUp]
        self._asanas = List[Asana]
        self._flows = List[YogaFlow]
        self._meditations = List[Meditation]

    def generate(self,
                 p_yoga_class: YogaClass,
                 p_pranayamas: List[Pranayama],
                 p_warmups: List[WarmUp],
                 p_asanas: List[Asana],
                 p_flows: List[YogaFlow],
                 p_meditations: List[Meditation]
                 ): #pylint: disable=R0913
        """ Default yoga flow generation """
        self._yoga_class = p_yoga_class

        self._pranayamas = copy.deepcopy(p_pranayamas)
        self._warmups = copy.deepcopy(p_warmups)
        self._asanas = copy.deepcopy(p_asanas)
        self._flows = copy.deepcopy(p_flows)
        self._meditations = copy.deepcopy(p_meditations)

        self._generate_opening_pranayamas()
        self._generate_warmups()
        self._generate_asanas()
        self._generate_closing_pranayamas()
        self._generate_meditation()

    @staticmethod
    def _generate_pranayamas(p_location: PranayamaLocation,
                             p_source: List[Pranayama],
                             p_target: List[Pranayama]):

        eligible_pranayama_candidates = []

        if p_location == PranayamaLocation.opener:
            number_of_pranayamas_to_generate = 3
            for pranayama_candidate in p_source:
                if pranayama_candidate.opener:
                    eligible_pranayama_candidates.append(pranayama_candidate)
        elif p_location == PranayamaLocation.closer:
            number_of_pranayamas_to_generate = 1
            for pranayama_candidate in p_source:
                if pranayama_candidate.closer:
                    eligible_pranayama_candidates.append(pranayama_candidate)
        else:
            assert False

        for pranayama_iteration in range(0, number_of_pranayamas_to_generate): #pylint: disable=W0612
            eligible_candidate_count = len(eligible_pranayama_candidates)
            if eligible_candidate_count <= 0:
                return
            random_pranayama_index = randint(0, eligible_candidate_count - 1)
            random_pranayama = eligible_pranayama_candidates[random_pranayama_index]
            p_target.append(random_pranayama)
            eligible_pranayama_candidates.remove(random_pranayama)
            p_source.remove(random_pranayama)

    def _generate_asanas(self):
        PrimalAsanaGenerator().generate(self._yoga_class, self._asanas, self._flows)

    def _generate_closing_pranayamas(self):
        PrimalGenerator._generate_pranayamas(
            p_location=PranayamaLocation.closer,
            p_source=self._pranayamas,
            p_target=self._yoga_class.closing_pranayamas)

    def _generate_meditation(self):
        meditation_count = len(self._meditations)
        if meditation_count <= 0:
            return
        meditation_index = randint(0, meditation_count - 1)
        meditation = self._meditations[meditation_index]
        self._yoga_class.meditation = meditation
        self._meditations.remove(meditation)

    def _generate_opening_pranayamas(self):
        PrimalGenerator._generate_pranayamas(
            p_location=PranayamaLocation.opener,
            p_source=self._pranayamas,
            p_target=self._yoga_class.opening_pranayamas)

    def _generate_warmups(self):
        for warmup_iteration in range(0, 5): #pylint: disable=W0612
            remaining_warmup_count = len(self._warmups)
            if remaining_warmup_count <= 0:
                return
            random_warmup_index = randint(0, remaining_warmup_count - 1)
            random_warmup = self._warmups[random_warmup_index]
            self._yoga_class.warmups.append(random_warmup)
            self._warmups.remove(random_warmup)
