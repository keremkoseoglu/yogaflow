""" Configuration module """
import json
import os


_CONFIG = {}


def get() -> dict:
    """ Reads and returns configuration """
    global _CONFIG
    if _CONFIG == {}:
        _read_config()
    return _CONFIG


def _read_config():
    global _CONFIG
    config_path = os.path.join(os.getcwd(), "config.json")
    with open(config_path) as config_file:
        _CONFIG = json.load(config_file)
