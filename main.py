"""Main entry point"""
from os import path
import subprocess
from flask import Flask, jsonify, request
import webview
from yogaflow import config, output
from yogaflow.reader import json_reader, yoga_database
from yogaflow.generator import primal_generator
from yogaflow.writer import html_writer, img_html_writer

_APP = Flask(__name__, static_folder=path.join("web", "static"))
_WINDOW = webview.create_window("YogaFlow", _APP, width=800, height=284)

@_APP.route("/")
def home():
    """ Main view """
    return _APP.send_static_file("index.html")

@_APP.route("/api/outputs")
def api_outputs():
    """ Outputs """
    return jsonify(output.get_output_dict())

@_APP.route("/api/classes")
def api_classes():
    """ Classes """
    return jsonify(_get_yoga_db().yoga_class_list)

@_APP.route("/api/edit_files")
def api_edit():
    """ Edit file """
    data_path = config.get()["DATA_DIR_PATH"]
    subprocess.call(["open", data_path])
    return ""

@_APP.route("/api/generate")
def api_generate():
    """ Generate """
    yoga_db = _get_yoga_db()
    selected_class = yoga_db.get_yoga_class_by_name(request.args.get("class"))
    generator = primal_generator.PrimalGenerator()
    generator.generate(
        p_yoga_class=selected_class,
        p_pranayamas=yoga_db.pranayamas,
        p_warmups=yoga_db.warmups,
        p_asanas=yoga_db.asanas,
        p_flows=yoga_db.flows,
        p_meditations=yoga_db.meditations)

    selected_output = request.args.get("output")
    if selected_output == output.Output.HTML.name:
        writer = html_writer.HtmlWriter()
    if selected_output == output.Output.IMG_HTML.name:
        writer = img_html_writer.ImgHtmlWriter()
    writer.write(generated_class=selected_class)
    return ""

def _get_yoga_db() -> yoga_database.YogaDatabase:
    return yoga_database.YogaDatabase(json_reader.JsonReader())

if __name__ == "__main__":
    #_APP.run(host="0.0.0.0", port=5001, debug=True)
    webview.start()
