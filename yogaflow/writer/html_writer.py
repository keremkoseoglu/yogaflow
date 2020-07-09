""" HTML output module """
import os
from typing import List
from yogaflow import config
from yogaflow.writer.abstract_writer import AbstractWriter
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.pranayama import Pranayama


class HtmlWriter(AbstractWriter): #pylint: disable=R0903
    """ HTML output class
    This is the default output generator. This class will save
    the generated yoga class as an HTML file and open in the browser.
    """

    def __init__(self):
        self._html = ""
        self._html_file = ""
        self._yoga_class = YogaClass()
        self._config = config.get()

    def write(self, generated_class: YogaClass):
        """ HTML generation entry point """
        self._yoga_class = generated_class

        self._html_file = os.path.join(
            self._config["DOWNLOAD_DIR"],
            self._yoga_class.name.replace(" ", "_") + ".html")

        self._generate_html()
        self._save_file()
        self._display_file()

    def _asanas(self):
        self._html += "<b>Asanas: </b>"
        for asa in self._yoga_class.asanas:
            if asa != self._yoga_class.asanas[0]:
                self._html += ", "
            self._html += asa.name

    def _begin_html(self):
        self._html = "<html><head>"
        self._html += "<style>"
        self._html += "td { font-family: Arial; font-size: 30px; padding: 5px; }"
        self._html += "tr:nth-child(even) { background: #CCC }"
        self._html += "tr:nth-child(odd) {background: #FFF }"
        self._html += "</style>"
        self._html += "</head><body>"

    def _closing_pranayamas(self):
        self._pranayamas("Closing Pranayamas", self._yoga_class.closing_pranayamas)

    def _display_file(self):
        os.system("open " + self._html_file)

    def _end_html(self):
        self._html += "</body></html>"

    def _generate_html(self):
        self._begin_html()
        self._html += "<h1>Preparation</h1>"
        self._opening_pranayamas()
        self._html += "<br>"
        self._warmups()
        self._html += "<h1>Main Flow</h1>"
        self._asanas()
        self._html += "<h1>Closure</h1>"
        self._closing_pranayamas()
        self._html += "<br>"
        self._meditation()
        self._end_html()

    def _meditation(self):
        self._html += "<b>Meditation: </b>" + self._yoga_class.meditation.name

    def _opening_pranayamas(self):
        self._pranayamas("Opening Pranayamas", self._yoga_class.opening_pranayamas)

    def _pranayamas(self, p_title: str, p_pranayamas: List[Pranayama]):
        self._html += "<b>" + p_title + ": </b>"
        for pranayama in p_pranayamas:
            if pranayama != p_pranayamas[0]:
                self._html += ", "
            self._html += pranayama.name

    def _save_file(self):
        file2 = open(self._html_file, "w+")
        file2.write(self._html)
        file2.close()

    def _warmups(self):
        self._html += "<b>Warmups: </b>"
        for warmup in self._yoga_class.warmups:
            if warmup != self._yoga_class.warmups[0]:
                self._html += ", "
            self._html += warmup.name
            if warmup.description != "":
                self._html += " <small><i>(" + warmup.description + ")</i></small>"
