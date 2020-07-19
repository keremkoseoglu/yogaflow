"""Primary GUI module"""
from enum import Enum
from PyQt5.Qt import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QComboBox # pylint: disable=E0611
from yogaflow.reader.json_reader import JsonReader
from yogaflow.reader.yoga_database import YogaDatabase
from yogaflow.generator.primal_generator import PrimalGenerator
from yogaflow.writer.html_writer import HtmlWriter
from yogaflow.writer.img_html_writer import ImgHtmlWriter


class Output(Enum):
    """ Output (writer) enum """
    HTML = 1
    IMG_HTML = 2


class Prime(QWidget):
    """ Main GUI window """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._outputs = [Output.IMG_HTML, Output.HTML]
        self._yoga_db = YogaDatabase(JsonReader())
        self._selected_class_index = 0
        self._selected_output_index = 0

        self._build_gui()

    def _build_gui(self):
        class_label = QLabel(self)
        class_label.setText("Class")
        class_combo = QComboBox(self)
        class_combo.currentIndexChanged.connect(self._class_selected)
        for yoga_class in self._yoga_db.classes:
            class_combo.addItem(yoga_class.name)
        class_layout = QHBoxLayout()
        class_layout.addWidget(class_label)
        class_layout.addWidget(class_combo)

        output_label = QLabel(self)
        output_label.setText("Output")
        output_combo = QComboBox(self)
        output_combo.currentIndexChanged.connect(self._output_selected)
        for output in self._outputs:
            output_combo.addItem(output.name)
        output_layout = QHBoxLayout()
        output_layout.addWidget(output_label)
        output_layout.addWidget(output_combo)

        gen_button = QLabel(self)
        gen_button.setText("Generate")
        gen_button.mousePressEvent = self._generate_clicked

        main_layout = QVBoxLayout()
        main_layout.addLayout(class_layout)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(gen_button)
        self.setLayout(main_layout)
        self.setWindowTitle("YogaFlow")
        self.show()

    def _class_selected(self, i):
        self._selected_class_index = i

    def _output_selected(self, i):
        self._selected_output_index = i

    def _generate_clicked(self, event): # pylint: disable=W0613
        selected_class = self._yoga_db.classes[self._selected_class_index]
        generator = PrimalGenerator()
        generator.generate(
            p_yoga_class=selected_class,
            p_pranayamas=self._yoga_db.pranayamas,
            p_warmups=self._yoga_db.warmups,
            p_asanas=self._yoga_db.asanas,
            p_flows=self._yoga_db.flows,
            p_meditations=self._yoga_db.meditations)

        selected_output = self._outputs[self._selected_output_index]
        if selected_output == Output.HTML:
            writer = HtmlWriter()
        if selected_output == Output.IMG_HTML:
            writer = ImgHtmlWriter()
        writer.write(generated_class=selected_class)
