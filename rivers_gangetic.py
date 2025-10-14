import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.Map):
    map.River(label="Ganga", value=overpass("1236345"), show_label=True)
    map.River(label="Yamuna", value=overpass("326077"), show_label=True)
    map.River(label="Sarayu", value=overpass("15793911"), show_label=True)
    map.River(label="Ramaganga", value=overpass("6722174"), show_label=True)
    map.River(label="Suvarnanadi", value=overpass("12559166"), show_label=True)
    map.River(label="Campa", value=overpass("247787304"), show_label=True)
    map.River(label="Kaushika", value=overpass("13676883"), show_label=True)
    map.River(label="Kshipra", value=overpass("11117634"), show_label=True)
    map.River(label="Chambal", value=overpass("8385364"), show_label=True)
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)
