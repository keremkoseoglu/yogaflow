""" Image HTML output module """
import os
from typing import List
from yogaflow import config
from yogaflow.writer.abstract_writer import AbstractWriter
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.pranayama import Pranayama
from yogaflow.yoga.asana import Asana


class ImageFinder:
    """ Finds images for asanas """
    _EXTENSIONS = ["jpg", "png"]

    def __init__(self):
        self._img_root = os.path.join(os.getcwd(), "data", "img")
        self._config = config.get()

    def get_image_code(self, asana: Asana, index: int) -> str:
        """ Returns the HTML code for the asana image """
        output = "<figure style='display:inline-block'>"
        output += "<img src='"
        output += self._get_image_path(asana)
        output += "' style='" + self._config["ASANA_IMG_STYLE"] + "'>"
        output += "<figcaption>(" + str(index) + ") " + asana.name + "</figcaption></figure>"
        return output

    def _get_image_path(self, asana: Asana) -> str:
        for extension in ImageFinder._EXTENSIONS:
            path_candidate = os.path.join(self._img_root, asana.name + "." + extension)
            if os.path.isfile(path_candidate):
                return path_candidate
        return ""


class ImgHtmlWriter(AbstractWriter): #pylint: disable=R0903
    """ HTML output class
    This is the default output generator. This class will save
    the generated yoga class as an HTML file and open in the browser.
    """

    def __init__(self):
        self._html = ""
        self._html_file = ""
        self._yoga_class = YogaClass()
        self._config = config.get()
        self._image_finder = ImageFinder()

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
            self._html += "<h2>" + str(flow.name).split(".")[1].capitalize() + "</h2>"
            index = 0
            for asa in flow.asanas:
                index += 1
                self._html += self._image_finder.get_image_code(asa, index)
            self._close_section()

    def _begin_html(self):
        self._html = "<html><head>"
        self._html += "</head><body>"

    def _display_file(self):
        os.system("open " + self._html_file)

    def _end_html(self):
        self._html += "</body></html>"

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
