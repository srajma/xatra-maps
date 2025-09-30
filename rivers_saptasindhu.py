import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.FlagMap):
    map.River(label="Sindhu", value=overpass("1159233"))
    map.River(label="Vitasta (jhelum)", value=overpass("8306691"))
    map.River(label="Chandrabhaga (chenab)", value=overpass("6085682"))
    map.River(label="Iravati (ravi)", value=overpass("8894611"))
    map.River(label="Satadru (sutlej)", value=overpass("325142"))
    map.River(label="Campavipasa (beas)", value=overpass("10693630"))
    map.River(label="Sarasvati (ghaggar)", value=overpass("5388381"))