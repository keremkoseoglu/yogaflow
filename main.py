"""Main entry point"""
import os
from PyQt5.Qt import QApplication
from gui.prime import Prime


APP = QApplication([])
P = Prime()
os._exit(APP.exec_()) # pylint: disable=W0212
