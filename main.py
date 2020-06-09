from yogaflow.reader.json_reader import JsonReader
from yogaflow.generator.primal_generator import PrimalGenerator
from yogaflow.yoga.yoga_class import YogaClass
from yogaflow.yoga.yoga_style import YogaStyle
from yogaflow.yoga.asana import AsanaDifficulty
from yogaflow.writer.html_writer import HtmlWriter

yoga_class = YogaClass(
    p_name="Test class",
    p_style=YogaStyle.hatha,
    p_difficulty=AsanaDifficulty.advanced,
    p_duration=60)

reader = JsonReader()
classes = reader.get_yoga_classes()
pranayamas = reader.get_pranayamas()
warmups = reader.get_warmups()
asanas = reader.get_asanas()
flows = reader.get_flows()
meditations = reader.get_meditations()

generator = PrimalGenerator()
generator.generate(
    p_yoga_class=yoga_class,
    p_pranayamas=pranayamas,
    p_warmups=warmups,
    p_asanas=asanas,
    p_flows=flows,
    p_meditations=meditations)

writer = HtmlWriter()
writer.write(generated_class=yoga_class)