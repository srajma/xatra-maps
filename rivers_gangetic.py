import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.FlagMap):
    map.River(label="Ganga", value=overpass("1236345"))
    map.River(label="Yamuna", value=overpass("326077"))
    map.River(label="Sarayu", value=overpass("15793911"))
    map.River(label="Ramaganga", value=overpass("6722174"))
    map.River(label="Suvarnanadi", value=overpass("12559166"))
    map.River(label="Campa", value=overpass("247787304"))
    map.River(label="Kaushika", value=overpass("13676883"))
    map.River(label="Kshipra", value=overpass("11117634"))
    map.River(label="Chambal", value=overpass("8385364"))
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)
