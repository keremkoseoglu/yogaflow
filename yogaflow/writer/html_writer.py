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
        for flow in self._yoga_class.asanas:
            self._open_section(str(flow.name).split(".")[1].capitalize())
            for asa in flow.asanas:
                self._html += "<li>" + asa.name + "</li>"
            self._close_section()

    def _begin_html(self):
        self._html = "<html><head>"
        self._html += "<style>"
        self._html += ".check-list {margin: 0; padding-left: 1.2rem;} "
        self._html += ".check-list li {position: relative; list-style-type: none; padding-left: 2.5rem; margin-bottom: 0.5rem;}"
        self._html += ".check-list li:before {content: ''; display: block; position: absolute; "
        self._html += "left: 0; top: -2px; width: 5px; height: 11px; border-width: 0 2px 2px 0; "
        self._html += "border-style: solid; border-color: #00a8a8; transform-origin: bottom left; transform: rotate(45deg);} "
        self._html += "*, *:before, *:after {box-sizing: border-box;} "
        self._html += "html {-webkit-font-smoothing: antialiased; font-family: \"Helvetica Neue\", sans-serif; font-size: 62.5%;} "
        self._html += "body {font-size: 1.6rem; background-color: #efefef; color: #324047} "
        self._html += "html, body, section {height: 100%;} "
        self._html += "section {max-width: 400px; margin-left: auto; margin-right: auto; display: flex; align-items: center;} "
        self._html += "div {margin: auto;} "
        self._html += "</style>"
        self._html += "</head><body><section><div>"

    def _display_file(self):
        os.system("open " + self._html_file)

    def _end_html(self):
        self._html += "</div></section></body></html>"

    def _generate_html(self):
        self._begin_html()

        self._open_section("Opening Pranayamas")
        self._pranayamas(self._yoga_class.opening_pranayamas)
        self._close_section()

        self._open_section("Warmups")
        self._warmups()
        self._close_section()

        self._asanas()

        self._open_section("Closure")
        self._pranayamas(self._yoga_class.closing_pranayamas)
        self._close_section()

        self._open_section("Meditation")
        self._html += "<li>" + self._yoga_class.meditation.name + "</li>"
        self._close_section()
        self._end_html()

    def _pranayamas(self, p_pranayamas: List[Pranayama]):
        for pranayama in p_pranayamas:
            self._html += "<li>" + pranayama.name + "</li>"

    def _save_file(self):
        file2 = open(self._html_file, "w+")
        file2.write(self._html)
        file2.close()

    def _warmups(self):
        for warmup in self._yoga_class.warmups:
            self._html += "<li>" + warmup.name
            if warmup.description != "":
                self._html += " <small><i>(" + warmup.description + ")</i></small>"
            self._html += "</li>"

    def _open_section(self, title: str):
        self._html += "<h2>"
        self._html += title
        self._html += "</h2><ul class=\"check-list\">"

    def _close_section(self):
        self._html += "</ul>"
