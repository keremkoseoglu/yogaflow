"""Primary GUI module"""
from PyQt5.Qt import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QComboBox # pylint: disable=E0611
from yogaflow.reader.json_reader import JsonReader
from yogaflow.generator.primal_generator import PrimalGenerator
from yogaflow.writer.html_writer import HtmlWriter

class Prime(QWidget):
    """ Main GUI window """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        reader = JsonReader()
        self._classes = reader.get_yoga_classes()
        self._pranayamas = reader.get_pranayamas()
        self._warmups = reader.get_warmups()
        self._asanas = reader.get_asanas()
        self._flows = reader.get_flows(self._asanas)
        self._meditations = reader.get_meditations()
        self._selected_class_index = 0

        self._build_gui()

    def _build_gui(self):
        class_label = QLabel(self)
        class_label.setText("Class")

        class_combo = QComboBox(self)
        class_combo.currentIndexChanged.connect(self._class_selected)

        for yoga_class in self._classes:
            class_combo.addItem(yoga_class.name)

        gen_button = QLabel(self)
        gen_button.setText("Generate")
        gen_button.mousePressEvent = self._generate_clicked

        class_layout = QHBoxLayout()
        class_layout.addWidget(class_label)
        class_layout.addWidget(class_combo)
        class_layout.addWidget(gen_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(class_layout)
        self.setLayout(main_layout)
        self.setWindowTitle("YogaFlow")
        self.show()

    def _class_selected(self, i):
        self._selected_class_index = i

    def _generate_clicked(self, event): # pylint: disable=W0613
        selected_class = self._classes[self._selected_class_index]
        generator = PrimalGenerator()
        generator.generate(
            p_yoga_class=selected_class,
            p_pranayamas=self._pranayamas,
            p_warmups=self._warmups,
            p_asanas=self._asanas,
            p_flows=self._flows,
            p_meditations=self._meditations)

        writer = HtmlWriter()
        writer.write(generated_class=selected_class)
