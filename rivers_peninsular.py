import xatra
from xatra.loaders import gadm, naturalearth, overpass
from xatra.territory_library import *
from xatra.colorseq import LinearColorSequence
from matplotlib.colors import LinearSegmentedColormap

def add_flags(map: xatra.FlagMap):
    map.River(label="Narmada", value=overpass("5405552"))
    map.River(label="Godavari", value=overpass("2826093"))
    map.River(label="Krsnaveni", value=overpass("337204"))
    map.River(label="Bhimarathi", value=overpass("2858525"))
    map.River(label="Tungabhadra", value=overpass("2742213"))
    map.River(label="kaveri", value=overpass("2704746"))
    map.CSS(r"""
    .river {stroke-width: 3;}
    """)